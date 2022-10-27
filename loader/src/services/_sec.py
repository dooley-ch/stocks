# *******************************************************************************************
#  File:  _sec.py
#
#  Created: 31-08-2022
#
#  History:
#  31-08-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['download_cik_file']

import csv
import loguru
from pathlib import Path

import orjson
from attrs import asdict

from . _core import get_web_page
from . _model import CikComponent


_cik_url = "https://www.sec.gov/files/company_tickers_exchange.json"


@loguru.logger.catch(reraise=True)
def download_cik_file(file: Path) -> None:
    """
    This function downloads the CIK file
    """
    contents = get_web_page(_cik_url)
    records: list[CikComponent] = list()

    if contents:
        data = orjson.loads(contents)
        fields = data['fields']
        rows = data['data']

        for row in rows:
            record_data = dict(zip(fields, row))
            record = CikComponent(**record_data)
            records.append(record)

    if records:
        header = ['cik', 'name', 'ticker', 'exchange']

        if file.exists():
            file.unlink()

        with file.open('w', encoding='UTF8') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            for item in records:
                # noinspection PyDataclass
                row = asdict(item)
                writer.writerow(row.values())
