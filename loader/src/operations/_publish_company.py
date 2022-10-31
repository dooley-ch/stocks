# *******************************************************************************************
#  File:  _publish_company.py
#
#  Created: 18-10-2022
#
#  History:
#  18-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['publish_company']

import pymysql
from loguru import logger
from .. import datastore as ds
from .. import model
from .. import config


def _build_sectors(db_conn: pymysql.Connection) -> None:
    """
    This function rebuilds the sector table
    """
    updated_rows = 0
    inserted_rows = 0

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE sector SET is_active = 0, lock_version = lock_version + 1, updated_at = CURRENT_TIMESTAMP 
                            WHERE name NOT IN (SELECT name FROM zs_sector);""")
        updated_rows = cursor.rowcount

    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO sector (name) SELECT name FROM zs_sector WHERE name NOT IN (SELECT name FROM sector);")
        inserted_rows = cursor.rowcount

    logger.info(f"Sectors - Updated: {updated_rows}, Inserted {inserted_rows}")


def _build_industries(db_conn: pymysql.Connection) -> None:
    """
    This function rebuilds the industry table
    """
    updated_rows = 0
    inserted_rows = 0

    def deactivate_industry(record_id: int, db_conn_x: pymysql.Connection) -> None:
        with db_conn_x.cursor() as cursor:
            cursor.execute("""UPDATE industry SET is_active = 0, lock_version = lock_version + 1, 
                                updated_at = CURRENT_TIMESTAMP() WHERE (id = %s)""", (record_id,))

    sectors = ds.sector_get_all(db_conn)
    staging_sectors = ds.zsSectorRecord_get_all(db_conn)

    if sectors and staging_sectors:
        staging_sectors_map = {row.name: row for row in staging_sectors}

        for sector in sectors:
            industries = ds.industry_get_by_sector(sector.id, db_conn)
            if industries:
                industries_map = {row.name: row for row in industries}
            else:
                industries_map = {}

            if sector.is_active:
                if sector.name in staging_sectors_map:
                    staging_sectors_id = staging_sectors_map[sector.name].id
                    staging_industries = ds.zsIndustryRecord_get_by_sector(staging_sectors_id, db_conn)
                    if staging_industries:
                        staging_industries_map = {row.name: row for row in staging_industries}

                        if industries:
                            for industry in industries:
                                if industry.name not in staging_industries_map:
                                    deactivate_industry(industry.id, db_conn)
                                    updated_rows += 1

                        for staging_industry in staging_industries:
                            if staging_industry.name not in industries_map:
                                ds.industry_insert(
                                    model.Industry(name=staging_industry.name, sector_id=sector.id), db_conn)
                                inserted_rows += 1
            else:
                # If sector is not active, then neither should the underlying industries
                if industries:
                    for industry in industries:
                        deactivate_industry(industry.id, db_conn)
                        updated_rows += 1

    logger.info(f"Industries - Updated: {updated_rows}, Inserted {inserted_rows}")


def _get_industry_id(sector_name: str, industry_name: str, db_conn: pymysql.Connection) -> int:
    """
    This function returns the id for the industry titled 'Unknown' in the public tables
    """
    sector = ds.sector_get_by_name(sector_name, db_conn)
    if sector is None:
        raise ValueError(f"Sector titled {sector_name} not found!")

    industries = ds.industry_get_by_sector(sector.id, db_conn)

    for industry in industries:
        if industry.name == industry_name:
            return industry.id

    raise ValueError(f"Industry titled {industry_name} not found")


def _update_industry_codes(db_conn: pymysql.Connection) -> None:
    """
    This function updates the
    """
    companies = ds.company_get_tickers(db_conn)

    for company in companies:
        zs_company = ds.zsCompanyRecord_get(company.ticker, db_conn)
        if zs_company:
            zs_industry = ds.zsIndustryRecord_get(zs_company.industry_id, db_conn)
            zs_sector = ds.zsSectorRecord_get(zs_industry.sector_id, db_conn)

            industry_id = _get_industry_id(zs_sector.name, zs_industry.name, db_conn)

            with db_conn.cursor() as cursor:
                cursor.execute("""UPDATE company SET industry_id = %s, lock_version = lock_version + 1, 
                                        updated_at = CURRENT_TIMESTAMP WHERE (id = %s)""", (industry_id, company.id))


# noinspection SqlWithoutWhere
@logger.catch(reraise=True)
def publish_company() -> bool:
    """
    This function populates the public company tables from the staging tables
    """
    updated_rows = 0
    inserted_rows = 0
    deactivated_rows = 0

    db_conn = ds.get_connection(config.database_info())

    _build_sectors(db_conn)
    _build_industries(db_conn)

    unknown_ind_id = _get_industry_id('Unknown', 'Unknown', db_conn)

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE company SET is_active = 0, lock_version = lock_version + 1, 
                            updated_at = CURRENT_TIMESTAMP WHERE ticker NOT IN (SELECT ticker FROM zs_company);""")
        deactivated_rows = cursor.rowcount

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE company c
                            INNER JOIN  zs_company zc on c.ticker = zc.ticker
                                SET c.name = zc.name,
                                    c.currency = zc.currency,
                                    c.description = zc.description,
                                    c.stock_exchange = zc.stock_exchange,
                                    c.cik_number = zc.cik_number,
                                    c.figi_code = zc.figi_code,
                                    c.simfin_number = zc.simfin_number,
                                    c.is_sp100 = zc.is_sp100,
                                    c.is_sp600 = zc.is_sp600,
                                    c.is_sp400 = zc.is_sp400,
                                    c.is_sp500 = zc.is_sp500,
                                    c.company_type_id = zc.company_type_id,
                                    c.industry_id = %s,
                                    c.has_financials = zc.has_financials,
                                    c.lock_version = c.lock_version + 1,
                                    c.updated_at = CURRENT_TIMESTAMP
                            WHERE c.is_active = 1;""", (unknown_ind_id,))
        updated_rows = cursor.rowcount

    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO company(ticker, name, currency, description, stock_exchange, cik_number, 
                                                figi_code, simfin_number, is_sp100, is_sp600, is_sp400, is_sp500, 
                                                company_type_id, industry_id, is_active, has_financials)
                            SELECT ticker, name, currency, description, stock_exchange, cik_number, figi_code, 
                                    simfin_number, is_sp100, is_sp600, is_sp400, is_sp500, company_type_id, %s, 
                                    is_active, has_financials FROM zs_company
                            WHERE ticker NOT IN (SELECT ticker from company);""", (unknown_ind_id,))
        inserted_rows = cursor.rowcount

    _update_industry_codes(db_conn)

    logger.info(f"Companies - Deactivated: {deactivated_rows}, Updated: {updated_rows}, Inserted {inserted_rows}")

    return True
