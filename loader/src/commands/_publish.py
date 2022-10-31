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

__all__ = ['publish']

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

    with ui.console.status("Publishing annual income statements..."):
        ops.publish_income_annual()
        msg = Text(" Annual income published...", style="grey50 on black")
        ui.console.print(msg)

    with ui.console.status("Publishing annual balance sheets..."):
        ops.publish_balance_sheet_annual()
        msg = Text(" Annual balance sheets published...", style="grey50 on black")
        ui.console.print(msg)

    with ui.console.status("Publishing cashflow figures..."):
        ops.publish_cashflow_figures()
        msg = Text(" Annual cashflow figures published...", style="grey50 on black")
        ui.console.print(msg)

    with ui.console.status("Publishing quarter figures..."):
        ops.publish_quarters()
        msg = Text(" Quarter figures published...", style="grey50 on black")
        ui.console.print(msg)

    logger.info("*** === Ended Staging Data === ***")

    return True
