# *******************************************************************************************
#  File:  _config.py
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

__all__ = ['config']

from rich.prompt import Prompt, Confirm
from rich.table import Table
from .. import config as cfg
from .. import ui as ui


def config() -> bool:
    config_data = cfg.load_config(cfg.config_file())

    ui.console.clear(home=True)
    ui.console.line(1)
    ui.line("Enter Configuration")

    open_figi = config_data.keys.openfigi
    if not open_figi:
        open_figi = 'None'

    simfin = config_data.keys.simfin
    if not simfin:
        simfin = 'None'

    user = config_data.database.user if config_data.database.user else 'None'
    password = config_data.database.password if config_data.database.user else 'None'
    database = config_data.database.database if config_data.database.database else 'None'
    host = config_data.database.host
    port = config_data.database.port


    open_figi = Prompt.ask("Enter OpenFigi api key", console=ui.console, show_default=True, default=open_figi)
    simfin = Prompt.ask("Enter SimFin api key", console=ui.console, show_default=True, default=simfin)

    user = Prompt.ask("Enter Database user", console=ui.console, show_default=True, default=user)
    password = Prompt.ask("Enter Database Password", console=ui.console, show_default=True, default=password)
    database = Prompt.ask("Enter Database Name", console=ui.console, show_default=True, default=database)
    host = Prompt.ask("Enter Database Host", console=ui.console, show_default=True, default=host)
    port = Prompt.ask("Enter Database Port", console=ui.console, show_default=True, default=str(port))


    table = Table(title="Config Parameters", style="table-style", show_header=False, show_footer=False,
                  border_style="table-border-style", title_style="table-title-style")
    table.add_column("Parameter", justify="left", no_wrap=True, width=30)
    table.add_column("Entered Value", justify="left", no_wrap=True, width=30)
    table.add_row("OpenFIGI Key", open_figi)
    table.add_row("SimFin Key", simfin)
    table.add_row("Database User", user)
    table.add_row("Database Password", password)
    table.add_row("Database Name", database)
    table.add_row("Host", host)
    table.add_row("Port", port)

    ui.console.line(2)
    ui.console.print(table)
    ui.console.line(1)
    confirm = Confirm.ask('Are you sure you wish to save the new parameters?', default='y')

    if confirm:
        config_data.keys.simfin = simfin
        config_data.keys.openfigi = open_figi

        config_data.database.user = user
        config_data.database.password = password
        config_data.database.database = database
        config_data.database.host = host
        config_data.database.port = port

        cfg.save_config(config_data, cfg.config_file())

        ui.success_message('Values saved.')

    return True
