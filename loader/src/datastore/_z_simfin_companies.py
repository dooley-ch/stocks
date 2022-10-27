# *******************************************************************************************
#  File:  _z_simfin_companies.py
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

__all__ = ['zSimFinCompanies_insert', 'zSimFinCompanies_get_all', 'zSimFinCompanies_get_by_ticker']

import related
import pymysql
from .. model import zSimFinCompaniesRecord


def zSimFinCompanies_insert(record: zSimFinCompaniesRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO z_simfin_companies(ticker, company, simfin_id, industry_id) VALUES (%s, %s, %s, %s);",
            (record.ticker, record.company, record.simfin_id, record.industry_id))
        return cursor.lastrowid


def zSimFinCompanies_get_all(db_conn: pymysql.Connection) -> list[zSimFinCompaniesRecord] | None:
    """
    This function returns all record from the table
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, company, simfin_id, industry_id FROM z_simfin_companies;")
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zSimFinCompaniesRecord, row)
                records.append(record)
            return records


def zSimFinCompanies_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zSimFinCompaniesRecord | None:
    """
    This function returns all record from the table
    :param ticker: The ticker of the company to load
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, company, simfin_id, industry_id 
                            FROM z_simfin_companies WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zSimFinCompaniesRecord, row)
            return record
