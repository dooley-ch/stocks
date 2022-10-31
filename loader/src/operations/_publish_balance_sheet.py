# *******************************************************************************************
#  File:  _build_balance_sheet.py
#
#  Created: 21-10-2022
#
#  History:
#  21-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['publish_balance_sheet_annual']

from typing import Any
import pymysql
from loguru import logger
from .. import datastore as ds
from .. import model
from .. import config


def _build_general_balance_sheet(company: Any, db_conn: pymysql.Connection) -> None:
    """
    This function imports a general balance sheet statement
    """
    rows = ds.zBalanceSheetGeneralAnnual_get_by_ticker(company.ticker, db_conn)

    for row in rows:
        record = model.BalanceSheet(
            fiscal_year=row.publish_date,
            restated=row.restated_date,
            shares_basic=row.shares_basic,
            shares_diluted=row.shares_diluted,
            cash=row.cash_cash_equivalents_short_term_investments,
            accounts_receivable=row.accounts_notes_receivable,
            inventories=row.inventories,
            current_assets=row.total_current_assets,
            total_assets=row.total_assets,
            accounts_payable=row.payables_accruals,
            current_liabilities=row.total_current_liabilities,
            long_term_debt=row.long_term_debt,
            share_capital=row.share_capital_additional_paid_in_capital,
            total_capital=row.total_equity,
            company_id=company.id)
        record = record.evolve(year=record.fiscal_year.year)

        ds.balance_sheet_insert(record, db_conn)


def _build_bank_balance_sheet(company: Any, db_conn: pymysql.Connection) -> None:
    """
    This function imports a bank balance sheet statement
    """
    rows = ds.zBalanceSheetBankAnnual_get_by_ticker(company.ticker, db_conn)

    for row in rows:
        record = model.BalanceSheet(
            fiscal_year=row.publish_date,
            restated=row.restated_date,
            shares_basic=row.shares_basic,
            shares_diluted=row.shares_diluted,
            cash=row.cash_cash_equivalents_short_term_investments,
            total_assets=row.total_assets,
            long_term_debt=row.long_term_debt,
            share_capital=row.share_capital_additional_paid_in_capital,
            total_capital=row.total_equity,
            bnk_inter_bank_assets=row.interbank_Assets,
            bnk_net_loans=row.net_loans,
            bnk_total_deposits=row.total_deposits,
            company_id=company.id)
        record = record.evolve(year=record.fiscal_year.year)

        ds.balance_sheet_insert(record, db_conn)


def _build_insurance_balance_sheet(company: Any, db_conn: pymysql.Connection) -> None:
    """
    This function imports an insurance balance sheet statement
    """
    rows = ds.zBalanceSheetInsuranceAnnual_get_by_ticker(company.ticker, db_conn)

    for row in rows:
        record = model.BalanceSheet(
            fiscal_year=row.publish_date,
            restated=row.restated_date,
            shares_basic=row.shares_basic,
            shares_diluted=row.shares_diluted,
            cash=row.cash_cash_equivalents_short_term_investments,
            accounts_receivable=row.accounts_notes_receivable,
            total_assets=row.total_assets,
            long_term_debt=row.long_term_debt,
            share_capital=row.share_capital_additional_paid_in_capital,
            total_capital=row.total_equity,
            ins_total_investments=row.total_investments,
            ins_insurance_reserves=row.insurance_reserves,
            ins_policyholders_equity=row.policyholders_equity,
            company_id=company.id)
        record = record.evolve(year=record.fiscal_year.year)

        ds.balance_sheet_insert(record, db_conn)


# noinspection SqlWithoutWhere
@logger.catch(reraise=True)
def publish_balance_sheet_annual() -> bool:
    """
    This function builds the company balance sheets
    """
    general_rows = 0
    bank_rows = 0
    insurance_rows = 0

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        cursor.execute('DELETE FROM balance_sheet;')

    companies = ds.company_get_financial_tickers(db_conn)

    for company in companies:
        if not company.has_financials:
            logger.warning(f"Company ({company.ticker}) - Does not have balance sheet statements")
            continue

        if company.company_type == model.CompanyType.General:
            _build_general_balance_sheet(company, db_conn)
            general_rows += 1
            continue
        if company.company_type == model.CompanyType.Bank:
            _build_bank_balance_sheet(company, db_conn)
            bank_rows += 1
            continue
        if company.company_type == model.CompanyType.Insurance:
            _build_insurance_balance_sheet(company, db_conn)
            insurance_rows += 1

    logger.info(f"Income - General: {general_rows} - Bank: {bank_rows} - Insurance: {insurance_rows}")

    return True
