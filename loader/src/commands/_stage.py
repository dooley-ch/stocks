# *******************************************************************************************
#  File:  _stage.py
#
#  Created: 26-10-2022
#
#  History:
#  26-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['stage']

from rich.text import Text
from loguru import logger
from .. import ui
from .. import operations as ops


def stage() -> bool:
    """
    This function handles the staging of the imported data
    """
    ui.console.clear(home=True)
    ui.console.line(1)
    ui.line("Stage Data")

    logger.info("*** === Started Staging Data === ***")

    with ui.console.status("Building Sectors and Industries..."):
        ops.build_sectors_industries()
        msg = Text(" Sectors built successfully...", style="grey50 on black")
        ui.console.print(msg)
        msg = Text(" Industries built successfully...", style="grey50 on black")
        ui.console.print(msg)

    with ui.console.status("Building Companies"):
        ops.build_companies()
        msg = Text(" Companies successfully...", style="grey50 on black")
        ui.console.print(msg)

    logger.info("*** === Ended Staging Data === ***")

    return True
