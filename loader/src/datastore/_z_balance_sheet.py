# *******************************************************************************************
#  File:  _z_balance_sheet.py
#
#  Created: 01-10-2022
#
#  History:
#  01-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['zBalanceSheetInsuranceQuarter_insert', 'zBalanceSheetInsuranceQuarter_get_by_ticker',
           'zBalanceSheetInsuranceAnnual_insert', 'zBalanceSheetInsuranceAnnual_get_by_ticker',
           'zBalanceSheetBankQuarter_insert', 'zBalanceSheetBankQuarter_get_by_ticker',
           'zBalanceSheetBankAnnual_insert', 'zBalanceSheetBankAnnual_get_by_ticker',
           'zBalanceSheetGeneralQuarter_insert', 'zBalanceSheetGeneralQuarter_get_by_ticker',
           'zBalanceSheetGeneralAnnual_insert', 'zBalanceSheetGeneralAnnual_get_by_ticker']

import related
import pymysql
from .. model import zBalanceSheetBankAnnualRecord, zBalanceSheetBankQuarterRecord, \
    zBalanceSheetInsuranceQuarterRecord, zBalanceSheetInsuranceAnnualRecord, zBalanceSheetGeneralQuarterRecord, \
    zBalanceSheetGeneralAnnualRecord


def zBalanceSheetInsuranceQuarter_insert(record: zBalanceSheetInsuranceQuarterRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_balance_sheet_insurance_quarter (ticker, simfin_id, currency, fiscal_year, 
                                fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                total_investments, cash_cash_equivalents_short_term_investments, 
                                accounts_notes_receivable, property_plant_equipment_net, total_assets, 
                                insurance_reserves, short_term_debt, long_term_debt, total_liabilities, 
                                preferred_equity, policyholders_equity, share_capital_additional_paid_in_capital, 
                                treasury_stock, retained_earnings, total_equity, total_liabilities_equity) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.total_investments,
                        record.cash_cash_equivalents_short_term_investments, record.accounts_notes_receivable,
                        record.property_plant_equipment_net, record.total_assets, record.insurance_reserves,
                        record.short_term_debt, record.long_term_debt, record.total_liabilities,
                        record.preferred_equity,
                        record.policyholders_equity, record.share_capital_additional_paid_in_capital,
                        record.treasury_stock, record.retained_earnings, record.total_equity, record.total_liabilities))
        return cursor.lastrowid


def zBalanceSheetInsuranceQuarter_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zBalanceSheetInsuranceQuarterRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                            restated_date, shares_basic, shares_diluted, total_investments, 
                            cash_cash_equivalents_short_term_investments, accounts_notes_receivable, 
                            property_plant_equipment_net, total_assets, insurance_reserves, short_term_debt, 
                            long_term_debt, total_liabilities, preferred_equity, policyholders_equity, 
                            share_capital_additional_paid_in_capital, treasury_stock, retained_earnings, 
                            total_equity, total_liabilities_equity  
                            FROM z_balance_sheet_insurance_quarter WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zBalanceSheetInsuranceQuarterRecord, row)
            return record


def zBalanceSheetInsuranceAnnual_insert(record: zBalanceSheetInsuranceAnnualRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_balance_sheet_insurance_annual (ticker, simfin_id, currency, fiscal_year, 
                                fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                total_investments, cash_cash_equivalents_short_term_investments, 
                                accounts_notes_receivable, property_plant_equipment_net, total_assets, 
                                insurance_reserves, short_term_debt, long_term_debt, total_liabilities, 
                                preferred_equity, policyholders_equity, share_capital_additional_paid_in_capital, 
                                treasury_stock, retained_earnings, total_equity, total_liabilities_equity) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.total_investments,
                        record.cash_cash_equivalents_short_term_investments, record.accounts_notes_receivable,
                        record.property_plant_equipment_net, record.total_assets, record.insurance_reserves,
                        record.short_term_debt, record.long_term_debt, record.total_liabilities,
                        record.preferred_equity,
                        record.policyholders_equity, record.share_capital_additional_paid_in_capital,
                        record.treasury_stock, record.retained_earnings, record.total_equity, record.total_liabilities))
        return cursor.lastrowid


def zBalanceSheetInsuranceAnnual_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zBalanceSheetInsuranceQuarterRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, 
                            publish_date, restated_date, 
                            IF(shares_basic = '', '0', shares_basic) AS shares_basic, 
                            IF(shares_diluted = '', '0', shares_diluted) AS shares_diluted, 
                            IF(total_investments = '', 'NaN', total_investments) AS total_investments, 
                            IF(cash_cash_equivalents_short_term_investments = '', 'NaN', cash_cash_equivalents_short_term_investments) AS cash_cash_equivalents_short_term_investments, 
                            IF(accounts_notes_receivable = '', 'NaN', accounts_notes_receivable) AS accounts_notes_receivable, 
                            IF(property_plant_equipment_net = '', 'NaN', property_plant_equipment_net) AS property_plant_equipment_net, 
                            IF(total_assets = '', 'NaN', total_assets) AS total_assets, 
                            IF(insurance_reserves = '', 'NaN', insurance_reserves) AS insurance_reserves, 
                            IF(short_term_debt = '', 'NaN', short_term_debt) AS short_term_debt, 
                            IF(long_term_debt = '', 'NaN', long_term_debt) AS long_term_debt, 
                            IF(total_liabilities = '', 'NaN', total_liabilities) AS total_liabilities, 
                            IF(preferred_equity = '', 'NaN', preferred_equity) AS preferred_equity, 
                            IF(policyholders_equity = '', 'NaN', policyholders_equity) AS policyholders_equity, 
                            IF(share_capital_additional_paid_in_capital = '', 'NaN', share_capital_additional_paid_in_capital) AS share_capital_additional_paid_in_capital, 
                            IF(treasury_stock = '', 'NaN', treasury_stock) AS treasury_stock, 
                            IF(retained_earnings = '', 'NaN', retained_earnings) AS retained_earnings, 
                            IF(total_equity = '', 'NaN', total_equity) AS total_equity, 
                            IF(total_liabilities_equity = '', 'NaN', total_liabilities_equity) AS total_liabilities_equity  
                            FROM z_balance_sheet_insurance_annual WHERE (ticker = %s);""", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zBalanceSheetInsuranceAnnualRecord, row)
                records.append(record)
            return records


def zBalanceSheetBankQuarter_insert(record: zBalanceSheetBankQuarterRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_balance_sheet_bank_quarter (ticker, simfin_id, currency, fiscal_year, 
                                fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                cash_cash_equivalents_short_term_investments, interbank_Assets, 
                                short_long_term_investments, accounts_notes_receivable, net_loans, net_fixed_assets, 
                                total_assets, total_deposits, short_term_debt, long_term_debt, total_liabilities, 
                                preferred_equity, share_capital_additional_paid_in_capital, treasury_stock, 
                                retained_earnings, total_equity, total_liabilities_equity) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                         %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.cash_cash_equivalents_short_term_investments, record.interbank_Assets,
                        record.short_long_term_investments, record.accounts_notes_receivable, record.net_loans,
                        record.net_fixed_assets, record.total_assets, record.total_deposits, record.short_term_debt,
                        record.long_term_debt, record.total_liabilities, record.preferred_equity,
                        record.share_capital_additional_paid_in_capital, record.treasury_stock, record.retained_earnings,
                        record.total_equity, record.total_liabilities_equity))
        return cursor.lastrowid


def zBalanceSheetBankQuarter_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zBalanceSheetBankQuarterRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                                restated_date, shares_basic, shares_diluted, 
                                cash_cash_equivalents_short_term_investments, 
                                interbank_Assets, short_long_term_investments, accounts_notes_receivable, net_loans, 
                                net_fixed_assets, total_assets, total_deposits, short_term_debt, long_term_debt, 
                                total_liabilities, preferred_equity, share_capital_additional_paid_in_capital, 
                                treasury_stock, retained_earnings, total_equity, total_liabilities_equity  
                            FROM z_balance_sheet_bank_quarter WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zBalanceSheetBankQuarterRecord, row)
            return record


def zBalanceSheetBankAnnual_insert(record: zBalanceSheetBankAnnualRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_balance_sheet_bank_annual (ticker, simfin_id, currency, fiscal_year, 
                                fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                cash_cash_equivalents_short_term_investments, interbank_Assets, 
                                short_long_term_investments, accounts_notes_receivable, net_loans, net_fixed_assets, 
                                total_assets, total_deposits, short_term_debt, long_term_debt, total_liabilities, 
                                preferred_equity, share_capital_additional_paid_in_capital, treasury_stock, 
                                retained_earnings, total_equity, total_liabilities_equity) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                         %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.cash_cash_equivalents_short_term_investments, record.interbank_Assets,
                        record.short_long_term_investments, record.accounts_notes_receivable, record.net_loans,
                        record.net_fixed_assets, record.total_assets, record.total_deposits, record.short_term_debt,
                        record.long_term_debt, record.total_liabilities, record.preferred_equity,
                        record.share_capital_additional_paid_in_capital, record.treasury_stock, record.retained_earnings,
                        record.total_equity, record.total_liabilities_equity))
        return cursor.lastrowid


def zBalanceSheetBankAnnual_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zBalanceSheetBankAnnualRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, 
                                publish_date, restated_date, 
                                IF(shares_basic = '', '0', shares_basic) AS shares_basic, 
                                IF(shares_diluted = '', '0', shares_diluted) AS shares_diluted, 
                                IF(cash_cash_equivalents_short_term_investments = '', 'NaN', cash_cash_equivalents_short_term_investments) AS cash_cash_equivalents_short_term_investments, 
                                IF(interbank_Assets = '', 'NaN', interbank_Assets) AS interbank_Assets, 
                                IF(short_long_term_investments = '', 'NaN', short_long_term_investments) AS short_long_term_investments, 
                                IF(accounts_notes_receivable = '', 'NaN', accounts_notes_receivable) AS accounts_notes_receivable, 
                                IF(net_loans = '', 'NaN', net_loans) AS net_loans, 
                                IF(net_fixed_assets = '', 'NaN', net_fixed_assets) AS net_fixed_assets, 
                                IF(total_assets = '', 'NaN', total_assets) AS total_assets, 
                                IF(total_deposits = '', 'NaN', total_deposits) AS total_deposits, 
                                IF(short_term_debt = '', 'NaN', short_term_debt) AS short_term_debt, 
                                IF(long_term_debt = '', 'NaN', long_term_debt) AS long_term_debt, 
                                IF(total_liabilities = '', 'NaN', total_liabilities) AS total_liabilities, 
                                IF(preferred_equity = '', 'NaN', preferred_equity) AS preferred_equity, 
                                IF(share_capital_additional_paid_in_capital = '', 'NaN', share_capital_additional_paid_in_capital) AS share_capital_additional_paid_in_capital, 
                                IF(treasury_stock = '', 'NaN', treasury_stock) AS treasury_stock, 
                                IF(retained_earnings = '', 'NaN', retained_earnings) AS retained_earnings, 
                                IF(total_equity = '', 'NaN', total_equity) AS total_equity, 
                                IF(total_liabilities_equity = '', 'NaN', total_liabilities_equity) AS total_liabilities_equity  
                            FROM z_balance_sheet_bank_annual WHERE (ticker = %s);""", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zBalanceSheetBankAnnualRecord, row)
                records.append(record)

            return records


def zBalanceSheetGeneralQuarter_insert(record: zBalanceSheetGeneralQuarterRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_balance_sheet_general_quarter (ticker, simfin_id, currency, fiscal_year, 
                            fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                            cash_cash_equivalents_short_term_investments, accounts_notes_receivable, inventories, 
                            total_current_assets, property_plant_equipment_net, long_term_investments_receivables, 
                            other_long_term_assets, total_noncurrent_assets, total_assets, payables_accruals, 
                            short_term_debt, total_current_liabilities, long_term_debt, total_noncurrent_liabilities, 
                            total_liabilities, share_capital_additional_paid_in_capital, treasury_stock, 
                            retained_earnings, total_equity, total_liabilities_equity) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.cash_cash_equivalents_short_term_investments,
                        record.accounts_notes_receivable, record.inventories, record.total_current_assets,
                        record.property_plant_equipment_net, record.long_term_investments_receivables,
                        record.other_long_term_assets, record.total_noncurrent_assets, record.total_assets,
                        record.payables_accruals, record.short_term_debt, record.total_current_liabilities,
                        record.long_term_debt, record.total_noncurrent_liabilities, record.total_liabilities,
                        record.share_capital_additional_paid_in_capital, record.treasury_stock,
                        record.retained_earnings,
                        record.total_equity, record.total_liabilities_equity))
        return cursor.lastrowid


def zBalanceSheetGeneralQuarter_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> zBalanceSheetGeneralQuarterRecord | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                                restated_date, shares_basic, shares_diluted, 
                                cash_cash_equivalents_short_term_investments, 
                                accounts_notes_receivable, inventories, total_current_assets, 
                                property_plant_equipment_net, 
                                long_term_investments_receivables, other_long_term_assets, total_noncurrent_assets, 
                                total_assets, payables_accruals, short_term_debt, total_current_liabilities, 
                                long_term_debt, 
                                total_noncurrent_liabilities, total_liabilities, 
                                share_capital_additional_paid_in_capital, 
                                treasury_stock, retained_earnings, total_equity, total_liabilities_equity  
                            FROM z_balance_sheet_general_quarter WHERE (ticker = %s);""", (ticker,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zBalanceSheetGeneralQuarterRecord, row)
            return record


def zBalanceSheetGeneralAnnual_insert(record: zBalanceSheetGeneralAnnualRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_balance_sheet_general_annual (ticker, simfin_id, currency, fiscal_year, 
                            fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                            cash_cash_equivalents_short_term_investments, accounts_notes_receivable, inventories, 
                            total_current_assets, property_plant_equipment_net, long_term_investments_receivables, 
                            other_long_term_assets, total_noncurrent_assets, total_assets, payables_accruals, 
                            short_term_debt, total_current_liabilities, long_term_debt, total_noncurrent_liabilities, 
                            total_liabilities, share_capital_additional_paid_in_capital, treasury_stock, 
                            retained_earnings, total_equity, total_liabilities_equity) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.cash_cash_equivalents_short_term_investments,
                        record.accounts_notes_receivable, record.inventories, record.total_current_assets,
                        record.property_plant_equipment_net, record.long_term_investments_receivables,
                        record.other_long_term_assets, record.total_noncurrent_assets, record.total_assets,
                        record.payables_accruals, record.short_term_debt, record.total_current_liabilities,
                        record.long_term_debt, record.total_noncurrent_liabilities, record.total_liabilities,
                        record.share_capital_additional_paid_in_capital, record.treasury_stock,
                        record.retained_earnings,
                        record.total_equity, record.total_liabilities_equity))
        return cursor.lastrowid


def zBalanceSheetGeneralAnnual_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zBalanceSheetGeneralAnnualRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                                restated_date,  
                                IF(shares_basic = '', '0', shares_basic) AS shares_basic, 
                                IF(shares_diluted = '', '0', shares_diluted) AS shares_diluted, 
                                IF(cash_cash_equivalents_short_term_investments = '', 'NaN', cash_cash_equivalents_short_term_investments) AS cash_cash_equivalents_short_term_investments, 
                                IF(accounts_notes_receivable = '', 'NaN', accounts_notes_receivable) AS accounts_notes_receivable, 
                                IF(inventories = '', 'NaN', inventories) AS inventories, 
                                IF(total_current_assets = '', 'NaN', total_current_assets) AS total_current_assets, 
                                IF(property_plant_equipment_net = '', 'NaN', property_plant_equipment_net) AS property_plant_equipment_net, 
                                IF(long_term_investments_receivables = '', 'NaN', long_term_investments_receivables) AS long_term_investments_receivables, 
                                IF(long_term_investments_receivables = '', 'NaN', long_term_investments_receivables) AS long_term_investments_receivables, 
                                IF(total_noncurrent_assets = '', 'NaN', total_noncurrent_assets) AS total_noncurrent_assets, 
                                IF(total_assets = '', 'NaN', total_assets) AS total_assets, 
                                IF(payables_accruals = '', 'NaN', payables_accruals) AS payables_accruals, 
                                IF(short_term_debt = '', 'NaN', short_term_debt) AS short_term_debt, 
                                IF(total_current_liabilities = '', 'NaN', total_current_liabilities) AS total_current_liabilities, 
                                IF(long_term_debt = '', 'NaN', long_term_debt) AS long_term_debt, 
                                IF(total_noncurrent_liabilities = '', 'NaN', total_noncurrent_liabilities) AS total_noncurrent_liabilities, 
                                IF(total_liabilities = '', 'NaN', total_liabilities) AS total_liabilities, 
                                IF(share_capital_additional_paid_in_capital = '', 'NaN', share_capital_additional_paid_in_capital) AS share_capital_additional_paid_in_capital, 
                                IF(treasury_stock = '', 'NaN', treasury_stock) AS treasury_stock, 
                                IF(retained_earnings = '', 'NaN', retained_earnings) AS retained_earnings, 
                                IF(total_equity = '', 'NaN', total_equity) AS total_equity, 
                                IF(total_liabilities_equity = '', 'NaN', total_liabilities_equity) AS total_liabilities_equity  
                            FROM z_balance_sheet_general_annual WHERE (ticker = %s);""", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zBalanceSheetGeneralAnnualRecord, row)
                records.append(record)

            return records
