# *******************************************************************************************
#  File:  _z_cashflow.py
#
#  Created: 29-09-2022
#
#  History:
#  29-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['zCashflowInsuranceQuarter_insert', 'zCashflowInsuranceQuarter_get_by_ticker',
           'zCashflowInsuranceAnnual_insert', 'zCashflowInsuranceAnnual_get_by_ticker',
           'zCashflowBankQuarter_insert', 'zCashflowBankQuarter_get_by_ticker',
           'zCashflowBankAnnual_insert', 'zCashflowBankAnnual_get_by_ticker',
           'zCashflowGeneralQuarter_insert', 'zCashflowGeneralQuarter_get_by_ticker',
           'zCashflowGeneralAnnual_insert', 'zCashflowGeneralAnnual_get_by_ticker']

import related
import pymysql
from .. model import zCashflowBankAnnualRecord, zCashflowBankQuarterRecord, zCashflowInsuranceAnnualRecord, \
    zCashflowInsuranceQuarterRecord, zCashflowGeneralAnnualRecord, zCashflowGeneralQuarterRecord


def zCashflowInsuranceQuarter_insert(record: zCashflowInsuranceQuarterRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_cashflow_insurance_quarter (ticker, simfin_id, currency, fiscal_year, 
                                fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                net_income_starting_line, depreciation_amortization, non_cash_items, 
                                net_cash_from_operating_activities, change_in_fixed_Assets_intangibles, 
                                net_change_in_investments, net_cash_from_investing_activities, dividends_paid, 
                                cash_from_repayment_of_debt, cash_from_repurchase_of_equity, 
                                net_cash_from_financing_activities, effect_of_foreign_exchange_rates, net_change_in_cash) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.net_income_starting_line, record.depreciation_amortization,
                        record.non_cash_items, record.net_cash_from_operating_activities,
                        record.change_in_fixed_Assets_intangibles, record.net_change_in_investments,
                        record.net_cash_from_investing_activities, record.dividends_paid,
                        record.cash_from_repayment_of_debt, record.cash_from_repurchase_of_equity,
                        record.net_cash_from_investing_activities, record.effect_of_foreign_exchange_rates,
                        record.net_change_in_cash))
        return cursor.lastrowid


def zCashflowInsuranceQuarter_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zCashflowInsuranceQuarterRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                                restated_date, shares_basic, shares_diluted, net_income_starting_line, 
                                depreciation_amortization, non_cash_items, net_cash_from_operating_activities, 
                                change_in_fixed_Assets_intangibles, net_change_in_investments, 
                                net_cash_from_investing_activities, dividends_paid, cash_from_repayment_of_debt, 
                                cash_from_repurchase_of_equity, net_cash_from_financing_activities, 
                                effect_of_foreign_exchange_rates, net_change_in_cash  
                            FROM z_cashflow_insurance_quarter WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zCashflowInsuranceQuarterRecord, row)
            return record


def zCashflowInsuranceAnnual_insert(record: zCashflowInsuranceAnnualRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_cashflow_insurance_annual (ticker, simfin_id, currency, fiscal_year, 
                                fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                net_income_starting_line, depreciation_amortization, non_cash_items, 
                                net_cash_from_operating_activities, change_in_fixed_Assets_intangibles, 
                                net_change_in_investments, net_cash_from_investing_activities, dividends_paid, 
                                cash_from_repayment_of_debt, cash_from_repurchase_of_equity, 
                                net_cash_from_financing_activities, effect_of_foreign_exchange_rates, net_change_in_cash) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.net_income_starting_line, record.depreciation_amortization,
                        record.non_cash_items, record.net_cash_from_operating_activities,
                        record.change_in_fixed_Assets_intangibles, record.net_change_in_investments,
                        record.net_cash_from_investing_activities, record.dividends_paid,
                        record.cash_from_repayment_of_debt, record.cash_from_repurchase_of_equity,
                        record.net_cash_from_investing_activities, record.effect_of_foreign_exchange_rates,
                        record.net_change_in_cash))
        return cursor.lastrowid


def zCashflowInsuranceAnnual_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zCashflowInsuranceAnnualRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                                restated_date, shares_basic, shares_diluted, net_income_starting_line, 
                                depreciation_amortization, non_cash_items, net_cash_from_operating_activities, 
                                change_in_fixed_Assets_intangibles, net_change_in_investments, 
                                net_cash_from_investing_activities, dividends_paid, cash_from_repayment_of_debt, 
                                cash_from_repurchase_of_equity, net_cash_from_financing_activities, 
                                effect_of_foreign_exchange_rates, net_change_in_cash  
                            FROM z_cashflow_insurance_annual WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zCashflowInsuranceAnnualRecord, row)
            return record


def zCashflowBankQuarter_insert(record: zCashflowBankQuarterRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_cashflow_bank_quarter (ticker, simfin_id, currency, fiscal_year, fiscal_period, 
                                report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                net_income_starting_line, depreciation_amortization, provision_for_loan_losses, 
                                non_cash_items, change_in_working_capital, net_cash_from_operating_activities, 
                                change_in_fixed_assets_intangibles, net_change_in_loans_interbank, 
                                net_cash_from_acquisitions_divestitures, net_cash_from_investing_activities, 
                                dividends_paid, cash_from_repayment_of_debt, cash_from_repurchase_of_equity, 
                                net_cash_from_financing_activities, effect_of_foreign_exchange_rates, net_change_in_cash) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.net_income_starting_line, record.depreciation_amortization,
                        record.provision_for_loan_losses, record.non_cash_items, record.change_in_working_capital,
                        record.net_cash_from_operating_activities, record.change_in_fixed_assets_intangibles,
                        record.net_change_in_loans_interbank, record.net_cash_from_acquisitions_divestitures,
                        record.net_cash_from_investing_activities, record.dividends_paid,
                        record.cash_from_repayment_of_debt, record.cash_from_repurchase_of_equity,
                        record.net_cash_from_financing_activities, record.effect_of_foreign_exchange_rates,
                        record.net_change_in_cash))
        return cursor.lastrowid


def zCashflowBankQuarter_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zCashflowBankQuarterRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                                restated_date, shares_basic, shares_diluted, net_income_starting_line, 
                                depreciation_amortization, provision_for_loan_losses, non_cash_items, 
                                change_in_working_capital, net_cash_from_operating_activities, 
                                change_in_fixed_assets_intangibles, net_change_in_loans_interbank, 
                                net_cash_from_acquisitions_divestitures, net_cash_from_investing_activities, 
                                dividends_paid, cash_from_repayment_of_debt, cash_from_repurchase_of_equity, 
                                net_cash_from_financing_activities, effect_of_foreign_exchange_rates, 
                                net_change_in_cash
                            FROM z_cashflow_bank_quarter WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zCashflowBankQuarterRecord, row)
            return record


def zCashflowBankAnnual_insert(record: zCashflowBankAnnualRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_cashflow_bank_annual (ticker, simfin_id, currency, fiscal_year, fiscal_period, 
                                report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                net_income_starting_line, depreciation_amortization, provision_for_loan_losses, 
                                non_cash_items, change_in_working_capital, net_cash_from_operating_activities, 
                                change_in_fixed_assets_intangibles, net_change_in_loans_interbank, 
                                net_cash_from_acquisitions_divestitures, net_cash_from_investing_activities, 
                                dividends_paid, cash_from_repayment_of_debt, cash_from_repurchase_of_equity, 
                                net_cash_from_financing_activities, effect_of_foreign_exchange_rates, net_change_in_cash) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.net_income_starting_line, record.depreciation_amortization,
                        record.provision_for_loan_losses, record.non_cash_items, record.change_in_working_capital,
                        record.net_cash_from_operating_activities, record.change_in_fixed_assets_intangibles,
                        record.net_change_in_loans_interbank, record.net_cash_from_acquisitions_divestitures,
                        record.net_cash_from_investing_activities, record.dividends_paid,
                        record.cash_from_repayment_of_debt, record.cash_from_repurchase_of_equity,
                        record.net_cash_from_financing_activities, record.effect_of_foreign_exchange_rates,
                        record.net_change_in_cash))
        return cursor.lastrowid


def zCashflowBankAnnual_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zCashflowBankAnnualRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                                restated_date, shares_basic, shares_diluted, net_income_starting_line, 
                                depreciation_amortization, provision_for_loan_losses, non_cash_items, 
                                change_in_working_capital, net_cash_from_operating_activities, 
                                change_in_fixed_assets_intangibles, net_change_in_loans_interbank, 
                                net_cash_from_acquisitions_divestitures, net_cash_from_investing_activities, 
                                dividends_paid, cash_from_repayment_of_debt, cash_from_repurchase_of_equity, 
                                net_cash_from_financing_activities, effect_of_foreign_exchange_rates, 
                                net_change_in_cash
                            FROM z_cashflow_bank_annual WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zCashflowBankAnnualRecord, row)
            return record


def zCashflowGeneralQuarter_insert(record: zCashflowGeneralQuarterRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_cashflow_general_quarter (ticker, simfin_id, currency, fiscal_year, fiscal_period, 
                            report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                            net_income_starting_line, depreciation_amortization, non_cash_items, 
                            change_in_working_capital, change_in_accounts_receivable, change_in_inventories, 
                            change_in_accounts_payable, change_in_other, net_cash_from_operating_Activities, 
                            change_in_fixed_assets_intangibles, net_change_in_long_term_investment, 
                            net_cash_from_acquisitions_divestitures, net_cash_from_investing_activities, 
                            dividends_paid, cash_from_repayment_of_debt, cash_from_repurchase_of_equity, 
                            net_cash_from_financing_activities, net_change_in_cash) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.net_income_starting_line, record.depreciation_amortization,
                        record.non_cash_items, record.change_in_working_capital, record.change_in_accounts_receivable,
                        record.change_in_inventories, record.change_in_accounts_payable, record.change_in_other,
                        record.net_cash_from_operating_Activities, record.change_in_fixed_assets_intangibles,
                        record.net_change_in_long_term_investment, record.net_cash_from_acquisitions_divestitures,
                        record.net_cash_from_investing_activities, record.dividends_paid, record.cash_from_repayment_of_debt,
                        record.cash_from_repurchase_of_equity, record.net_cash_from_financing_activities,
                        record.net_change_in_cash))
        return cursor.lastrowid


def zCashflowGeneralQuarter_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zCashflowGeneralQuarterRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, 
                                publish_date, restated_date, shares_basic, shares_diluted, net_income_starting_line, 
                                depreciation_amortization, non_cash_items, change_in_working_capital, 
                                change_in_accounts_receivable, change_in_inventories, change_in_accounts_payable, 
                                change_in_other, net_cash_from_operating_Activities, change_in_fixed_assets_intangibles, 
                                net_change_in_long_term_investment, net_cash_from_acquisitions_divestitures, 
                                net_cash_from_investing_activities, dividends_paid, cash_from_repayment_of_debt, 
                                cash_from_repurchase_of_equity, net_cash_from_financing_activities, net_change_in_cash
                            FROM z_cashflow_general_quarter WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zCashflowGeneralQuarterRecord, row)
            return record


def zCashflowGeneralAnnual_insert(record: zCashflowGeneralAnnualRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_cashflow_general_annual (ticker, simfin_id, currency, fiscal_year, fiscal_period, 
                            report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                            net_income_starting_line, depreciation_amortization, non_cash_items, 
                            change_in_working_capital, change_in_accounts_receivable, change_in_inventories, 
                            change_in_accounts_payable, change_in_other, net_cash_from_operating_Activities, 
                            change_in_fixed_assets_intangibles, net_change_in_long_term_investment, 
                            net_cash_from_acquisitions_divestitures, net_cash_from_investing_activities, 
                            dividends_paid, cash_from_repayment_of_debt, cash_from_repurchase_of_equity, 
                            net_cash_from_financing_activities, net_change_in_cash) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.net_income_starting_line, record.depreciation_amortization,
                        record.non_cash_items, record.change_in_working_capital, record.change_in_accounts_receivable,
                        record.change_in_inventories, record.change_in_accounts_payable, record.change_in_other,
                        record.net_cash_from_operating_Activities, record.change_in_fixed_assets_intangibles,
                        record.net_change_in_long_term_investment, record.net_cash_from_acquisitions_divestitures,
                        record.net_cash_from_investing_activities, record.dividends_paid, record.cash_from_repayment_of_debt,
                        record.cash_from_repurchase_of_equity, record.net_cash_from_financing_activities,
                        record.net_change_in_cash))
        return cursor.lastrowid


def zCashflowGeneralAnnual_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zCashflowGeneralAnnualRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, 
                                publish_date, restated_date, shares_basic, shares_diluted, net_income_starting_line, 
                                depreciation_amortization, non_cash_items, change_in_working_capital, 
                                change_in_accounts_receivable, change_in_inventories, change_in_accounts_payable, 
                                change_in_other, net_cash_from_operating_Activities, change_in_fixed_assets_intangibles, 
                                net_change_in_long_term_investment, net_cash_from_acquisitions_divestitures, 
                                net_cash_from_investing_activities, dividends_paid, cash_from_repayment_of_debt, 
                                cash_from_repurchase_of_equity, net_cash_from_financing_activities, net_change_in_cash
                            FROM z_cashflow_general_annual WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zCashflowGeneralAnnualRecord, row)
            return record
