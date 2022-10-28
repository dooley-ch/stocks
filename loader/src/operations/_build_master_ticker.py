# *******************************************************************************************
#  File:  _build_master_ticker.py
#
#  Created: 11-10-2022
#
#  History:
#  11-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['build_master_ticker_table']

import pymysql
import loguru
from .. import config
from .. import datastore as ds


@loguru.logger.catch(reraise=True)
def _insert_sp600(db_conn: pymysql.Connection) -> int:
    """
    This function imports the S&P 600 index components
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_master_ticker(ticker, company)
                            SELECT ticker, company FROM z_sp_600 
                                WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);""")
        return cursor.rowcount


@loguru.logger.catch(reraise=True)
def _insert_sp400(db_conn: pymysql.Connection) -> int:
    """
    This function imports the S&P 400 index components
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_master_ticker(ticker, company)
                            SELECT ticker, company FROM z_sp_400 
                                WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);""")
        return cursor.rowcount


@loguru.logger.catch(reraise=True)
def _insert_sp500(db_conn: pymysql.Connection) -> int:
    """
    This function imports the S&P 500 index components
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_master_ticker(ticker, company)
                            SELECT ticker, company FROM z_sp_500 
                                WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);""")
        return cursor.rowcount


@loguru.logger.catch(reraise=True)
def build_master_ticker_table() -> bool:
    """
    This function builds the master ticker table
    """
    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_master_ticker;")

    rows = _insert_sp600(db_conn)
    rows += _insert_sp400(db_conn)
    rows += _insert_sp500(db_conn)

    loguru.logger.info(f"Master ticker list built: {rows} rows inserted.")

    return  rows > 1450
