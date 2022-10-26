# *******************************************************************************************
#  File:  ui.py
#
#  Created: 30-08-2022
#
#  History:
#  30-08-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['console', 'message', 'error_message', 'warning_message', 'success_message', 'system_message',
           'confirm_message', 'line', 'done', 'not_done']

from rich.console import Console
from rich.prompt import Confirm
from rich.text import Text
from rich.theme import Theme
from rich.rule import Rule


theme = Theme({
    "normal_message": "bright_white on black",
    "error_message": "bright_red on black",
    "success_message": "light_green on black",
    "system_message": "bright_blue on black",
    "confirm_message": "bright_white on black",
    "warning_message": "orange3 on black",
    "table-style": "bright_white on black",
    "table-cell-style": "bright_white on black",
    "table-header-style": "bold bright_blue",
    "table-title-style": "bold bright_blue",
    "table-border-style": "bright_blue on black",
    "table-odd-row-style": "dark_sea_green3 on black",
    "table-even-row-style": "bright_blue on black",
    "line-normal-style": "dim",
    "progress-bar-column-style": "hot_pink2",
    "progress-bar-column-complete-style": "bright_blue",
    "progress-bar-column-finished_style": "bright_green",
    "progress-text-column-style": "bright_blue"
})
console = Console(theme=theme)
done = Text('✔︎', style="green on black")
not_done = Text('✘', style="red on black")


def line(msg: str, style: str = "line-normal-style") -> None:
    """
    This function draws a line on the terminal
    """
    rule = Rule(title=Text(msg, style=style), style=style)
    console.line(1)
    console.print(rule)
    console.line(1)


def _message(value: str, text_style: str, clear: bool, pad: bool) -> None:
    """
    Internal function to display a message on the console
    """
    if clear:
        console.clear()
    if pad:
        console.line(1)

    msg = Text(value, style=text_style)
    console.print(msg)

    if pad:
        console.line(1)


# noinspection GrazieInspection
def message(value: str, clear: bool = False, pad: bool = True) -> None:
    """
    This function displays a normal message on the console

    :param value: the text to display
    :param clear: flag to indicate if the console should be cleared first
    :param pad: flag to indicate if the message should be preceded and succeeded by a blank line

    :return: None
    """
    _message(value, "normal_message", clear, pad)


# noinspection GrazieInspection
def error_message(value: str, clear: bool = False, pad: bool = True) -> None:
    """
    This function displays an error message on the console

    :param value: the text to display
    :param clear: flag to indicate if the console should be cleared first
    :param pad: flag to indicate if the message should be preceded and succeeded by a blank line

    :return: None
    """
    _message(value, "error_message", clear, pad)


def warning_message(value: str, clear: bool = False, pad: bool = True) -> None:
    """
    This function displays a warning message on the console

    :param value: the text to display
    :param clear: flag to indicate if the console should be cleared first
    :param pad: flag to indicate if the message should be preceded and succeeded by a blank line

    :return: None
    """
    _message(value, "warning_message", clear, pad)


# noinspection GrazieInspection
def success_message(value: str, clear: bool = False, pad: bool = True) -> None:
    """
    This function displays a success message on the console

    :param value: the text to display
    :param clear: flag to indicate if the console should be cleared first
    :param pad: flag to indicate if the message should be preceded and succeeded by a blank line

    :return: None
    """
    _message(value, "success_message", clear, pad)


# noinspection GrazieInspection
def system_message(value: str, clear: bool = False, pad: bool = True) -> None:
    """
    This function displays a system message on the console

    :param value: the text to display
    :param clear: flag to indicate if the console should be cleared first
    :param pad: flag to indicate if the message should be preceded and succeeded by a blank line

    :return: None
    """
    _message(value, "system_message", clear, pad)


# noinspection GrazieInspection
def confirm_message(value: str, default: bool, clear: bool = False, pad: bool = True) -> bool:
    """
    This function ask the user to confirm or reject the execution of an action

    :param value: the text to display
    :param default: the default response if the user just hits enter
    :param clear: flag to indicate if the console should be cleared first
    :param pad: flag to indicate if the message should be preceded and succeeded by a blank line

    :return: None
    """
    if clear:
        console.clear()
    if pad:
        console.line(1)

    msg = Text(value, style="confirm_message")
    return Confirm.ask(msg, default=default, show_default=True)
