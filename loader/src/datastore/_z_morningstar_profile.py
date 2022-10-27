# *******************************************************************************************
#  File:  _z_morningstar_profile.py
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

__all__ = ['zMorningstarProfileRecord_insert', 'zMorningstarProfileRecord_get_by_ticker']

import related
import pymysql
from .. model import zMorningstarProfileRecord


def zMorningstarProfileRecord_insert(record: zMorningstarProfileRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_morningstar_profile (ticker, company_name, description, sector, industry, 
                            recent_earnings, fiscal_year_end, stock_type, employees) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.company_name, record.description, record.sector, record.industry,
                        record.recent_earnings, record.fiscal_year_end, record.stock_type, record.employees))
        return cursor.lastrowid


def zMorningstarProfileRecord_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zMorningstarProfileRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, company_name, description, sector, industry, recent_earnings, 
                            fiscal_year_end, stock_type, employees 
                            FROM z_morningstar_profile WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zMorningstarProfileRecord, row)
            return record
