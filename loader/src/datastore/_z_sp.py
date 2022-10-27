# *******************************************************************************************
#  File:  _z_sp.py
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

__all__ = ['zSP100_insert', 'zSP100_get_all', 'zSP600_insert', 'zSP600_get_all', 'zSP400_insert', 'zSP400_get_all',
           'zSP500_insert', 'zSP500_get_all']

import related
import pymysql
from .. model import zSp100Record, zSp600Record, zSp400Record, zSp500Record


def zSP100_insert(record: zSp100Record, db_conn: pymysql.Connection) -> int:
    """
    This function inserts a record in the table
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the new record id
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO z_sp_100 (ticker, company, industry) VALUES (%s, %s, %s);",
                       (record.ticker, record.company, record.industry))
        return cursor.lastrowid


def zSP100_get_all(db_conn: pymysql.Connection) -> list[zSp100Record] | None:
    """
    This function returns all the records in the table
    :param db_conn: the database_old connection to use
    :return: list of records from the table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT * FROM z_sp_100;")

        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zSp100Record, row)
                records.append(record)
            return records


def zSP600_insert(record: zSp600Record, db_conn: pymysql.Connection) -> int:
    """
    This function inserts a record in the table
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the new record id
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO z_sp_600 (ticker, company, industry) VALUES (%s, %s, %s);",
                       (record.ticker, record.company, record.industry))
        return cursor.lastrowid


def zSP600_get_all(db_conn: pymysql.Connection) -> list[zSp600Record] | None:
    """
    This function returns all the records in the table
    :param db_conn: the database_old connection to use
    :return: list of records from the table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, company, industry FROM z_sp_600;")

        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zSp600Record, row)
                records.append(record)
            return records


def zSP400_insert(record: zSp400Record, db_conn: pymysql.Connection) -> int:
    """
    This function inserts a record in the table
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the new record id
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO z_sp_400 (ticker, company, industry) VALUES (%s, %s, %s);",
                       (record.ticker, record.company, record.industry))
        return cursor.lastrowid


def zSP400_get_all(db_conn: pymysql.Connection) -> list[zSp400Record] | None:
    """
    This function returns all the records in the table
    :param db_conn: the database_old connection to use
    :return: list of records from the table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, company, industry FROM z_sp_400;")

        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zSp400Record, row)
                records.append(record)
            return records


def zSP500_insert(record: zSp500Record, db_conn: pymysql.Connection) -> int:
    """
    This function inserts a record in the table
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the new record id
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO z_sp_500 (ticker, company, industry) VALUES (%s, %s, %s);",
                       (record.ticker, record.company, record.industry))
        return cursor.lastrowid


def zSP500_get_all(db_conn: pymysql.Connection) -> list[zSp500Record] | None:
    """
    This function returns all the records in the table
    :param db_conn: the database_old connection to use
    :return: list of records from the table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, ticker, company, industry FROM z_sp_500;")

        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zSp500Record, row)
                records.append(record)
            return records
