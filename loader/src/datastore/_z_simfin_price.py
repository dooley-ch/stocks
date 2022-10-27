# *******************************************************************************************
#  File:  _z_simfin_price.py
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

__all__ = ['zSimFinPrice_insert', 'zSimFinPrice_get_ticker']

import related
import pymysql
from .. model import zSimFinPrice


def zSimFinPrice_insert(record: zSimFinPrice, db_conn: pymysql.Connection) -> int:
    """
    This function inserts a record in the table
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the new record id
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_simfin_price(ticker, simfin_id, price_date, open_price, low_price, high_price, 
                                close_price, adjusted_close_price, dividend, volume, shares_outstanding) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.price_date, record.open_price, record.low_price,
                        record.high_price, record.close_price, record.adjusted_close_price, record.dividend,
                        record.volume, record.shares_outstanding))
        return cursor.lastrowid


def zSimFinPrice_get_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zSimFinPrice] | None:
    """
    This function returns the prices for a given ticker
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the list of prices associated with the ticker
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, price_date, open_price, low_price, high_price, close_price, 
                                adjusted_close_price, dividend, volume, shares_outstanding 
                            FROM z_simfin_price WHERE (ticker = %s);""", (ticker,))

        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zSimFinPrice, row)
                records.append(record)
            return records
