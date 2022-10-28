# *******************************************************************************************
#  File:  _import_simfin_general_balance_sheet.py
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

__all__ = ['import_balance_sheet_general_annual_file', 'import_balance_sheet_general_quarter_file']

import csv
import pathlib
from loguru import logger
from rich.progress import Progress, TaskID
from .. import config
from .. import datastore as ds
from .. import services as svc
from .. import model


_balance_sheet_general_header = ['ticker', 'simfin_id', 'currency', 'fiscal_year', 'fiscal_period', 'report_date',
                                 'publish_date', 'restated_date', 'shares_basic', 'shares_diluted',
                                 'cash_cash_equivalents_short_term_investments', 'accounts_notes_receivable',
                                 'inventories', 'total_current_assets', 'property_plant_equipment_net',
                                 'long_term_investments_receivables', 'other_long_term_assets', 'total_noncurrent_assets',
                                 'total_assets', 'payables_accruals', 'short_term_debt', 'total_current_liabilities',
                                 'long_term_debt', 'total_noncurrent_liabilities', 'total_liabilities',
                                 'share_capital_additional_paid_in_capital', 'treasury_stock', 'retained_earnings',
                                 'total_equity', 'total_liabilities_equity']


def _read_balance_sheet_general_file(file: pathlib.Path, delimiter=';'):
    """
    This function reads the contents of a balance sheet file
    """
    first_row = True

    if not file.exists():
        raise ValueError(f"Can't import balance sheet file: {file}")

    with file.open("r") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if first_row:
                first_row = False
                continue

            row_iterator = zip(_balance_sheet_general_header, row)
            data = dict(row_iterator)

            yield data


@logger.catch(reraise=True)
def import_balance_sheet_general_annual_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the SimFin General Balance Sheet file - annual
    """
    estimated_rows = 11_000
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_BALANCE_GENERAL_ANNUAL_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_balance_general_annual(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_balance_sheet_general_annual;")

    with db_conn:
        for row in _read_balance_sheet_general_file(file):
            record = model.zBalanceSheetGeneralAnnualRecord(**row)
            record_id: int = ds.zBalanceSheetGeneralAnnual_insert(record, db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin General Annual Balance Sheet: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True


@logger.catch(reraise=True)
def import_balance_sheet_general_quarter_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the SimFin General Balance Sheet file - annual
    """
    estimated_rows = 40_000
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_BALANCE_GENERAL_QUARTER_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_balance_general_quarter(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_balance_sheet_general_quarter;")

    with db_conn:
        for row in _read_balance_sheet_general_file(file):
            record = model.zBalanceSheetGeneralQuarterRecord(**row)
            record_id: int = ds.zBalanceSheetGeneralQuarter_insert(record, db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin General Quarter Balance Sheet: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True
