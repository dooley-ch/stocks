# *******************************************************************************************
#  File:  _z_openfigi.py
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

__all__ = ['zOpenFIGI_insert', 'zOpenFIGI_get_by_ticker']

import related
import pymysql
from .. model import zOpenFIGIRecord


def zOpenFIGI_insert(record: zOpenFIGIRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO z_openfigi (ticker, open_figi) VALUES (%s, %s);", (record.ticker, record.open_figi))
        return cursor.lastrowid


def zOpenFIGI_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zOpenFIGIRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, open_figi FROM z_openfigi WHERE (ticker = %s);", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zOpenFIGIRecord, row)
            return record
