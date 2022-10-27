# *******************************************************************************************
#  File:  _import_cik_map.py
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

__all__ = ['import_cik_file']

import csv
import pathlib
from time import sleep
from loguru import logger
from rich.progress import Progress, TaskID
from .. import config
from .. import datastore as ds
from .. import services as svc


def _read_cik_file(file: pathlib.Path):
    """
    This function reads the contents of the CIK file
    """
    if not file.exists():
        raise ValueError(f"Can't import CIK file: {file}")

    with file.open("r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield svc.CikComponent(**row)


@logger.catch(reraise=True)
def import_cik_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the S&P 100 index
    """
    estimated_rows = 11_500
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.CIK_FILE)
    if file.exists():
        file.unlink()

    svc.download_cik_file(file)

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_cik;")

    with db_conn:
        for row in _read_cik_file(file):
            record_id: int = ds.zCikRecord_insert(row.to_zCikRecord(), db_conn)
            if record_id > 0:
                processed_rows += 1

            actual_rows += 1
            if actual_rows < estimated_rows:
                sleep(0.05)  # for cosmetics
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported CIK file: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True
