# *******************************************************************************************
#  File:  _trim_data.py
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

__all__ = ['scrub_filter_imported_data']

import pymysql
from loguru import logger
from .. import datastore as ds
from .. import config


def _scrub_simfin_companies(db_conn: pymysql.Connection) -> None:
    """
    This function deletes all data in the table not in the master_ticker table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM z_simfin_companies WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Companies scrubbed from simfin companies: {cursor.rowcount}")


def _scrub_simfin_income(db_conn: pymysql.Connection) -> None:
    """
    This function deletes all data in the table not in the master_ticker table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM z_income_general_quarter WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin general income - quarter: {cursor.rowcount}")

        cursor.execute("DELETE FROM z_income_general_annual WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin general income - annual: {cursor.rowcount}")

        cursor.execute("DELETE FROM z_income_bank_quarter WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin bank income - quarter: {cursor.rowcount}")

        cursor.execute("DELETE FROM z_income_bank_annual WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin bank income - annual: {cursor.rowcount}")

        cursor.execute(
            "DELETE FROM z_income_insurance_quarter WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        rowcount_insurance_quarter = cursor.rowcount
        cursor.execute(
            "DELETE FROM z_income_insurance_annual WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin Insurance income - quarter: {cursor.rowcount}")


def _scrub_cashflow(db_conn: pymysql.Connection) -> None:
    """
    This function deletes all data in the table not in the master_ticker table
    """
    with db_conn.cursor() as cursor:
        cursor.execute(
            "DELETE FROM z_cashflow_general_quarter WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin general cashflow - quarter: {cursor.rowcount}")
        cursor.execute(
            "DELETE FROM z_cashflow_general_annual WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin general cashflow - annual: {cursor.rowcount}")

        cursor.execute("DELETE FROM z_cashflow_bank_quarter WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin bank cashflow - quarter: {cursor.rowcount}")
        cursor.execute("DELETE FROM z_cashflow_bank_annual WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin bank cashflow - annual: {cursor.rowcount}")

        cursor.execute(
            "DELETE FROM z_cashflow_insurance_quarter WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin insurance cashflow - quarter: {cursor.rowcount}")
        cursor.execute(
            "DELETE FROM z_cashflow_insurance_annual WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin insurance cashflow - annual: {cursor.rowcount}")


def _scrub_balance_sheet(db_conn: pymysql.Connection) -> None:
    """
    This function deletes all data in the table not in the master_ticker table
    """
    with db_conn.cursor() as cursor:
        cursor.execute(
            "DELETE FROM z_balance_sheet_general_quarter WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin General balance sheet - quarter: {cursor.rowcount}")
        cursor.execute(
            "DELETE FROM z_balance_sheet_general_annual WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin General balance sheet - annual: {cursor.rowcount}")

        cursor.execute(
            "DELETE FROM z_balance_sheet_bank_quarter WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin Bank balance sheet - quarter: {cursor.rowcount}")
        cursor.execute(
            "DELETE FROM z_balance_sheet_bank_annual WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin Bank balance sheet - annual: {cursor.rowcount}")

        cursor.execute(
            "DELETE FROM z_balance_sheet_insurance_quarter WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin Insurance balance sheet - quarter: {cursor.rowcount}")
        cursor.execute(
            "DELETE FROM z_balance_sheet_insurance_annual WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from simfin Insurance balance sheet - annual: {cursor.rowcount}")


def _trim_peer_map(db_conn: pymysql.Connection) -> None:
    """
    This function deletes all data in the table not in the master_ticker table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM z_peer_map WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from Peer Map: {cursor.rowcount}")


def _trim_cik(db_conn: pymysql.Connection) -> None:
    """
    This function deletes all data in the table not in the master_ticker table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM z_cik WHERE ticker NOT IN (SELECT ticker FROM z_master_ticker);")
        logger.info(f"Records deleted from CIK table: {cursor.rowcount}")


@logger.catch(reraise=True)
def scrub_filter_imported_data() -> None:
    """
    This function deletes unnecessary data from the import tables
    """
    db_conn = ds.get_connection(config.database_info())

    logger.info("*** Started scrubbing data")

    _scrub_simfin_companies(db_conn)
    _scrub_simfin_income(db_conn)
    _scrub_cashflow(db_conn)
    _scrub_balance_sheet(db_conn)
    _trim_peer_map(db_conn)
    _trim_cik(db_conn)

    logger.info("*** Ended scrubbing data")
