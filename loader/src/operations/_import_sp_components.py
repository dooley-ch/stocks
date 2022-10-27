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

from time import sleep

from rich.progress import Progress, TaskID


def import_sp_100_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the S&P 100 index
    """
    progress.update(task, visible=True, total=100)

    for i in range(1,99):
        sleep(0.10)
        progress.update(task, advance=1)

    progress.update(task, completed=100)

    return False


def import_sp_600_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the S&P 600 index
    """
    progress.update(task, visible=True, total=600)

    for i in range(1,540):
        sleep(0.05)
        progress.update(task, advance=1)

    progress.update(task, completed=600)

    return False


def import_sp_400_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the S&P 400 index
    """
    progress.update(task, visible=True, total=400)

    for i in range(1,380):
        sleep(0.05)
        progress.update(task, advance=1)

    progress.update(task, completed=400)

    return False


def import_sp_500_file(progress: Progress, task: TaskID) -> bool:
    """
    This function downloads and imports the S&P 500 index
    """
    progress.update(task, visible=True, total=500)

    for i in range(1,480):
        sleep(0.05)
        progress.update(task, advance=1)

    progress.update(task, completed=500)

    return False
