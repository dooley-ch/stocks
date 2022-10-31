# *******************************************************************************************
#  File:  _publish_cashflow.py
#
#  Created: 31-10-2022
#
#  History:
#  31-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['publish_cashflow_figures']

import pymysql
from loguru import logger
from .. import config
from .. import datastore as ds
from .. import model


def _update_general_cashflow(ticker: str, company_id: int, db_conn: pymysql.Connection):
    """
    This function updates the general balance sheets with the cashflow figures:
    """
    cashflows = ds.zCashflowGeneralAnnual_get_by_ticker(ticker, db_conn)
    if cashflows:
        for cashflow in cashflows:
            bs = ds.balance_sheet_get_by_year(company_id, int(cashflow.fiscal_year), db_conn)
            if bs:
                expenditure = cashflow.change_in_fixed_assets_intangibles if cashflow.change_in_fixed_assets_intangibles != '' else 'NaN'
                net_cashflow = cashflow.net_change_in_cash if cashflow.net_change_in_cash != '' else 'NaN'
                bs = bs.evolve(capital_expenditure=expenditure, cashflow=net_cashflow)
                ds.balance_sheet_update(bs, db_conn)


def _update_bank_cashflow(ticker: str, company_id: int, db_conn: pymysql.Connection):
    """
    This function updates the bank balance sheets with the cashflow figures:
    """
    cashflows = ds.zCashflowBankAnnual_get_by_ticker(ticker, db_conn)
    if cashflows:
        for cashflow in cashflows:
            bs = ds.balance_sheet_get_by_year(company_id, int(cashflow.fiscal_year), db_conn)
            if bs:
                expenditure = cashflow.change_in_fixed_assets_intangibles if cashflow.change_in_fixed_assets_intangibles != '' else 'NaN'
                net_cashflow = cashflow.net_change_in_cash if cashflow.net_change_in_cash != '' else 'NaN'
                bs = bs.evolve(capital_expenditure=expenditure, cashflow=net_cashflow)
                ds.balance_sheet_update(bs, db_conn)


def _update_insurance_cashflow(ticker: str, company_id: int, db_conn: pymysql.Connection):
    """
    This function updates the insurance balance sheets with the cashflow figures:
    """
    cashflows = ds.zCashflowInsuranceAnnual_get_by_ticker(ticker, db_conn)
    if cashflows:
        for cashflow in cashflows:
            bs = ds.balance_sheet_get_by_year(company_id, int(cashflow.fiscal_year), db_conn)
            if bs:
                expenditure = cashflow.change_in_fixed_Assets_intangibles if cashflow.change_in_fixed_Assets_intangibles != '' else 'NaN'
                net_cashflow = cashflow.net_change_in_cash if cashflow.net_change_in_cash != '' else 'NaN'
                bs = bs.evolve(capital_expenditure=expenditure, cashflow=net_cashflow)
                ds.balance_sheet_update(bs, db_conn)



@logger.catch(reraise=True)
def publish_cashflow_figures() -> bool:
    """
    This function updates the balance sheet statement with the relevant cashflow figures
    """
    general_rows = 0
    bank_rows = 0
    insurance_rows = 0

    db_conn = ds.get_connection(config.database_info())

    companies = ds.company_get_financial_tickers(db_conn)

    for company in companies:
        if not company.has_financials:
            logger.warning(f"Company ({company.ticker}) - Does not have income statements")
            continue

        if company.company_type == model.CompanyType.General:
            _update_general_cashflow(company.ticker, company.id, db_conn)
            general_rows += 1
            continue

        if company.company_type == model.CompanyType.Bank:
            _update_bank_cashflow(company.ticker, company.id, db_conn)
            bank_rows += 1
            continue

        if company.company_type == model.CompanyType.Insurance:
            _update_insurance_cashflow(company.ticker, company.id, db_conn)
            insurance_rows += 1

    logger.info(f"Cashflow updates - General: {general_rows} - Bank: {bank_rows} - Insurance: {insurance_rows}")

    return True
