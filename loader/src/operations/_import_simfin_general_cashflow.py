# *******************************************************************************************
#  File:  _import_simfin_general_cashflow.py
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

__all__ = ['import_cashflow_general_annual_file', 'import_cashflow_general_quarter_file']


import csv
import pathlib
from loguru import logger
from rich.progress import Progress, TaskID
from .. import config
from .. import datastore as ds
from .. import services as svc
from .. import model


_cashflow_general_header = ['ticker', 'simfin_id', 'currency', 'fiscal_year', 'fiscal_period', 'report_date',
                            'publish_date', 'restated_date', 'shares_basic', 'shares_diluted', 'net_income_starting_line',
                            'depreciation_amortization', 'non_cash_items', 'change_in_working_capital',
                            'change_in_accounts_receivable', 'change_in_inventories', 'change_in_accounts_payable',
                            'change_in_other', 'net_cash_from_operating_Activities', 'change_in_fixed_assets_intangibles',
                            'net_change_in_long_term_investment', 'net_cash_from_acquisitions_divestitures',
                            'net_cash_from_investing_activities', 'dividends_paid', 'cash_from_repayment_of_debt',
                            'cash_from_repurchase_of_equity', 'net_cash_from_financing_activities', 'net_change_in_cash']


def _read_cashflow_general_file(file: pathlib.Path, delimiter=';'):
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

            row_iterator = zip(_cashflow_general_header, row)
            data = dict(row_iterator)

            yield data


@logger.catch(reraise=True)
def import_cashflow_general_annual_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the SimFin General Cashflow file - annual
    """
    estimated_rows = 11_000
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_CASHFLOW_GENERAL_ANNUAL_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_cashflow_general_annual(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_cashflow_general_annual;")

    with db_conn:
        for row in _read_cashflow_general_file(file):
            record = model.zCashflowGeneralAnnualRecord(**row)
            record_id: int = ds.zCashflowGeneralAnnual_insert(record, db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin General Annual Cashflow: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True


@logger.catch(reraise=True)
def import_cashflow_general_quarter_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the SimFin General Cashflow file - annual
    """
    estimated_rows = 40_000
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_CASHFLOW_GENERAL_QUARTER_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_cashflow_general_quarter(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_cashflow_general_quarter;")

    with db_conn:
        for row in _read_cashflow_general_file(file):
            record = model.zCashflowGeneralQuarterRecord(**row)
            record_id: int = ds.zCashflowGeneralQuarter_insert(record, db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin General Quarter Cashflow: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True
