# *******************************************************************************************
#  File:  _zs_industry.py
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

__all__ = ['zsIndustryRecord_insert', 'zsIndustryRecord_get', 'zsIndustryRecord_get_by_sector']

import related
import pymysql
from .. model import zsIndustryRecord


def zsIndustryRecord_insert(record: zsIndustryRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO zs_industry (name, sector_id) VALUES (%s, %s);", (record.name, record.sector_id))
        return cursor.lastrowid


def zsIndustryRecord_get(record_id: int, db_conn: pymysql.Connection) -> zsIndustryRecord | None:
    """
    Returns a record from the table based on the given id
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, name, sector_id, IF(is_active = 1, 'True', 'False') AS is_active FROM zs_industry 
                            WHERE (id = %s);""", (record_id,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zsIndustryRecord, row)
            return record


def zsIndustryRecord_get_by_sector(sector_id: int, db_conn: pymysql.Connection) -> list[zsIndustryRecord] | None:
    """
    Returns all records from the table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, name, sector_id, IF(is_active = 1, 'True', 'False') AS is_active FROM zs_industry 
                            WHERE (sector_id = %s);""", (sector_id,))
        rows = cursor.fetchall()

        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zsIndustryRecord, row)
                records.append(record)

            return records
