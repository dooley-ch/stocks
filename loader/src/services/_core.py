# *******************************************************************************************
#  File:  _core.py
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

__all__ = ['get_web_page']

import requests
import retry
import loguru

@retry.retry(Exception, tries=10, delay=3)
def get_web_page(url: str) -> str | None:
    """
    This function downloads the page specified by the URL
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

    if response.status_code != 404:
        loguru.logger.error(f"url: {url}, code: {response.status_code}")
