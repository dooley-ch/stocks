# *******************************************************************************************
#  File:  _import_simfin_bank_cashflow.py
#
#  Created: 28-10-2022
#
#  History:
#  28-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['import_cashflow_bank_annual_file', 'import_cashflow_bank_quarter_file']

import csv
import pathlib
from loguru import logger
from rich.progress import Progress, TaskID
from .. import config
from .. import datastore as ds
from .. import services as svc
from .. import model


_cashflow_bank_header = ['ticker', 'simfin_id', 'currency', 'fiscal_year', 'fiscal_period', 'report_date',
                         'publish_date', 'restated_date', 'shares_basic', 'shares_diluted', 'net_income_starting_line',
                         'depreciation_amortization', 'provision_for_loan_losses', 'non_cash_items',
                         'change_in_working_capital', 'net_cash_from_operating_activities',
                         'change_in_fixed_assets_intangibles', 'net_change_in_loans_interbank',
                         'net_cash_from_acquisitions_divestitures', 'net_cash_from_investing_activities', 'dividends_paid',
                         'cash_from_repayment_of_debt', 'cash_from_repurchase_of_equity', 'net_cash_from_financing_activities',
                         'effect_of_foreign_exchange_rates', 'net_change_in_cash']


def _read_cashflow_bank_file(file: pathlib.Path, delimiter=';'):
    """
    This function reads the contents of a cashflow file
    """
    first_row = True

    if not file.exists():
        raise ValueError(f"Can't import cashflow file: {file}")

    with file.open("r") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if first_row:
                first_row = False
                continue

            row_iterator = zip(_cashflow_bank_header, row)
            data = dict(row_iterator)

            yield data


@logger.catch(reraise=True)
def import_cashflow_bank_annual_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the SimFin Bank Cashflow file - annual
    """
    estimated_rows = 400
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_CASHFLOW_BANK_ANNUAL_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_cashflow_bank_annual(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_cashflow_bank_annual;")

    with db_conn:
        for row in _read_cashflow_bank_file(file):
            record = model.zCashflowBankAnnualRecord(**row)
            record_id: int = ds.zCashflowBankAnnual_insert(record, db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin Bank Annual Cashflow: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True


@logger.catch(reraise=True)
def import_cashflow_bank_quarter_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the SimFin Bank Cashflow file - annual
    """
    estimated_rows = 1_400
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_CASHFLOW_BANK_QUARTER_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_cashflow_bank_quarter(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_cashflow_bank_quarter;")

    with db_conn:
        for row in _read_cashflow_bank_file(file):
            record = model.zCashflowBankQuarterRecord(**row)
            record_id: int = ds.zCashflowBankQuarter_insert(record, db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin Bank Quarter Cashflow: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True
