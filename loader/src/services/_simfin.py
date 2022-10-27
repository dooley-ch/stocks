# *******************************************************************************************
#  File:  _simfin.py
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

__all__ = ['download_simfin_companies', 'download_simfin_industries', 'download_simfin_prices',
           'download_simfin_income_general_annual', 'download_simfin_income_bank_annual',
           'download_simfin_income_insurance_annual', 'download_simfin_income_general_quarter',
           'download_simfin_income_bank_quarter', 'download_simfin_income_insurance_quarter',
           'download_simfin_cashflow_general_annual', 'download_simfin_cashflow_bank_annual',
           'download_simfin_cashflow_insurance_annual', 'download_simfin_cashflow_general_quarter',
           'download_simfin_cashflow_bank_quarter', 'download_simfin_cashflow_insurance_quarter',
           'download_simfin_balance_general_annual', 'download_simfin_balance_bank_annual',
           'download_simfin_balance_insurance_annual', 'download_simfin_balance_general_quarter',
           'download_simfin_balance_bank_quarter', 'download_simfin_balance_insurance_quarter']

from enum import Enum
from pathlib import Path
import zipfile
import requests
from loguru import logger
from .. import config


class _Dataset(str, Enum):
    Companies = "companies"
    Industries = "industries"
    IncomeGeneral = "income"
    IncomeBanks = "income-banks"
    IncomeInsurance = "income-insurance"
    BalanceSheetGeneral = "balance"
    BalanceSheetBanks = "balance-banks"
    BalanceSheetInsurance = "balance-insurance"
    CashflowGeneral = "cashflow"
    CashflowBanks = "cashflow-banks"
    CashflowInsurance = "cashflow-insurance"
    SharePrice = "shareprices"


class _Variant(str, Enum):
    Null = "null"
    Annual = "annual"
    Quarterly = "quarterly"
    Daily = "daily"
    Latest = "latest"


_simfin_url = 'https://simfin.com/api/bulk/bulk.php'


def _get_params(dataset: _Dataset, variant: _Variant, key: str) -> dict[str, str]:
    """
    This function returns the parameters needed to download a dataset from SimFin
    """
    return {
        "dataset": dataset.value,
        "variant": variant.value,
        "market": "us",
        "api-key": key
    }


def _download_file(params: dict[str, str], folder: Path, extract_file: str, data_file: str) -> bool:
    """
    This function downloads and extracts a SimFin file
    """
    zip_file = folder.joinpath('simfin_data.zip')
    extracted_file = folder.joinpath(extract_file)
    data_file = folder.joinpath(data_file)

    response = requests.get(_simfin_url, params)

    if response.status_code != 200:
        logger.error(f"Failed to download {data_file} file: {response.status_code} - {response.text}")
        return False

    if zip_file.exists():
        zip_file.unlink()
    if data_file.exists():
        data_file.unlink()

    with zip_file.open('wb') as file:
        file.write(response.content)

    with zipfile.ZipFile(zip_file, 'r') as zip_handle:
        zip_handle.extractall(folder)

    if extracted_file.exists():
        extracted_file.rename(data_file)
        zip_file.unlink()
        return True


@logger.catch(reraise=True)
def download_simfin_companies(folder: Path, key: str) -> None:
    """
    This function downloads the SimFin companies file
    """
    params = _get_params(_Dataset.Companies, _Variant.Null, key)
    _download_file(params, folder, 'us-companies.csv', config.SIMFIN_COMPANIES_FILE)


@logger.catch(reraise=True)
def download_simfin_industries(folder: Path, key: str) -> None:
    """
    This function downloads the SimFin industries file
    """
    params = _get_params(_Dataset.Industries, _Variant.Null, key)
    del params['market']

    _download_file(params, folder, 'industries.csv', config.SIMFIN_INDUSTRIES_FILE)


def download_simfin_income_general_annual(folder: Path, key: str) -> None:
    """
    This function download the SimFin general income annual
    """
    params = _get_params(_Dataset.IncomeGeneral, _Variant.Annual, key)
    _download_file(params, folder, 'us-income-annual.csv', 'simfin_income_general_annual.csv')


@logger.catch(reraise=True)
def download_simfin_income_bank_annual(folder: Path, key: str) -> None:
    """
    This function download the SimFin bank income annual
    """
    params = _get_params(_Dataset.IncomeBanks, _Variant.Annual, key)
    _download_file(params, folder, 'us-income-banks-annual.csv', 'simfin_income_bank_annual.csv')


def download_simfin_income_insurance_annual(folder: Path, key: str) -> None:
    """
    This function download the SimFin insurance income annual
    """
    params = _get_params(_Dataset.IncomeInsurance, _Variant.Annual, key)
    _download_file(params, folder, 'us-income-insurance-annual.csv', 'simfin_income_insurance_annual.csv')


@logger.catch(reraise=True)
def download_simfin_income_general_quarter(folder: Path, key: str) -> None:
    """
    This function download the SimFin general income quarter
    """
    params = _get_params(_Dataset.IncomeGeneral, _Variant.Quarterly, key)
    _download_file(params, folder, 'us-income-quarterly.csv', 'simfin_income_general_quarter.csv')


def download_simfin_income_bank_quarter(folder: Path, key: str) -> None:
    """
    This function download the SimFin general income quarter
    """
    params = _get_params(_Dataset.IncomeBanks, _Variant.Quarterly, key)
    _download_file(params, folder, 'us-income-banks-quarterly.csv', 'simfin_income_bank_quarter.csv')


@logger.catch(reraise=True)
def download_simfin_income_insurance_quarter(folder: Path, key: str) -> None:
    """
    This function download the SimFin general income quarter
    """
    params = _get_params(_Dataset.IncomeInsurance, _Variant.Quarterly, key)
    _download_file(params, folder, 'us-income-insurance-quarterly.csv', 'simfin_income_insurance_quarter.csv')


@logger.catch(reraise=True)
def download_simfin_balance_general_annual(folder: Path, key: str) -> None:
    """
    This function download the SimFin general balance sheet annual
    """
    params = _get_params(_Dataset.BalanceSheetGeneral, _Variant.Annual, key)
    _download_file(params, folder, 'us-balance-annual.csv', 'simfin_balance_general_annual.csv')


def download_simfin_balance_bank_annual(folder: Path, key: str) -> None:
    """
    This function download the SimFin banks balance sheet annual
    """
    params = _get_params(_Dataset.BalanceSheetBanks, _Variant.Annual, key)
    _download_file(params, folder, 'us-balance-banks-annual.csv', 'simfin_balance_bank_annual.csv')


@logger.catch(reraise=True)
def download_simfin_balance_insurance_annual(folder: Path, key: str) -> None:
    """
    This function download the SimFin insurance balance sheet annual
    """
    params = _get_params(_Dataset.BalanceSheetInsurance, _Variant.Annual, key)
    _download_file(params, folder, 'us-balance-insurance-annual.csv', 'simfin_balance_insurance_annual.csv')


@logger.catch(reraise=True)
def download_simfin_balance_general_quarter(folder: Path, key: str) -> None:
    """
    This function download the SimFin general balance sheet annual
    """
    params = _get_params(_Dataset.BalanceSheetGeneral, _Variant.Quarterly, key)
    _download_file(params, folder, 'us-balance-quarterly.csv', 'simfin_balance_general_quarter.csv')


@logger.catch(reraise=True)
def download_simfin_balance_bank_quarter(folder: Path, key: str) -> None:
    """
    This function download the SimFin banks balance sheet annual
    """
    params = _get_params(_Dataset.BalanceSheetBanks, _Variant.Quarterly, key)
    _download_file(params, folder, 'us-balance-banks-quarterly.csv', 'simfin_balance_bank_quarter.csv')


@logger.catch(reraise=True)
def download_simfin_balance_insurance_quarter(folder: Path, key: str) -> None:
    """
    This function download the SimFin insurance balance sheet annual
    """
    params = _get_params(_Dataset.BalanceSheetInsurance, _Variant.Quarterly, key)
    _download_file(params, folder, 'us-balance-insurance-quarterly.csv', 'simfin_balance_insurance_quarter.csv')


def download_simfin_cashflow_general_annual(folder: Path, key: str) -> None:
    """
    This function download the SimFin general cashflow annual
    """
    params = _get_params(_Dataset.CashflowGeneral, _Variant.Annual, key)
    _download_file(params, folder, 'us-cashflow-annual.csv', 'simfin_cashflow_general_annual.csv')


@logger.catch(reraise=True)
def download_simfin_cashflow_bank_annual(folder: Path, key: str) -> None:
    """
    This function download the SimFin banks cashflow annual
    """
    params = _get_params(_Dataset.CashflowBanks, _Variant.Annual, key)
    _download_file(params, folder, 'us-cashflow-banks-annual.csv', 'simfin_cashflow_bank_annual.csv')


@logger.catch(reraise=True)
def download_simfin_cashflow_insurance_annual(folder: Path, key: str) -> None:
    """
    This function download the SimFin insurance cashflow annual
    """
    params = _get_params(_Dataset.CashflowInsurance, _Variant.Annual, key)
    _download_file(params, folder, 'us-cashflow-insurance-annual.csv', 'simfin_cashflow_insurance_annual.csv')


def download_simfin_cashflow_general_quarter(folder: Path, key: str) -> None:
    """
    This function download the SimFin general cashflow quarter
    """
    params = _get_params(_Dataset.CashflowGeneral, _Variant.Quarterly, key)
    _download_file(params, folder, 'us-cashflow-quarterly.csv', 'simfin_cashflow_general_quarter.csv')


@logger.catch(reraise=True)
def download_simfin_cashflow_bank_quarter(folder: Path, key: str) -> None:
    """
    This function download the SimFin banks cashflow quarter
    """
    params = _get_params(_Dataset.CashflowBanks, _Variant.Quarterly, key)
    _download_file(params, folder, 'us-cashflow-banks-quarterly.csv', 'simfin_cashflow_bank_quarter.csv')


def download_simfin_cashflow_insurance_quarter(folder: Path, key: str) -> None:
    """
    This function download the SimFin insurance cashflow quarter
    """
    params = _get_params(_Dataset.CashflowInsurance, _Variant.Quarterly, key)
    _download_file(params, folder, 'us-cashflow-insurance-quarterly.csv', 'simfin_cashflow_insurance_quarter.csv')


@logger.catch(reraise=True)
def download_simfin_prices(folder: Path, key: str) -> None:
    """
    This function downloads the SimFin cashflow files
    """
    params = _get_params(_Dataset.SharePrice, _Variant.Daily, key)
    _download_file(params, folder, 'us-shareprices-daily.csv', 'simfin_prices.csv')
