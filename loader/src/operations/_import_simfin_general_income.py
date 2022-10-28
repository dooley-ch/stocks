# *******************************************************************************************
#  File:  _import_simfin_general_income.py
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

__all__ = ['import_income_general_annual_file', 'import_income_general_quarter_file']

import csv
import pathlib
from loguru import logger
from rich.progress import Progress, TaskID
from .. import config
from .. import datastore as ds
from .. import services as svc
from .. import model


_income_general_header = ['ticker', 'simfin_id', 'currency', 'fiscal_year', 'fiscal_period', 'report_date',
                          'publish_date', 'restated_date', 'shares_basic', 'shares_diluted', 'revenue',
                          'cost_of_revenue', 'gross_profit', 'operating_expenses', 'selling_general_administrative',
                          'research_development', 'depreciation_amortization', 'operating_income',
                          'non_operating_income',
                          'interest_expense_net', 'pretax_income_loss_adj', 'abnormal_gains_lLosses',
                          'pretax_income_loss',
                          'income_tax_expense_benefit_net', 'income_loss_from_continuing_operations',
                          'net_extraordinary_gains_losses', 'net_income', 'net_income_common']


def _read_income_general_file(file: pathlib.Path, delimiter=';'):
    """
    This function reads the contents of an income file
    """
    first_row = True

    if not file.exists():
        raise ValueError(f"Can't import income file: {file}")

    with file.open("r") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if first_row:
                first_row = False
                continue

            row_iterator = zip(_income_general_header, row)
            data = dict(row_iterator)

            yield data


@logger.catch(reraise=True)
def import_income_general_annual_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the SimFin General Income file - annual
    """
    estimated_rows = 11_000
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_INCOME_GENERAL_ANNUAL_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_income_general_annual(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_income_general_annual;")

    with db_conn:
        for row in _read_income_general_file(file):
            record = model.zIncomeGeneralAnnualRecord(**row)
            record_id: int = ds.zIncomeGeneralAnnual_insert(record, db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin General Annual Income: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True


@logger.catch(reraise=True)
def import_income_general_quarter_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the SimFin General Income file - quarterly
    """
    estimated_rows = 40_000
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_INCOME_GENERAL_QUARTER_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_income_general_quarter(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_income_general_quarter;")

    with db_conn:
        for row in _read_income_general_file(file):
            record = model.zIncomeGeneralQuarterRecord(**row)
            record_id: int = ds.zIncomeGeneralQuarter_insert(record, db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin General Quarter Income: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True
