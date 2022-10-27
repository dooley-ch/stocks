# *******************************************************************************************
#  File:  _z_peer_map.py
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

__all__ = ['zPeerMapRecord_insert', 'zPeerMapRecord_get_by_ticker']

import related
import pymysql
from .. model import zPeerMapRecord


def zPeerMapRecord_insert(record: zPeerMapRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO z_peer_map (ticker, peer) VALUES (%s, %s);", (record.ticker, record.peer))
        return cursor.lastrowid


def zPeerMapRecord_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zPeerMapRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT DISTINCT ticker, peer, 0 AS id FROM z_peer_map 
                            WHERE (ticker = %s);""", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zPeerMapRecord, row)
                records.append(record)
            return records
