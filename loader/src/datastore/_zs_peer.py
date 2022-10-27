# *******************************************************************************************
#  File:  _zs_peer.py
#
#  Created: 27-09-2022
#
#  History:
#  27-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['zsPeerRecord_insert', 'zsPeerRecord_get_by_ticker']

import related
import pymysql
from .. model import zsPeerRecord


def zsPeerRecord_insert(record: zsPeerRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO zs_peer (ticker, peer) VALUES (%s, %s);", (record.ticker, record.peer))
        return cursor.lastrowid


def zsPeerRecord_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zsPeerRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, peer FROM zs_peer WHERE (ticker = %s);", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zsPeerRecord, row)
                records.append(record)
            return records
