# *******************************************************************************************
#  File:  _z_master_ticker.py
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

__all__ = ['zMasterTicker_insert', 'zMasterTicker_get_by_ticker', 'zMasterTicker_get_all']

import related
import pymysql
from .. model import zMasterTickerRecord


def zMasterTicker_insert(record: zMasterTickerRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO z_master_ticker (ticker, company) VALUES (%s, %s);", (record.ticker, record.company))
        return cursor.lastrowid


def zMasterTicker_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zMasterTickerRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, company FROM z_master_ticker WHERE (ticker = %s);", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zMasterTickerRecord, row)
            return record


def zMasterTicker_get_all(db_conn: pymysql.Connection) -> list[zMasterTickerRecord] | None:
    """
    This function returns all record from the table
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, company FROM z_master_ticker")
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(zMasterTickerRecord, row)
                records.append(record)

            return records
