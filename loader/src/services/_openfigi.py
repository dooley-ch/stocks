# *******************************************************************************************
#  File:  _openfigi.py
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

__all__ = ['get_figi_codes']

import requests
from orjson import orjson

from . _model import FigiData
from . _errors import ServiceError, ServiceLimitExceeded


def get_figi_codes(tickers: list[str], key: str) -> dict[str, FigiData] | None:
    """
    This function obtains OpenFIGI data for a given list of tickers
    """
    query = [{'idType': 'TICKER', 'idValue': ticker, 'exchCode': 'US'} for ticker in tickers]
    headers = {'Content-Type': 'text/json', 'X-OPENFIGI-APIKEY': key}

    response = requests.post(url="https://api.openfigi.com/v1/mapping", headers=headers, json=query)

    if response.status_code == 429:
        raise ServiceLimitExceeded(f"{response.status_code} - {response.text}")

    if response.status_code != 200:
        raise ServiceError(f"{response.status_code} - {response.text}")

    content = orjson.loads(response.text)

    if 'error' in content[0]:
        msg: str = content[0]['error']
        if msg == 'No identifier found.':
            return None
        raise ServiceError(f"Error while seeking FIGI code for: {' '.join(tickers)} - {response.status_code} - {msg}")

    records: dict[str, FigiData] = dict()
    for index, row in enumerate(content):
        if 'error' in row:
            msg = row['error']
            if msg == 'No identifier found.':
                records[tickers[index]] = FigiData(tickers[index], '', '')
                continue
            raise ServiceError(f"Unexpected response from OpenFIGI API: {tickers[index]} - {msg}")

        ticker = row['data'][0]['ticker']
        figi = row['data'][0]['figi']
        name = row['data'][0]['name']
        records[tickers[index]] = FigiData(ticker, name, figi)

    return records
