# *******************************************************************************************
#  File:  _build_income.py
#
#  Created: 20-10-2022
#
#  History:
#  20-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['publish_income_annual']

from typing import Any
import pymysql
from loguru import logger
from .. import config
from .. import datastore as ds
from .. import model


def _build_general_income(company: Any, db_conn: pymysql.Connection) -> None:
    """
    This function imports a general income statement
    """
    rows = ds.zIncomeGeneralAnnual_get_by_ticker(company.ticker, db_conn)

    for row in rows:
        record = model.Income(
            fiscal_year=row.publish_date,
            restated=row.restated_date,
            revenue=row.revenue if row.revenue != '' else 'NaN',
            gross_profit=row.gross_profit if row.gross_profit != '' else 'NaN',
            depreciation=row.depreciation_amortization if row.depreciation_amortization != '' else 'NaN',
            interest_expense=row.interest_expense_net if row.interest_expense_net != '' else 'NaN',
            pretax_income=row.pretax_income_loss if row.pretax_income_loss != '' else 'NaN',
            tax=row.income_tax_expense_benefit_net if row.income_tax_expense_benefit_net != '' else 'NaN',
            net_income=row.net_income if row.net_income != '' else 'NaN',
            net_income_core=row.net_income_common if row.net_income_common != '' else 'NaN',
            company_id=company.id)
        record = record.evolve(year=record.fiscal_year.year)

        ds.income_insert(record, db_conn)


def _build_bank_income(company: Any, db_conn: pymysql.Connection) -> None:
    """
    This function imports a bank income statement
    """
    rows = ds.zIncomeBankAnnual_get_by_ticker(company.ticker, db_conn)

    for row in rows:
        record = model.Income(
            fiscal_year=row.publish_date,
            restated=row.restated_date,
            revenue=row.net_Revenue_after_provisions,
            pretax_income=row.pretax_income_loss,
            tax=row.income_tax_expense_benefit_net,
            net_income=row.net_income,
            net_income_core=row.net_income_common,
            bnk_provision_for_loan_losses=row.provision_for_loan_losses,
            bnk_operating_income=row.operating_income_loss,
            company_id=company.id)
        record = record.evolve(year=record.fiscal_year.year)

        ds.income_insert(record, db_conn)


def _build_insurance_income(company: Any, db_conn: pymysql.Connection) -> None:
    """
    This function imports an insurance income statement
    """
    rows = ds.zIncomeInsuranceAnnual_get_by_ticker(company.ticker, db_conn)

    for row in rows:
        record = model.Income(
            fiscal_year=row.publish_date,
            restated=row.restated_date,
            revenue=row.revenue,
            pretax_income=row.pretax_income_loss,
            tax=row.income_tax_expense_benefit_net,
            net_income=row.net_income,
            net_income_core=row.net_income_common,
            ins_total_claims=row.total_claims_losses,
            ins_operating_income=row.operating_income_loss,
            company_id=company.id)
        record = record.evolve(year=record.fiscal_year.year)

        ds.income_insert(record, db_conn)


# noinspection SqlWithoutWhere
@logger.catch(reraise=True)
def publish_income_annual() -> bool:
    """
    This function builds the company income statements
    """
    general_rows = 0
    bank_rows = 0
    insurance_rows = 0

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        cursor.execute('DELETE FROM income;')

    companies = ds.company_get_financial_tickers(db_conn)

    for company in companies:
        if not company.has_financials:
            logger.warning(f"Company ({company.ticker}) - Does not have income statements")
            continue

        if company.company_type == model.CompanyType.General:
            _build_general_income(company, db_conn)
            general_rows += 1
            continue
        if company.company_type == model.CompanyType.Bank:
            _build_bank_income(company, db_conn)
            bank_rows += 1
            continue
        if company.company_type == model.CompanyType.Insurance:
            _build_insurance_income(company, db_conn)
            insurance_rows += 1

    logger.info(f"Income - General: {general_rows} - Bank: {bank_rows} - Insurance: {insurance_rows}")

    return True
