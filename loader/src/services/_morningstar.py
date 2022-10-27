# *******************************************************************************************
#  File:  _morningstar.py
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

__all__ = ['get_morningstar_profile']

from bs4 import BeautifulSoup
from . _model import MorningstarProfile
from ._core import get_web_page

_url = "https://www.morningstar.com/stocks/<exchange>/<symbol>/quote"


def _map_exchange(value: str):
    """
    This function maps a CIK exchange to a morningstar exchange
    """
    ret_value = value.upper()
    match ret_value:
        case 'NYSE':
            ret_value = 'xnys'
        case 'NASDAQ':
            ret_value = 'xnas'
        case 'CBOE':
            ret_value = 'bats'
        case 'BATS':
            ret_value = 'bats'
        case _:
            raise ValueError(f"Stock exchange not supported: {value}")

    return ret_value


# noinspection PyUnresolvedReferences
def get_morningstar_profile(exchange: str, ticker: str) -> MorningstarProfile | None:
    """
    This function download a company profile from the morningstar website
    """
    exchange = _map_exchange(exchange)

    url = _url.replace('<exchange>', exchange).replace('<symbol>', ticker)

    data = get_web_page(url)

    if data:
        soup = BeautifulSoup(data, 'html.parser')

        # Ticker & Name
        data = soup.find('div', {'class': 'mdc-security-header__inner'})
        if data:
            data = data.contents[0]
            name = data.contents[0].text.strip()
            symbol = data.contents[1].text.strip()
        else:
            raise ServieError(f"Unable to parse data for ticker: {ticker}")

        #        data = soup.find('div', {'class' : 'stock__content-articles stock__profile'})

        data = soup.find('p', {'itemprop': 'description', 'class': 'stock__profile-description-text'})
        description = str(data.contents[0]).strip()

        data = soup.findAll('div', {
            'class': 'mdc-column mds-layout-grid__col stock__profile-items-item mds-layout-grid__col--6 '
                     'mds-layout-grid__col--3-at-768 mds-layout-grid__col--6-at-1304'})
        sector = str(data[0].contents[2].contents[0]).strip()
        industry = str(data[1].contents[2].contents[0]).strip()
        recent_earnings = str(data[2].contents[2].contents[0]).strip()
        fiscal_year_end = str(data[3].contents[2].contents[0]).strip()
        stock_type = ''
        employees = str(data[4].contents[2].contents[0]).strip()

        return MorningstarProfile(symbol, name, description, sector, industry, recent_earnings,
                                  fiscal_year_end, stock_type, employees)
