# *******************************************************************************************
#  File:  _build_companies.py
#
#  Created: 17-10-2022
#
#  History:
#  17-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['build_companies']

from loguru import logger

from .. import config
from .. import datastore as ds
from .. import model


# noinspection SqlWithoutWhere
@logger.catch(reraise=True)
def build_companies() -> bool:
    """
    This function builds the company master records
    """
    company_count = 0
    peer_count = 0

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM zs_company;")
        cursor.execute("DELETE FROM zs_peer;")

    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO zs_company(ticker, name, description, is_active)
            SELECT ticker, company, 'No description available', 1 FROM z_master_ticker;""")
        company_count = cursor.rowcount

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE zs_company c
                            INNER JOIN z_cik zc on c.ticker = zc.ticker
                            SET c.stock_exchange = zc.exchange, c.cik_number = zc.cik;""")

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE zs_company c
                            INNER JOIN z_openfigi f on c.ticker = f.ticker
                            SET c.figi_code = f.open_figi;""")

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE zs_company c
                            INNER JOIN z_simfin_companies zsc on c.ticker = zsc.ticker
                            SET c.simfin_number = zsc.simfin_id;""")

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE zs_company c
                            INNER JOIN z_morningstar_profile m on c.ticker = m.ticker
                            SET c.description = m.description;""")

    with db_conn.cursor() as cursor:
        cursor.execute("UPDATE zs_company set is_sp100 = 1 WHERE ticker IN (SELECT ticker FROM z_sp_100);")

    with db_conn.cursor() as cursor:
        cursor.execute("UPDATE zs_company set is_sp600 = 1 WHERE ticker IN (SELECT ticker FROM z_sp_600);")

    with db_conn.cursor() as cursor:
        cursor.execute("UPDATE zs_company set is_sp400 = 1 WHERE ticker IN (SELECT ticker FROM z_sp_400);")

    with db_conn.cursor() as cursor:
        cursor.execute("UPDATE zs_company set is_sp500 = 1 WHERE ticker IN (SELECT ticker FROM z_sp_500);")

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE zs_company SET company_type_id = 1, has_financials = 1
                  WHERE ticker IN (SELECT ticker FROM z_balance_sheet_general_annual);""")

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE zs_company SET company_type_id = 2, has_financials = 1
                  WHERE ticker IN (SELECT ticker FROM z_balance_sheet_bank_annual);""")

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE zs_company SET company_type_id = 3, has_financials = 1
                  WHERE ticker IN (SELECT ticker FROM z_balance_sheet_insurance_annual);""")

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE company c INNER JOIN z_balance_sheet_general_annual b on c.ticker = b.ticker
                                SET c.currency = b.currency
                            WHERE c.ticker IN (SELECT ticker from z_balance_sheet_general_annual);""")

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE company c INNER JOIN z_balance_sheet_bank_annual b on c.ticker = b.ticker
                                SET c.currency = b.currency
                            WHERE c.ticker IN (SELECT ticker from z_balance_sheet_bank_annual);""")

    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE company c INNER JOIN z_balance_sheet_insurance_annual b on c.ticker = b.ticker
                                SET c.currency = b.currency
                            WHERE c.ticker IN (SELECT ticker from z_balance_sheet_insurance_annual);""")

    # Add the industry ids
    sector_records = ds.zsSectorRecord_get_all(db_conn)
    if sector_records is None:
        raise ValueError("No Sector records found")
    sector_map = {row.name: row.id for row in sector_records}

    # Set default industry for all companies
    sector_id = sector_map['Unknown']
    industry_records = ds.zsIndustryRecord_get_by_sector(sector_id, db_conn)
    if not industry_records:
        raise ValueError("No Sector records found for Unknown sector")
    industry_id = industry_records[0].id
    with db_conn.cursor() as cursor:
        cursor.execute("UPDATE zs_company SET industry_id = %s", (industry_id,))

    companies = ds.zsCompanyRecord_get_tickers(db_conn)
    if companies:
        for company in companies:
            simfin_company = ds.zSimFinCompanies_get_by_ticker(company.ticker, db_conn)
            if simfin_company:
                simfin_industry = ds.zSimFinIndustries_get_by_industry_id(simfin_company.industry_id, db_conn)
                if simfin_industry:
                    sector_id = sector_map[simfin_industry.sector]
                    industries = ds.zsIndustryRecord_get_by_sector(sector_id, db_conn)
                    if industries:
                        industry_map = {row.name: row.id for row in industries}
                        if simfin_industry.industry in industry_map:
                            industry_id = industry_map[simfin_industry.industry]

                            # Update company record
                            with db_conn.cursor() as cursor:
                                cursor.execute("UPDATE zs_company SET industry_id = %s WHERE (id = %s);",
                                               (industry_id, company.id))

    # Add peers
    if companies:
        for company in companies:
            peers = ds.zPeerMapRecord_get_by_ticker(company.ticker, db_conn)
            if peers:
                for peer in peers:
                    peer_count += 1

                    try:
                        ds.zsPeerRecord_insert(model.zsPeerRecord(ticker=company.ticker, peer=peer.peer), db_conn)
                    except ValueError as e:
                        logger.warning(f"Failed to insert peer record: {company.ticker} -> {peer.peer}")

    logger.info(f"Build Company - Total companies: {company_count} - Total peers: {peer_count}")

    return True
