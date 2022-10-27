# *******************************************************************************************
#  File:  _company.py
#
#  Created: 24-09-2022
#
#  History:
#  24-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['company_insert', 'company_update', 'company_delete', 'company_get', 'company_get_by_ticker',
           'company_get_by_name', 'company_get_tickers', 'company_get_financial_tickers']

from collections import namedtuple
import related
import pymysql
from .. import model


def company_insert(record: model.Company, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO company(ticker, name, currency, description, stock_exchange, cik_number, figi_code, 
                                simfin_number, is_sp100, is_sp600, is_sp400, is_sp500, company_type_id, industry_id, 
                                is_active, has_financials) 
                          VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s);""",
                       (
                           record.ticker, record.name, record.currency, record.description, record.stock_exchange,
                           record.cik_number, record.figi_code, record.simfin_number, record.is_sp100, record.is_sp600,
                           record.is_sp400, record.is_sp500, int(record.company_type_id), record.industry_id,
                           record.is_active, record.has_financials))
        return cursor.lastrowid


def company_update(record: model.Company, db_conn: pymysql.Connection) -> bool:
    """
    This function updates a company record, if one exists
    :param record: the record to update
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE company SET ticker = %s, name = %s, currency = %s, description = %s, stock_exchange = %s,
                            cik_number = %s, figi_code = %s, simfin_number = %s, is_sp100 = %s,  is_sp600 = %s,
                            is_sp400 = %s, is_sp500 = %s, company_type_id = %s, industry_id = %s, is_active = %s,
                            has_financials = %s, lock_version = lock_version + 1,  updated_at = CURRENT_TIMESTAMP 
                            WHERE (id = %s) AND (lock_version = %s);""",
                       (record.ticker, record.name, record.currency, record.description, record.stock_exchange,
                        record.cik_number, record.figi_code, record.simfin_number, record.is_sp100, record.is_sp600,
                        record.is_sp400, record.is_sp500, int(record.company_type_id), record.industry_id,
                        record.is_active, record.has_financials, record.id, record.lock_version))
        return cursor.rowcount == 1


def company_delete(record_id: int, lock_version: int, db_conn: pymysql.Connection) -> bool:
    """
    This function deletes records based on the provided parameters
    :param record_id: the id of the record to delete
    :param lock_version: the version flag of the record to delete
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM company WHERE (id = %s) AND (lock_version = %s);", (record_id, lock_version))
        return cursor.rowcount == 1


def company_get(record_id: int, db_conn: pymysql.Connection) -> model.Company | None:
    """
    This function returns a Company record for the given parameters, if one exists
    :param record_id: the id of the record to load
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
                            IF(has_financials = 1, 'True', 'False') AS  has_financials, lock_version, created_at, 
                            updated_at FROM company WHERE (id = %s)""", (record_id,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(model.Company, data)
            return record


def company_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> model.Company | None:
    """
    This function returns a Company record for the given parameters, if one exists
    :param ticker: the ticker of the record to load
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
                            IF(has_financials = 1, 'True', 'False') AS  has_financials, lock_version, created_at, 
                            updated_at FROM company WHERE (ticker = %s)""", (ticker,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(model.Company, data)
            return record


def company_get_by_name(name: str, db_conn: pymysql.Connection) -> list[model.Company] | None:
    """
    This function returns a Company record for the given parameters, if one exists
    :param name: the name to filter by
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
                            IF(has_financials = 1, 'True', 'False') AS  has_financials, lock_version, created_at, 
                            updated_at FROM company WHERE (name LIKE %s)""", (name,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(model.Company, row)
                records.append(record)
            return records


def company_get_tickers(db_conn: pymysql.Connection) -> list[(str, str, str)] | None:
    """
    This function returns summary records for each company
    """
    CompanyRecord = namedtuple('CompanyRecord', ['id', 'ticker', 'name'])

    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, name FROM company;")
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                # noinspection PyTypeChecker
                record = CompanyRecord(row['id'], row['ticker'], row['name'])
                records.append(record)
            return records


def company_get_financial_tickers(db_conn: pymysql.Connection) -> list[(str, str, str)] | None:
    """
    This function returns summary records for each company
    """
    CompanyRecord = namedtuple('CompanyRecord', ['id', 'ticker', 'name', 'company_type', 'has_financials'])

    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, name, company_type_id, 
                            IF(has_financials = 1, 'True', 'False') AS has_financials FROM company ORDER BY ticker;""")
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                # noinspection PyTypeChecker
                record = CompanyRecord(row['id'], row['ticker'], row['name'],
                                       model.CompanyType(row['company_type_id']), bool(row['has_financials']))
                records.append(record)
            return records
