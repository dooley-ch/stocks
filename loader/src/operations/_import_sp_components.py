# *******************************************************************************************
#  File:  _import_sp_components.py
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

__all__ = ['import_sp_100_file', 'import_sp_600_file', 'import_sp_400_file', 'import_sp_500_file']

import csv
import pathlib
from time import sleep
from loguru import logger
from rich.progress import Progress, TaskID
from .. import config
from .. import services as svc


def _read_sp_file(file: pathlib.Path):
    """
    This function reads the contents of an S&P file
    """
    if not file.exists():
        raise ValueError(f"Can't import S&P file: {file}")

    with file.open("r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield svc.IndexComponent(**row)


@logger.catch(reraise=True)
def import_sp_100_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the S&P 100 index
    """
    estimated_rows = 100
    actual_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SP_100_FILE)
    if file.exists():
        file.unlink()

    svc.download_sp100(file)

    for row in _read_sp_file(file):
        actual_rows += 1
        if actual_rows < estimated_rows:
            sleep(0.05)  # for cosmetics
            progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported S&P 100 index: {actual_rows} rows loaded")

    return True


@logger.catch(reraise=True)
def import_sp_600_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the S&P 600 index
    """
    estimated_rows = 600
    actual_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SP_600_FILE)
    if file.exists():
        file.unlink()

    svc.download_sp600(file)

    for row in _read_sp_file(file):
        actual_rows += 1
        if actual_rows < estimated_rows:
            sleep(0.05)  # for cosmetics
            progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported S&P 600 index: {actual_rows} rows loaded")

    return True


@logger.catch(reraise=True)
def import_sp_400_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the S&P 400 index
    """
    estimated_rows = 400
    actual_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SP_400_FILE)
    if file.exists():
        file.unlink()

    svc.download_sp400(file)

    for row in _read_sp_file(file):
        actual_rows += 1
        if actual_rows < estimated_rows:
            sleep(0.05)  # for cosmetics
            progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported S&P 400 index: {actual_rows} rows loaded")

    return True


@logger.catch(reraise=True)
def import_sp_500_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the S&P 500 index
    """
    estimated_rows = 100
    actual_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.SP_500_FILE)
    if file.exists():
        file.unlink()

    svc.download_sp500(file)

    for row in _read_sp_file(file):
        actual_rows += 1
        if actual_rows < estimated_rows:
            sleep(0.05)  # for cosmetics
            progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported S&P 500 index: {actual_rows} rows loaded")

    return True
