# *******************************************************************************************
#  File:  _quarter.py
#
#  Created: 25-10-2022
#
#  History:
#  25-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['quarter_insert', 'quarter_update', 'quarter_delete', 'quarter_get', 'quarter_get_audit_records',
           'quarter_get_audit_records_by_record']

import loguru
import related
import pymysql
from .. import model
from ._errors import DuplicateKeyError


def quarter_insert(record: model.Quarter, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        try:
            cursor.execute("""INSERT INTO quarter(year, quarter, fiscal_year, restated, shares_basic, shares_diluted, 
                                revenue, pretax_income, tax, net_income, net_income_core, dividends_paid, 
                                net_change_in_cash, company_id)  
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                           (record.year, record.quarter, record.fiscal_year, record.restated, str(record.shares_basic),
                            str(record.shares_diluted), str(record.revenue), str(record.pretax_income),
                            str(record.tax), str(record.net_income), str(record.net_income_core),
                            str(record.dividends_paid), str(record.net_change_in_cash), record.company_id))
        except pymysql.err.IntegrityError as e:
            err_no = e.args[0]
            err_msg = e.args[1]

            if err_no == 1062:
                raise DuplicateKeyError(err_msg)
            else:
                loguru.logger.error(f"Failed to insert income record: {record.company_id}, error: {err_msg}")
            raise

        return cursor.lastrowid


def quarter_update(record: model.Quarter, db_conn: pymysql.Connection) -> bool:
    """
    This function updates a record in the database_old
    :param record: the record to update
    :param db_conn: the database_old connection to use
    :return: true if the update succeeds, otherwise false
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE quarter SET year = %s, quarter = %s, fiscal_year = %s, restated = %s, shares_basic = %s, 
                            shares_diluted = %s, revenue = %s, pretax_income = %s, tax = %s, net_income = %s, 
                            net_income_core = %s, dividends_paid = %s, net_change_in_cash = %s, company_id = %s, 
                            lock_version = lock_version + 1,  updated_at = CURRENT_TIMESTAMP 
                          WHERE (id = %s) AND (lock_version = %s);""",
                       (record.year, record.quarter, record.fiscal_year, record.restated, str(record.shares_basic),
                        str(record.shares_diluted), str(record.revenue), str(record.pretax_income), str(record.tax),
                        str(record.net_income), str(record.net_income_core), str(record.dividends_paid),
                        str(record.net_change_in_cash), record.company_id, record.id, record.lock_version))
        return cursor.rowcount == 1


def quarter_delete(record_id: int, lock_version: int, db_conn: pymysql.Connection) -> int | None:
    """
    This function deletes records based on the provided parameters
    :param record_id: the id of the record to delete
    :param lock_version: the version flag of the record to delete
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM quarter WHERE (id = %s) AND (lock_version = %s);", (record_id, lock_version))
        return cursor.rowcount == 1


def quarter_get(record_id: int, db_conn: pymysql.Connection) -> model.Quarter | None:
    """
    This function returns a quarter record for the given parameters, if one exists
    :param record_id: the id of the record to load
    :param db_conn: the database_old connection to use
    :return: the PerShare record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, year, quarter, fiscal_year, restated, shares_basic, shares_diluted, revenue, 
                            pretax_income, tax, net_income, net_income_core, dividends_paid, net_change_in_cash, 
                            company_id, lock_version, created_at, updated_at 
                          FROM quarter WHERE (id = %s)""", (record_id,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(model.Quarter, data)
            return record


def quarter_get_audit_records(db_conn: pymysql.Connection) -> list[model.XxxQuarter] | None:
    """
    This function returns all the audit records for the table
    :param db_conn: the database_old connection to use
    :return: the PerShare record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, logged_at, audit_action, record_id, year, quarter, fiscal_year, restated, 
                            shares_basic, shares_diluted, revenue, pretax_income, tax, net_income, net_income_core, 
                            dividends_paid, net_change_in_cash, company_id, lock_version
                          FROM xxx_quarter""")
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxQuarter, row)
                records.append(record)

            return records


def quarter_get_audit_records_by_record(record_id: int, db_conn: pymysql.Connection) -> list[model.XxxQuarter] | None:
    """
    This function returns all audit records for a given record
    :param record_id: The id to report on
    :param db_conn: the database_old connection to use
    :return: list of audit records, if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, logged_at, audit_action, record_id, year, quarter, fiscal_year, restated, 
                            shares_basic, shares_diluted, revenue, pretax_income, tax, net_income, net_income_core, 
                            dividends_paid, net_change_in_cash, company_id, lock_version
                          FROM xxx_quarter WHERE (record_id = %s)""", record_id)
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxQuarter, row)
                records.append(record)

            return records
