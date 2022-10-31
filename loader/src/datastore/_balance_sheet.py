# *******************************************************************************************
#  File:  _balance_sheet.py
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

__all__ = ['balance_sheet_insert', 'balance_sheet_update', 'balance_sheet_delete', 'balance_sheet_get',
           'balance_sheet_get_audit_records', 'balance_sheet_get_audit_records_by_record']

import loguru
import related
import pymysql
from .. import model
from . _errors import DuplicateKeyError


def balance_sheet_insert(record: model.BalanceSheet, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        try:
            cursor.execute("""INSERT INTO balance_sheet(year, fiscal_year, restated, shares_basic, shares_diluted,
                                cash, accounts_receivable, inventories, current_assets, total_assets, 
                                accounts_payable, current_liabilities, long_term_debt, share_capital, total_capital, 
                                capital_expenditure, cashflow, bnk_inter_bank_assets, bnk_net_loans, bnk_total_deposits, 
                                ins_total_investments, ins_insurance_reserves, ins_policyholders_equity, company_id)
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                        %s, %s, %s, %s, %s);""",
                           (record.year, record.fiscal_year, record.restated, record.shares_basic,
                            record.shares_diluted, str(record.cash), str(record.accounts_receivable),
                            str(record.inventories), str(record.current_assets), str(record.total_assets),
                            str(record.accounts_payable), str(record.current_liabilities), str(record.long_term_debt),
                            str(record.share_capital), str(record.total_capital), str(record.capital_expenditure),
                            str(record.cashflow), str(record.bnk_inter_bank_assets), str(record.bnk_net_loans),
                            str(record.bnk_total_deposits), str(record.ins_total_investments),
                            str(record.ins_insurance_reserves), str(record.ins_policyholders_equity), record.company_id))
        except pymysql.err.IntegrityError as e:
            err_no = e.args[0]
            err_msg = e.args[1]

            if err_no == 1062:
                raise DuplicateKeyError(err_msg)
            else:
                loguru.logger.error(f"Failed to insert balance_sheet record: {record.company_id}, error: {err_msg}")
            raise

        return cursor.lastrowid


def balance_sheet_update(record: model.BalanceSheet, db_conn: pymysql.Connection) -> bool | None:
    """
    This function updates a record in the database_old
    :param record: the record to update
    :param db_conn: the database_old connection to use
    :return: true if the update succeeds, otherwise false
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE balance_sheet SET fiscal_year = %s, restated = %s, shares_basic = %s, 
                            shares_diluted = %s, cash = %s, accounts_receivable = %s, inventories = %s, 
                            current_assets = %s, total_assets = %s, accounts_payable = %s, current_liabilities = %s, 
                            long_term_debt = %s, share_capital = %s, total_capital = %s, capital_expenditure = %s, 
                            cashflow = %s, bnk_inter_bank_assets = %s, bnk_net_loans = %s, bnk_total_deposits = %s, 
                            ins_total_investments = %s, ins_insurance_reserves = %s, 
                            ins_policyholders_equity = %s, company_id = %s, lock_version = lock_version + 1, 
                            updated_at = CURRENT_TIMESTAMP 
                            WHERE (id = %s) AND (lock_version = %s);""",
                       (record.fiscal_year, record.restated, record.shares_basic, record.shares_diluted,
                        str(record.cash), str(record.accounts_receivable), str(record.inventories),
                        str(record.current_assets), str(record.total_assets), str(record.accounts_payable),
                        str(record.current_liabilities), str(record.long_term_debt), str(record.share_capital),
                        str(record.total_capital), str(record.capital_expenditure), str(record.cashflow),
                        str(record.bnk_inter_bank_assets), str(record.bnk_net_loans), str(record.bnk_total_deposits),
                        str(record.ins_total_investments), str(record.ins_insurance_reserves),
                        str(record.ins_policyholders_equity), record.company_id, record.id, record.lock_version))

        return cursor.rowcount == 1


def balance_sheet_delete(record_id: int, lock_version: int, db_conn: pymysql.Connection) -> int | None:
    """
    This function deletes records based on the provided parameters
    :param record_id: the id of the record to delete
    :param lock_version: the version flag of the record to delete
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM balance_sheet WHERE (id = %s) AND (lock_version = %s);", (record_id, lock_version))
        return cursor.rowcount == 1


def balance_sheet_get(record_id: int, db_conn: pymysql.Connection) -> model.BalanceSheet | None:
    """
    This function returns a PerShare record for the given parameters, if one exists
    :param record_id: the id of the record to load
    :param db_conn: the database_old connection to use
    :return: the PerShare record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, fiscal_year, restated, shares_basic, shares_diluted, cash, 
                            accounts_receivable, inventories, current_assets, total_assets, accounts_payable, 
                            current_liabilities, long_term_debt, share_capital, total_capital, capital_expenditure, 
                            cashflow, bnk_inter_bank_assets, bnk_net_loans, bnk_total_deposits, ins_total_investments, 
                            ins_insurance_reserves, ins_policyholders_equity, company_id, lock_version, created_at, 
                            updated_at FROM balance_sheet WHERE (id = %s)""", (record_id,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(model.BalanceSheet, data)
            return record


def balance_sheet_get_audit_records(db_conn: pymysql.Connection) -> list[model.XxxBalanceSheet] | None:
    """
    This function returns all the audit records for the table
    :param db_conn: the database_old connection to use
    :return: the PerShare record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, logged_at, audit_action, record_id, fiscal_year, restated, shares_basic, 
                                shares_diluted, cash, accounts_receivable, inventories, current_assets, total_assets, 
                                accounts_payable, current_liabilities, long_term_debt, share_capital, total_capital, 
                                capital_expenditure, cashflow, bnk_inter_bank_assets, bnk_net_loans, bnk_total_deposits, 
                                ins_total_investments, ins_insurance_reserves, ins_policyholders_equity, company_id, 
                                lock_version
                        FROM xxx_balance_sheet""")
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxBalanceSheet, row)
                records.append(record)

            return records


def balance_sheet_get_audit_records_by_record(record_id: int, db_conn: pymysql.Connection) -> list[model.XxxBalanceSheet] | None:
    """
    This function returns all audit records for a given record
    :param record_id: The id to report on
    :param db_conn: the database_old connection to use
    :return: list of audit records, if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, logged_at, audit_action, record_id, fiscal_year, restated, shares_basic, 
                                shares_diluted, cash, accounts_receivable, inventories, current_assets, total_assets, 
                                accounts_payable, current_liabilities, long_term_debt, share_capital, total_capital, 
                                capital_expenditure, cashflow, bnk_inter_bank_assets, bnk_net_loans, bnk_total_deposits, 
                                ins_total_investments, ins_insurance_reserves, ins_policyholders_equity, company_id, 
                                lock_version
                          FROM xxx_balance_sheet WHERE (record_id = %s)""", record_id)
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxBalanceSheet, row)
                records.append(record)

            return records
