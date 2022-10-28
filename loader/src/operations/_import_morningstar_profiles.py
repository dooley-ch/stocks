# *******************************************************************************************
#  File:  _import_morningstar_profiles.py
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

__all__ = ['import_morningstar_profiles']

from loguru import logger
from rich.progress import Progress, TaskID
from .. import config
from .. import datastore as ds
from .. import services as svc


@logger.catch(reraise=True)
def import_morningstar_profiles(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads the Morningstar profiles
    """
    estimated_rows = 1550
    total_rows = 0
    total_errors = 0

    progress.update(task, visible=True, total=estimated_rows)

    db_conn = ds.get_connection(config.database_info())

    records = ds.zMasterTicker_get_all(db_conn)

    for record in records:
        total_rows += 1

        cik_record = ds.zCikRecord_get_by_ticker(record.ticker, db_conn)
        if cik_record is None:
            logger.warning(f"Failed to get stock exchange: {record.ticker}")
            continue

        profile = svc.get_morningstar_profile(cik_record.exchange, record.ticker)

        if profile is None:
            logger.warning(f"Failed to get profile for: {record.ticker}")
            continue

        record_id = ds.zMorningstarProfileRecord_insert(profile.to_zMorningstarProfileRecord(), db_conn)
        if record_id == 0:
            total_errors += 1

        progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Morningstar profiles downloaded - Processed: {total_rows} - Errors: {total_errors}")

    return total_errors == 0
