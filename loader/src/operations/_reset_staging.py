# *******************************************************************************************
#  File:  _reset_staging.py
#
#  Created: 01-11-2022
#
#  History:
#  01-11-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['reset_staging_area']

from loguru import logger
from .. import config
from .. import datastore as ds


# noinspection SqlWithoutWhere
@logger.catch(reraise=True)
def reset_staging_area() -> bool:
    """
    This function deletes all the data in the import and staging tables
    """
    db_conn = ds.get_connection(config.database_info())

    with db_conn:
        with db_conn.cursor() as cursor:
            cursor.execute("DELETE FROM zs_peer;")
            cursor.execute("DELETE FROM zs_company;")
            cursor.execute("DELETE FROM zs_industry;")
            cursor.execute("DELETE FROM zs_sector;")

        with db_conn.cursor() as cursor:
            cursor.execute("DELETE FROM z_sp_100;")
            cursor.execute("DELETE FROM z_sp_600;")
            cursor.execute("DELETE FROM z_sp_400;")
            cursor.execute("DELETE FROM z_sp_500;")

        with db_conn.cursor() as cursor:
            cursor.execute("DELETE FROM z_simfin_industries;")
            cursor.execute("DELETE FROM z_simfin_companies;")

        with db_conn.cursor() as cursor:
            cursor.execute("DELETE FROM z_peer_map;")
            cursor.execute("DELETE FROM z_openfigi;")
            cursor.execute("DELETE FROM z_morningstar_profile;")
            cursor.execute("DELETE FROM z_master_ticker;")
            cursor.execute("DELETE FROM z_cik;")

        with db_conn.cursor() as cursor:
            cursor.execute("DELETE FROM z_income_general_annual;")
            cursor.execute("DELETE FROM z_income_general_quarter;")
            cursor.execute("DELETE FROM z_income_bank_annual;")
            cursor.execute("DELETE FROM z_income_bank_quarter;")
            cursor.execute("DELETE FROM z_income_insurance_annual;")
            cursor.execute("DELETE FROM z_income_insurance_quarter;")

        with db_conn.cursor() as cursor:
            cursor.execute("DELETE FROM z_cashflow_general_annual;")
            cursor.execute("DELETE FROM z_cashflow_general_quarter;")
            cursor.execute("DELETE FROM z_cashflow_bank_annual;")
            cursor.execute("DELETE FROM z_cashflow_bank_quarter;")
            cursor.execute("DELETE FROM z_cashflow_insurance_annual;")
            cursor.execute("DELETE FROM z_cashflow_insurance_quarter;")

        with db_conn.cursor() as cursor:
            cursor.execute("DELETE FROM z_balance_sheet_general_annual;")
            cursor.execute("DELETE FROM z_balance_sheet_general_quarter;")
            cursor.execute("DELETE FROM z_balance_sheet_bank_annual;")
            cursor.execute("DELETE FROM z_balance_sheet_bank_quarter;")
            cursor.execute("DELETE FROM z_balance_sheet_insurance_annual;")
            cursor.execute("DELETE FROM z_balance_sheet_insurance_quarter;")

    return True
