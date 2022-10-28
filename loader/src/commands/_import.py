# *******************************************************************************************
#  File:  _import.py
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

__all__ = ['import_data']

from loguru import logger
from rich.progress import Progress

from .. import operations as ops
from .. import ui


def import_data() -> bool:
    """
    This function imports the data into the staging tables
    :return:
    """
    ui.console.clear(home=True)
    ui.console.line(1)
    ui.line("Import Data")

    logger.info("*** === Started Importing Data === ***")

    with Progress() as progress:
        sp_100_task = progress.add_task("[dodger_blue1]Importing S&P 100 index...", total=1, visible=False)
        sp_600_task = progress.add_task("[dodger_blue1]Importing S&P 600 index...", total=1, visible=False)
        sp_400_task = progress.add_task("[dodger_blue1]Importing S&P 400 index...", total=1, visible=False)
        sp_500_task = progress.add_task("[dodger_blue1]Importing S&P 500 index...", total=1, visible=False)

        cik_task = progress.add_task("[dark_orange3]Importing CIK file...", total=1, visible=False)
        peers_task = progress.add_task("[dark_orange3]Importing Peers Map...", total=1, visible=False)

        simfin_industries_task = progress.add_task("[chartreuse2]Importing SimFin Industries...", total=1, visible=False)
        simfin_companies_task = progress.add_task("[chartreuse2]Importing SimFin Companies...", total=1, visible=False)

        simfin_income_general_annual_task = progress.add_task("[medium_violet_red]Importing SimFin Annual General Income Statements...", total=1, visible=False)
        simfin_balance_sheet_general_annual_task = progress.add_task("[medium_violet_red]Importing SimFin Annual General Balance Sheets...", total=1, visible=False)
        simfin_cashflow_general_annual_task = progress.add_task("[medium_violet_red]Importing SimFin Annual General Cashflow Statements...", total=1, visible=False)
        simfin_income_general_quarter_task = progress.add_task("[medium_violet_red]Importing SimFin Quarterly General Income Statements...", total=1, visible=False)
        simfin_balance_sheet_general_quarter_task = progress.add_task("[medium_violet_red]Importing SimFin Quarterly General Balance Sheets...", total=1, visible=False)
        simfin_cashflow_general_quarter_task = progress.add_task("[medium_violet_red]Importing SimFin Quarterly General Cashflow Statements...", total=1, visible=False)

        # simfin_income_bank_annual_task = progress.add_task("Importing SimFin Annual Bank Income Statements...", total=500)
        # simfin_balance_sheet_bank_annual_task = progress.add_task("Importing SimFin Annual Bank Balance Sheets...", total=500)
        # simfin_cashflow_bank_annual_task = progress.add_task("Importing SimFin Annual Bank Cashflow Statements...", total=500)
        # simfin_income_bank_quarter_task = progress.add_task("Importing SimFin Quarterly Bank Income Statements...", total=500)
        # simfin_balance_sheet_bank_quarter_task = progress.add_task("Importing SimFin Quarterly Bank Balance Sheets...", total=500)
        # simfin_cashflow_bank_quarter_task = progress.add_task("Importing SimFin Quarterly Bank Cashflow Statements...", total=500)
        #
        # simfin_income_insurance_annual_task = progress.add_task("Importing SimFin Annual Insurance Income Statements...", total=500)
        # simfin_balance_sheet_insurance_annual_task = progress.add_task("Importing SimFin Annual Insurance Balance Sheets...", total=500)
        # simfin_cashflow_insurance_annual_task = progress.add_task("Importing SimFin Annual Insurance Cashflow Statements...", total=500)
        # simfin_income_insurance_quarter_task = progress.add_task("Importing SimFin Quarterly Insurance Income Statements...", total=500)
        # simfin_balance_sheet_insurance_quarter_task = progress.add_task("Importing SimFin Quarterly Insurance Balance Sheets...", total=500)
        # simfin_cashflow_insurance_quarter_task = progress.add_task("Importing SimFin Quarterly Insurance Cashflow Statements...", total=500)

        ops.import_sp_100_file(progress, sp_100_task)
        ops.import_sp_600_file(progress, sp_600_task)
        ops.import_sp_400_file(progress, sp_400_task)
        ops.import_sp_500_file(progress, sp_500_task)

        ops.import_cik_file(progress, cik_task)
        ops.import_peers_file(progress, peers_task)

        ops.import_industries_file(progress, simfin_industries_task)
        ops.import_companies_file(progress, simfin_companies_task)

        ops.import_income_general_annual_file(progress, simfin_income_general_annual_task)
        ops.import_cashflow_general_annual_file(progress, simfin_cashflow_general_annual_task)
        ops.import_income_general_quarter_file(progress, simfin_income_general_quarter_task)
        ops.import_cashflow_general_quarter_file(progress, simfin_cashflow_general_quarter_task)

        # TODO - Add code to build master list

    logger.info("*** === Ended Importing Data === ***")

    return True
