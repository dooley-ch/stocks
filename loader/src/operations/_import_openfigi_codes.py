# *******************************************************************************************
#  File:  _import_openfigi_codes.py
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

__all__ = ['import_openfigi_codes']

import pymysql
from loguru import logger
from rich.progress import Progress, TaskID
from .. import config
from .. import datastore as ds
from .. import model
from .. import services as svc


def _get_tickers(db_conn: pymysql.Connection):
    """
    This function gets the ticker records from the master ticker table
    """
    tickers = list()
    records = ds.zMasterTicker_get_all(db_conn)
    for record in records:
        tickers.append(record.ticker)

        if len(tickers) == 50:
            yield tickers
            tickers.clear()

    if len(tickers) > 0:
        yield tickers


@logger.catch(reraise=True)
def import_openfigi_codes(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads the OpenFIGI codes for the target set of tickers
    """
    estimated_rows = 1500
    total_rows = 0
    total_errors = 0

    progress.update(task, visible=True, total=estimated_rows)

    db_conn = ds.get_connection(config.database_info())

    for tickers in _get_tickers(db_conn):
        total_rows += len(tickers)

        data: dict[str, svc.FigiData] = svc.get_figi_codes(tickers, config.openfigi_key())
        for item in data.items():
            openfigi_data = item[1]
            if openfigi_data.figi == '':
                logger.warning(f"Failed to find an OpenFigi code for: {openfigi_data.ticker}")
                continue

            record = model.zOpenFIGIRecord(ticker=openfigi_data.ticker, open_figi=openfigi_data.figi)
            record_id = ds.zOpenFIGI_insert(record, db_conn)
            if record_id == 0:
                total_errors += 1

        progress.update(task, advance=len(tickers))

    progress.update(task, completed=estimated_rows)

    logger.info(f"OpenFigi codes downloaded - Processed: {total_rows} - Errors: {total_errors}")

    return total_errors == 0
