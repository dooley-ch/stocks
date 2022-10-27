# *******************************************************************************************
#  File:  _import_simfin_companies_and_industries.py
#
#  Created: 27-10-2022
#
#  History:
#  27-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['import_industries_file', 'import_companies_file']

import csv
import pathlib
from loguru import logger
from rich.progress import Progress, TaskID
from .. import config
from .. import datastore as ds
from .. import services as svc


def _read_company_file(file: pathlib.Path):
    """
    This function reads the contents of the companies file
    """
    with file.open("r") as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            ticker = row['Ticker']
            simfin_id = int(row['SimFinId']) if row['SimFinId'] else 0
            name = row['Company Name']
            industry_id = int(row['IndustryId']) if row['IndustryId'] else 0

            yield svc.SimFinCompany(ticker=ticker, simfin_id=simfin_id, company_name=name, industry_id=industry_id)


def _read_industry_file(file: pathlib.Path):
    """
    This function reads the contents of the industries file
    """
    with file.open("r") as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            industry_id = int(row['IndustryId']) if row['IndustryId'] else 0
            sector = row['Sector']
            industry = row['Industry']

            yield svc.SimFinIndustry(industry_id, sector, industry)


@logger.catch(reraise=True)
def import_industries_file(progress: Progress, task: TaskID) -> bool:
    """
    This function imports the industries file
    """
    estimated_rows = 70
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_INDUSTRIES_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_industries(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_simfin_industries;")

    with db_conn:
        for row in _read_industry_file(file):
            record_id: int = ds.zSimFinIndustries_insert(row.to_zSimFinIndustriesRecord(), db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin Industries: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True


@logger.catch(reraise=True)
def import_companies_file(progress: Progress, task: TaskID) -> bool:
    """
    This function imports the companies file
    """
    estimated_rows = 3_100
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SIMFIN_COMPANIES_FILE)
    if file.exists():
        file.unlink()

    svc.download_simfin_companies(config.data_folder(), config.simfin_key())

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_simfin_companies;")

    with db_conn:
        for row in _read_company_file(file):
            record_id: int = ds.zSimFinCompanies_insert(row.to_zSimFinCompaniesRecord(), db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported SimFin Companies: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True
