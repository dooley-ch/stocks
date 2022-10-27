# *******************************************************************************************
#  File:  _income.py
#
#  Created: 25-09-2022
#
#  History:
#  25-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['income_insert', 'income_update', 'income_delete', 'income_get', 'income_get_audit_records',
           'income_get_audit_records_by_record']

import loguru
import related
import pymysql
from .. import model
from ._errors import DuplicateKeyError


def income_insert(record: model.Income, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        try:
            cursor.execute("""INSERT INTO income(fiscal_year, restated, revenue,  gross_profit, depreciation, 
                                    interest_expense, pretax_income, tax, net_income, net_income_core, 
                                    bnk_operating_income, bnk_provision_for_loan_losses, ins_operating_income, 
                                    ins_total_claims, company_id)  
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                           (record.fiscal_year, record.restated, str(record.revenue), str(record.gross_profit),
                            str(record.depreciation), str(record.interest_expense), str(record.pretax_income),
                            str(record.tax), str(record.net_income), str(record.net_income_core),
                            str(record.bnk_operating_income), str(record.bnk_provision_for_loan_losses),
                            str(record.ins_operating_income), str(record.ins_total_claims), record.company_id))
        except pymysql.err.IntegrityError as e:
            err_no = e.args[0]
            err_msg = e.args[1]

            if err_no == 1062:
                raise DuplicateKeyError(err_msg)
            else:
                loguru.logger.error(f"Failed to insert income record: {record.company_id}, error: {err_msg}")
            raise

        return cursor.lastrowid


def income_update(record: model.Income, db_conn: pymysql.Connection) -> bool:
    """
    This function updates a record in the database_old
    :param record: the record to update
    :param db_conn: the database_old connection to use
    :return: true if the update succeeds, otherwise false
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE income SET fiscal_year = %s, restated = %s, revenue = %s, gross_profit = %s, 
                            depreciation = %s, interest_expense = %s, pretax_income = %s, tax = %s, net_income = %s, 
                            net_income_core = %s, bnk_operating_income = %s, bnk_provision_for_loan_losses = %s, 
                            ins_operating_income = %s, ins_total_claims = %s, company_id = %s, 
                            lock_version = lock_version + 1,  updated_at = CURRENT_TIMESTAMP 
                          WHERE (id = %s) AND (lock_version = %s);""",
                       (record.fiscal_year, record.restated, str(record.revenue), str(record.gross_profit),
                        str(record.depreciation), str(record.interest_expense), str(record.pretax_income),
                        str(record.tax), str(record.net_income), str(record.net_income_core),
                        str(record.bnk_operating_income), str(record.bnk_provision_for_loan_losses),
                        str(record.ins_operating_income), str(record.ins_total_claims), record.company_id,
                        record.id, record.lock_version))
        return cursor.rowcount == 1


def income_delete(record_id: int, lock_version: int, db_conn: pymysql.Connection) -> int | None:
    """
    This function deletes records based on the provided parameters
    :param record_id: the id of the record to delete
    :param lock_version: the version flag of the record to delete
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM income WHERE (id = %s) AND (lock_version = %s);", (record_id, lock_version))
        return cursor.rowcount == 1


def income_get(record_id: int, db_conn: pymysql.Connection) -> model.Income | None:
    """
    This function returns an Income record for the given parameters, if one exists
    :param record_id: the id of the record to load
    :param db_conn: the database_old connection to use
    :return: the PerShare record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, fiscal_year, restated, revenue, gross_profit, depreciation, interest_expense, 
                                pretax_income, tax, net_income, net_income_core, bnk_operating_income, 
                                bnk_provision_for_loan_losses, ins_operating_income, ins_total_claims, company_id, 
                                lock_version, created_at, updated_at 
                          FROM income WHERE (id = %s)""", (record_id,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(model.Income, data)
            return record


def income_get_audit_records(db_conn: pymysql.Connection) -> list[model.XxxIncome] | None:
    """
    This function returns all the audit records for the table
    :param db_conn: the database_old connection to use
    :return: the PerShare record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, logged_at, audit_action, record_id, fiscal_year, restated, revenue, gross_profit, 
                                depreciation, interest_expense, pretax_income, tax, net_income, net_income_core, 
                                bnk_operating_income, bnk_provision_for_loan_losses, ins_operating_income, 
                                ins_total_claims, company_id, lock_version
                          FROM xxx_income""")
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxIncome, row)
                records.append(record)

            return records


def income_get_audit_records_by_record(record_id: int, db_conn: pymysql.Connection) -> list[model.XxxIncome] | None:
    """
    This function returns all audit records for a given record
    :param record_id: The id to report on
    :param db_conn: the database_old connection to use
    :return: list of audit records, if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, logged_at, audit_action, record_id, fiscal_year, restated, revenue, gross_profit, 
                                depreciation, interest_expense, pretax_income, tax, net_income, net_income_core, 
                                bnk_operating_income, bnk_provision_for_loan_losses, ins_operating_income, 
                                ins_total_claims, company_id, lock_version
                          FROM xxx_income WHERE (record_id = %s)""", record_id)
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxIncome, row)
                records.append(record)

            return records
