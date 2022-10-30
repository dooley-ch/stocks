# *******************************************************************************************
#  File:  _build_sectors_industries.py
#
#  Created: 17-10-2022
#
#  History:
#  17-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['build_sectors_industries']

from loguru import logger

from .. import config
from .. import datastore as ds
from .. import model


# noinspection SqlWithoutWhere
@logger.catch(reraise=True)
def build_sectors_industries() -> bool:
    """
    This function builds the sector and industry tables ready for publishing
    """
    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM zs_industry;")
        cursor.execute("DELETE FROM zs_sector;")

    sector_names = ds.zSimFinIndustries_get_sectors(db_conn)

    sector_rows = 0
    industry_rows = 0

    # Insert default values
    sector_id = ds.zsSectorRecord_insert(model.zsSectorRecord(name='Unknown'), db_conn)
    ds.zsIndustryRecord_insert(model.zsIndustryRecord(name='Unknown', sector_id=sector_id), db_conn)

    # Insert Sectors
    for name in sector_names:
        ds.zsSectorRecord_insert(model.zsSectorRecord(name=name), db_conn)
        sector_rows += 1

    # Insert Industries
    sectors = ds.zsSectorRecord_get_all(db_conn)
    for sector in sectors:
        industry_names = ds.zSimFinIndustries_get_industries_by_sector(sector.name, db_conn)
        if industry_names:
            for name in industry_names:
                ds.zsIndustryRecord_insert(model.zsIndustryRecord(name=name, sector_id=sector.id), db_conn)
                industry_rows += 1

    logger.info(f"Build Sectors & Industries: Sectors - {sector_rows}, Industries - {industry_rows}")

    return True
