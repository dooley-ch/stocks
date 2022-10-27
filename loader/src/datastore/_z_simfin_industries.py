# *******************************************************************************************
#  File:  _z_simfin_industries.py
#
#  Created: 28-09-2022
#
#  History:
#  28-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['zSimFinIndustries_insert', 'zSimFinIndustries_get_all', 'zSimFinIndustries_get_sectors',
           'zSimFinIndustries_get_industries_by_sector', 'zSimFinIndustries_get_by_industry_id']

import related
import pymysql
from .. model import zSimFinIndustriesRecord


def zSimFinIndustries_insert(record: zSimFinIndustriesRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_simfin_industries(industry_id, sector, industry) VALUES (%s, %s, %s);""",
                       (record.industry_id, record.sector, record.industry))
        return cursor.lastrowid


def zSimFinIndustries_get_all(db_conn: pymysql.Connection) -> list[zSimFinIndustriesRecord] | None:
    """
    This function returns all record from the table
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, industry_id, sector, industry FROM z_simfin_industries;")
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zSimFinIndustriesRecord, row)
                records.append(record)
            return records


def zSimFinIndustries_get_sectors(db_conn: pymysql.Connection) -> list[str] | None:
    """
    This function returns the unique names of the sectors
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT DISTINCT sector FROM z_simfin_industries;")
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                # noinspection PyTypeChecker
                records.append(row['sector'])
            return records


def zSimFinIndustries_get_industries_by_sector(sector_name: str, db_conn: pymysql.Connection) -> list[str] | None:
    """
    This function returns the unique names of the sectors
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT DISTINCT industry FROM z_simfin_industries WHERE (sector = %s);", (sector_name,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                # noinspection PyTypeChecker
                records.append(row['industry'])
            return records


def zSimFinIndustries_get_by_industry_id(industry_id: int, db_conn: pymysql.Connection) -> zSimFinIndustriesRecord | None:
    """
    This function returns all record from the table
    :param industry_id: The id to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, industry_id, sector, industry FROM z_simfin_industries WHERE (industry_id = %s);",
                       (industry_id,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zSimFinIndustriesRecord, row)
            return record
