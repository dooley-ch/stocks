# *******************************************************************************************
#  File:  _wikipedia.py
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

__all__ = ['download_sp100', 'download_sp600', 'download_sp400', 'download_sp500']

import csv
from pathlib import Path
import loguru
import bs4
from attr import asdict
from . _core import get_web_page
from . _model import IndexComponent

_sp100_url = "https://en.wikipedia.org/wiki/S%26P_100"
_sp600_url = "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies"
_sp400_url = "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies"
_sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"


def _write_sp_file(data: list[IndexComponent], file: Path) -> None:
    """
    This function writes an S&P file
    """
    header = ['ticker', 'name', 'industry']

    if file.exists():
        file.unlink()

    with file.open('w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        for item in data:
            # noinspection PyTypeChecker,PyDataclass
            row = asdict(item)
            writer.writerow(row.values())


@loguru.logger.catch(reraise=True)
def download_sp100(data_file: Path) -> None:
    """
    This function downloads the S&P 100 file
    """
    contents = get_web_page(_sp100_url)
    components: list[IndexComponent] = list()

    if contents:
        soup = bs4.BeautifulSoup(contents, 'html.parser')
        table = soup.find('table', attrs={'id': 'constituents'})
        if table:
            tbody = table.find('tbody')
            if tbody:
                rows = tbody.find_all('tr')
                if rows:
                    for row in rows:
                        name = str(row.contents[3].text).strip()
                        ticker = str(row.contents[1].text).strip()
                        industry = str(row.contents[5].text).strip()

                        if name == 'Name':
                            continue

                        components.append(IndexComponent(ticker, name, industry))

    if components:
        _write_sp_file(components, data_file)


@loguru.logger.catch(reraise=True)
def download_sp600(data_file: Path) -> None:
    """
    This function downloads the S&P 600 file
    """
    contents = get_web_page(_sp600_url)
    components: list[IndexComponent] = list()

    if contents:
        soup = bs4.BeautifulSoup(contents, 'html.parser')
        table = soup.find('table', attrs={'id': 'constituents'})
        if table:
            tbody = table.find('tbody')
            if tbody:
                rows = tbody.find_all('tr')
                if rows:
                    for row in rows:
                        name = str(row.contents[1].text).strip()
                        ticker = str(row.contents[3].text).strip()
                        industry = str(row.contents[7].text).strip()

                        if name == 'Company':
                            continue

                        components.append(IndexComponent(ticker, name, industry))

    if components:
        _write_sp_file(components, data_file)


@loguru.logger.catch(reraise=True)
def download_sp400(data_file: Path) -> None:
    """
    This function downloads the S&P 400 file
    """
    contents = get_web_page(_sp400_url)
    components: list[IndexComponent] = list()

    if contents:
        soup = bs4.BeautifulSoup(contents, 'html.parser')
        table = soup.find('table', attrs={'id': 'constituents'})
        if table:
            tbody = table.find('tbody')
            if tbody:
                rows = tbody.find_all('tr')
                if rows:
                    for row in rows:
                        name = str(row.contents[3].text).strip()
                        ticker = str(row.contents[1].text).strip()
                        industry = str(row.contents[5].text).strip()

                        if name == 'Security':
                            continue

                        components.append(IndexComponent(ticker, name, industry))

    if components:
        _write_sp_file(components, data_file)


@loguru.logger.catch(reraise=True)
def download_sp500(data_file: Path) -> None:
    """
    This function downloads the S&P 500 file
    """
    contents = get_web_page(_sp500_url)
    components: list[IndexComponent] = list()

    if contents:
        soup = bs4.BeautifulSoup(contents, 'html.parser')
        table = soup.find('table', attrs={'id': 'constituents'})
        if table:
            tbody = table.find('tbody')
            if tbody:
                rows = tbody.find_all('tr')
                if rows:
                    for row in rows:
                        name = str(row.contents[3].text).strip()
                        ticker = str(row.contents[1].text).strip()
                        industry = str(row.contents[9].text).strip()

                        if name == 'Security':
                            continue

                        components.append(IndexComponent(ticker, name, industry))

    if components:
        _write_sp_file(components, data_file)
