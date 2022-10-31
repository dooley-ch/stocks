# *******************************************************************************************
#  File:  _core.py
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
__version__ = "1.0.1"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['main']

import atexit

from loguru import logger
import click
from rich.traceback import install as rich_traceback
from .. import ui
from ..config import configure_logging
from ._config import config as do_config
from ._stage import stage as do_stage
from ._publish import publish as do_publish
from ._import import import_data as do_import_data


@click.group(context_settings={'help_option_names': ('-h', '--help')})
@click.version_option(__version__, '--version', '-v')
def app(**kwargs) -> None:
    """
    This application handles the ETL process for the stocks database
    """
    pass


@app.command("import")
@click.pass_context
def import_data(ctx: click.Context) -> None:
    """
    Download & import data
    """
    if do_import_data():
        ui.success_message('Data imported successfully')
        ctx.exit(0)
    else:
        ui.error_message('Failed to import data, see the log for details')
        ctx.exit(1)


@app.command("stage")
@click.pass_context
def stage(ctx: click.Context) -> None:
    """
    Parse data for publishing
    """
    if do_stage():
        ui.success_message('Data staged successfully')
        ctx.exit(0)
    else:
        ui.error_message('Failed to stage data, see the log for details')
        ctx.exit(1)


@app.command("publish")
@click.pass_context
def publish_data(ctx: click.Context) -> None:
    """
    Publish the company data
    """
    if do_publish():
        ui.success_message('Publish data successfully')
        ctx.exit(0)
    else:
        ui.error_message('Failed to publish data, see the log for details')
        ctx.exit(1)


@app.command("config")
@click.pass_context
def config(ctx: click.Context) -> None:
    """
    Set configuration data
    """
    if do_config():
        ui.success_message('Configuration completed')
        ctx.exit(0)
    else:
        ui.error_message('Failed to configure application, see the log for details')
        ctx.exit(1)


def exit_routine() -> None:
    """
    Logs the termination of the application
    """
    # noinspection PyBroadException
    try:
        logger.info("<========== E N D ==========>")
    except:
        ui.system_message('Failed to log application exit!')


def main() -> None:
    # Configure custom stack trace
    rich_traceback(show_locals=True, suppress=[click])

    # Set up logging
    configure_logging('loader.log')
    atexit.register(exit_routine)

    logger.info("<========== S T A R T E D ==========>")

    # Launch the application
    app()
