# *******************************************************************************************
#  File:  _zs_sector.py
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

__all__ = ['zsSectorRecord_insert', 'zsSectorRecord_get', 'zsSectorRecord_get_all']

import related
import pymysql
from .. model import zsSectorRecord


def zsSectorRecord_insert(record: zsSectorRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("INSERT INTO zs_sector (name) VALUES (%s);", (record.name,))
        return cursor.lastrowid


def zsSectorRecord_get(record_id: int, db_conn: pymysql.Connection) -> zsSectorRecord | None:
    """
    Returns a record from the table based on the given id
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, name, IF(is_active = 1, 'True', 'False') AS is_active FROM zs_sector WHERE (id = %s);", (record_id,))
        row = cursor.fetchone()
        if row:
            record = related.to_model(zsSectorRecord, row)
            return record


def zsSectorRecord_get_all(db_conn: pymysql.Connection) -> list[zsSectorRecord] | None:
    """
    Returns all records from the table
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, name, IF(is_active = 1, 'True', 'False') AS is_active FROM zs_sector;")
        rows = cursor.fetchall()

        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zsSectorRecord, row)
                records.append(record)

            return records
