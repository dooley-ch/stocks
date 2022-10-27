# *******************************************************************************************
#  File:  _zs_company.py
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

__all__ = ['zsCompanyRecord_insert', 'zsCompanyRecord_get', 'zsCompanyRecord_get_all', 'zsCompanyRecord_get_tickers']

from collections import namedtuple
import related
import pymysql
from .. model import zsCompanyRecord

def zsCompanyRecord_insert(record: zsCompanyRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO zs_company(ticker, name, currency, description, stock_exchange, cik_number, figi_code, 
                                simfin_number, is_sp100, is_sp600, is_sp400, is_sp500, company_type_id, industry_id, 
                                is_active, has_financials) 
                          VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s);""",
                       (
                           record.ticker, record.name, record.currency, record.description, record.stock_exchange,
                           record.cik_number, record.figi_code, record.simfin_number, record.is_sp100, record.is_sp600,
                           record.is_sp400, record.is_sp500, int(record.company_type_id), record.industry_id, record.is_active,
                           record.has_financials))
        return cursor.lastrowid


def zsCompanyRecord_get(ticker: str, db_conn: pymysql.Connection) -> zsCompanyRecord | None:
    """
    This function returns a zsCompanyRecord record for the given parameters, if one exists
    :param ticker: the ticker of the company to load
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, name, currency, description, IFNULL(stock_exchange,"") AS stock_exchange, 
                            cik_number, figi_code, simfin_number,  IF(is_sp100 = 1, 'True', 'False') AS is_sp100, 
                            IF(is_sp600 = 1, 'True', 'False') AS is_sp600, IF(is_sp400 = 1, 'True', 'False') AS 
                            is_sp400,  IF(is_sp500 = 1, 'True', 'False') AS is_sp500, company_type_id, industry_id, 
                            IF(is_active = 1, 'True', 'False') AS is_active, 
                            IF(has_financials = 1, 'True', 'False') AS  has_financials 
                            FROM zs_company WHERE (ticker = %s)""", (ticker,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(zsCompanyRecord, data)
            return record


def zsCompanyRecord_get_all(db_conn: pymysql.Connection) -> list[zsCompanyRecord] | None:
    """
    This function returns all record from the table
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, name, currency, description, stock_exchange, cik_number, figi_code, 
                            simfin_number,  IF(is_sp100 = 1, 'True', 'False') AS is_sp100, 
                            IF(is_sp600 = 1, 'True', 'False') AS is_sp600, IF(is_sp400 = 1, 'True', 'False') AS 
                            is_sp400, 
                            IF(is_sp500 = 1, 'True', 'False') AS is_sp500, company_type_id, industry_id, 
                            IF(is_active = 1, 'True', 'False') AS is_active, 
                            IF(has_financials = 1, 'True', 'False') AS  has_financials FROM zs_company;""")
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zsCompanyRecord, row)
                records.append(record)
            return records


def zsCompanyRecord_get_tickers(db_conn: pymysql.Connection) -> list[(str, str, str)] | None:
    """
    This function returns summary records for each company
    """
    Company = namedtuple('Company', ['id', 'ticker', 'name'])

    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, name  FROM zs_company;")
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                # noinspection PyTypeChecker
                record = Company(row['id'], row['ticker'], row['name'])
                records.append(record)
            return records
