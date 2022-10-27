# *******************************************************************************************
#  File:  config.py
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

__all__ = ['application_folder', 'config_file', 'logs_folder', 'data_folder', 'configure_logging', 'load_config',
           'save_config', 'ApiKeys', 'ConfigFile', 'openfigi_key', 'simfin_key',
           'CIK_FILE', 'SP_100_FILE', 'SP_600_FILE', 'SP_400_FILE', 'SP_500_FILE', 'SIMFIN_BALANCE_BANK_ANNUAL_FILE',
           'SIMFIN_BALANCE_BANK_QUARTER_FILE', 'SIMFIN_BALANCE_GENERAL_ANNUAL_FILE',
           'SIMFIN_BALANCE_GENERAL_QUARTER_FILE',
           'SIMFIN_BALANCE_INSURANCE_ANNUAL_FILE', 'SIMFIN_BALANCE_INSURANCE_QUARTER_FILE',
           'SIMFIN_CASHFLOW_BANK_ANNUAL_FILE', 'SIMFIN_CASHFLOW_BANK_QUARTER_FILE',
           'SIMFIN_CASHFLOW_GENERAL_ANNUAL_FILE',
           'SIMFIN_CASHFLOW_GENERAL_QUARTER_FILE', 'SIMFIN_CASHFLOW_INSURANCE_ANNUAL_FILE',
           'SIMFIN_CASHFLOW_INSURANCE_QUARTER_FILE', 'SIMFIN_INCOME_BANK_ANNUAL_FILE',
           'SIMFIN_INCOME_BANK_QUARTER_FILE',
           'SIMFIN_INCOME_GENERAL_ANNUAL_FILE', 'SIMFIN_INCOME_GENERAL_QUARTER_FILE',
           'SIMFIN_INCOME_INSURANCE_ANNUAL_FILE',
           'SIMFIN_INCOME_INSURANCE_QUARTER_FILE', 'SIMFIN_COMPANIES_FILE', 'SIMFIN_INDUSTRIES_FILE', 'PEERS_FILE']

import pathlib
import sys
import click
import related
import loguru

CIK_FILE = "cik.csv"

SP_100_FILE = "sp_100.csv"
SP_600_FILE = "sp_600.csv"
SP_400_FILE = "sp_400.csv"
SP_500_FILE = "sp_500.csv"

SIMFIN_BALANCE_BANK_ANNUAL_FILE = "simfin_balance_bank_annual.csv"
SIMFIN_BALANCE_BANK_QUARTER_FILE = "simfin_balance_bank_quarter.csv"
SIMFIN_BALANCE_GENERAL_ANNUAL_FILE = "simfin_balance_general_annual.csv"
SIMFIN_BALANCE_GENERAL_QUARTER_FILE = "simfin_balance_general_quarter.csv"
SIMFIN_BALANCE_INSURANCE_ANNUAL_FILE = "simfin_balance_insurance_annual.csv"
SIMFIN_BALANCE_INSURANCE_QUARTER_FILE = "simfin_balance_insurance_quarter.csv"

SIMFIN_CASHFLOW_BANK_ANNUAL_FILE = "simfin_cashflow_bank_annual.csv"
SIMFIN_CASHFLOW_BANK_QUARTER_FILE = "simfin_cashflow_bank_quarter.csv"
SIMFIN_CASHFLOW_GENERAL_ANNUAL_FILE = "simfin_cashflow_general_annual.csv"
SIMFIN_CASHFLOW_GENERAL_QUARTER_FILE = "simfin_cashflow_general_quarter.csv"
SIMFIN_CASHFLOW_INSURANCE_ANNUAL_FILE = "simfin_cashflow_insurance_annual.csv"
SIMFIN_CASHFLOW_INSURANCE_QUARTER_FILE = "simfin_cashflow_insurance_quarter.csv"

SIMFIN_INCOME_BANK_ANNUAL_FILE = "simfin_income_bank_annual.csv"
SIMFIN_INCOME_BANK_QUARTER_FILE = "simfin_income_bank_quarter.csv"
SIMFIN_INCOME_GENERAL_ANNUAL_FILE = "simfin_income_general_annual.csv"
SIMFIN_INCOME_GENERAL_QUARTER_FILE = "simfin_income_general_quarter.csv"
SIMFIN_INCOME_INSURANCE_ANNUAL_FILE = "simfin_income_insurance_annual.csv"
SIMFIN_INCOME_INSURANCE_QUARTER_FILE = "simfin_income_insurance_quarter.csv"

SIMFIN_COMPANIES_FILE = "simfin_companies.csv"
SIMFIN_INDUSTRIES_FILE = "simfin_industries.csv"

PEERS_FILE = 'peers.json'


def application_folder() -> pathlib.Path:
    """
    This function returns the folder where the application's data is stored
    """
    folder = pathlib.Path(click.get_app_dir(app_name="developer_notes")).joinpath("stocks-loader")
    folder.mkdir(parents=True, exist_ok=True)

    return folder


def config_file() -> pathlib.Path:
    """
    This function returns the config file name
    """
    return application_folder().joinpath('config.yaml')


@related.mutable
class ApiKeys:
    openfigi: str = related.StringField(default='')
    simfin: str = related.StringField(default='')


@related.immutable
class ConfigFile:
    keys: ApiKeys = related.ChildField(ApiKeys, default=ApiKeys())


def load_config(file: pathlib.Path) -> ConfigFile:
    """
    This function loads and returns the config file data
    """
    if not file.exists():
        return ConfigFile()

    with file.open('r') as hFile:
        content = hFile.read()

    data = related.from_yaml(content)
    obj = related.to_model(ConfigFile, data)
    return obj


def save_config(model: ConfigFile, file: pathlib.Path) -> None:
    """
    This function saves the application config information
    """
    data = related.to_yaml(model, suppress_empty_values=True, suppress_map_key_values=True).strip()

    with file.open('w') as hFile:
        hFile.write(data)


def logs_folder() -> pathlib.Path:
    """
    This function returns the location of the logs folder
    """
    folder = pathlib.Path(__file__).parent.parent.joinpath('logs')
    folder.mkdir(parents=True, exist_ok=True)

    return folder


def configure_logging(log_name: str) -> None:
    """
    This function configures application logging
    """
    log_file = logs_folder().joinpath(log_name)

    file_format: str = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {function: ^15} | {file: ^15} | {line: >3} | {" \
                       "message}"
    console_format: str = "<red>{time:HH:mm:ss} {level} {function}() {file}:{line} - {message}</red>"

    loguru.logger.remove()

    loguru.logger.add(sys.stderr, format=console_format, level="ERROR", colorize=True)
    loguru.logger.add(log_file, rotation='1 day', retention='5 days', compression='zip', level='INFO', backtrace=True,
                      diagnose=True, format=file_format)


def openfigi_key() -> str:
    """
    This function returns the openfigi key
    """
    data = load_config(config_file())
    return data.keys.openfigi


def simfin_key() -> str:
    """
    This function returns the simfin key
    """
    data = load_config(config_file())
    return data.keys.openfigi


def data_folder() -> pathlib.Path:
    """
    This function returns the location of the logs folder
    """
    folder = pathlib.Path(__file__).parent.parent.joinpath('data')
    folder.mkdir(parents=True, exist_ok=True)

    return folder
