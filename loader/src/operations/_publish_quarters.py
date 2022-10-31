# *******************************************************************************************
#  File:  _publish_quarters.py
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

__all__ = ['publish_quarters']

from typing import Any
import pymysql
from loguru import logger
from .. import config
from .. import datastore as ds
from .. import model


def _build_general_quarter(company: Any, db_conn: pymysql.Connection) -> None:
    """
    This function imports a general quarter figures
    """
    rows = ds.zIncomeGeneralQuarter_get_by_ticker(company.ticker, db_conn)

    if rows:
        for row in rows:
            record = model.Quarter(year=row.fiscal_year, quarter=row.fiscal_period, fiscal_year=row.publish_date,
                                   restated=row.restated_date, shares_basic=row.shares_basic,
                                   shares_diluted=row.shares_diluted,
                                   revenue=row.revenue, pretax_income=row.pretax_income_loss,
                                   tax=row.income_tax_expense_benefit_net,
                                   net_income=row.net_income, net_income_core=row.net_income_common, company_id=company.id)

            ds.quarter_insert(record, db_conn)
    else:
        logger.warning(f"No quarter figures for ticker: {company.ticker}")


def _build_bank_quarter(company: Any, db_conn: pymysql.Connection) -> None:
    """
    This function imports a bank quarter figures
    """
    rows = ds.zIncomeBankQuarter_get_by_ticker(company.ticker, db_conn)

    if rows:
        for row in rows:
            record = model.Quarter(year=row.fiscal_year, quarter=row.fiscal_period, fiscal_year=row.publish_date,
                                   restated=row.restated_date, shares_basic=row.shares_basic,
                                   shares_diluted=row.shares_diluted,
                                   revenue=row.revenue, pretax_income=row.pretax_income_loss,
                                   tax=row.income_tax_expense_benefit_net,
                                   net_income=row.net_income, net_income_core=row.net_income_common, company_id=company.id)

            ds.quarter_insert(record, db_conn)
    else:
        logger.warning(f"No quarter figures for ticker: {company.ticker}")


def _build_insurance_quarter(company: Any, db_conn: pymysql.Connection) -> None:
    """
    This function imports a insurance quarter figures
    """
    rows = ds.zIncomeInsuranceQuarter_get_by_ticker(company.ticker, db_conn)

    if rows:
        for row in rows:
            record = model.Quarter(year=row.fiscal_year, quarter=row.fiscal_period, fiscal_year=row.publish_date,
                                   restated=row.restated_date, shares_basic=row.shares_basic,
                                   shares_diluted=row.shares_diluted,
                                   revenue=row.revenue, pretax_income=row.pretax_income_loss,
                                   tax=row.income_tax_expense_benefit_net,
                                   net_income=row.net_income, net_income_core=row.net_income_common, company_id=company.id)

            ds.quarter_insert(record, db_conn)
    else:
        logger.warning(f"No quarter figures for ticker: {company.ticker}")


@logger.catch(reraise=True)
def publish_quarters() -> bool:
    """
    This function builds the company income statements
    """
    general_rows = 0
    bank_rows = 0
    insurance_rows = 0

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute('DELETE FROM quarter;')

    companies = ds.company_get_financial_tickers(db_conn)

    for company in companies:
        if not company.has_financials:
            logger.warning(f"Company ({company.ticker}) - Does not have income statements")
            continue

        if company.company_type == model.CompanyType.General:
            _build_general_quarter(company, db_conn)
            general_rows += 1
            continue
        if company.company_type == model.CompanyType.Bank:
            _build_bank_quarter(company, db_conn)
            bank_rows += 1
            continue
        if company.company_type == model.CompanyType.Insurance:
            _build_insurance_quarter(company, db_conn)
            insurance_rows += 1

    logger.info(f"Income - General: {general_rows} - Bank: {bank_rows} - Insurance: {insurance_rows}")

    return True
