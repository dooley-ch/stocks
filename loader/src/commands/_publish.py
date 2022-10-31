# *******************************************************************************************
#  File:  _publish.py
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

__all__ = []

from rich.text import Text
from loguru import logger
from .. import ui
from .. import operations as ops


def publish() -> bool:
    ui.console.clear(home=True)
    ui.console.line(1)
    ui.line("Publish Data")

    logger.info("*** === Started Staging Data === ***")

    with ui.console.status("Publishing companies..."):
        ops.publish_company()
        msg = Text(" Companies published...", style="grey50 on black")
        ui.console.print(msg)

    with ui.console.status("Publishing annual income..."):
        ops.publish_income_annual()
        msg = Text(" Annual income published...", style="grey50 on black")
        ui.console.print(msg)

    logger.info("*** === Ended Staging Data === ***")

    return True
