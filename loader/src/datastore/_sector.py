# *******************************************************************************************
#  File:  _sector.py
#
#  Created: 22-09-2022
#
#  History:
#  22-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['sector_insert', 'sector_update', 'sector_delete', 'sector_get', 'sector_get_all', 'sector_get_by_name',
           'sector_get_audit_records', 'sector_get_audit_records_by_record']

import loguru
import related
import pymysql
from .. import model
from . _errors import DuplicateKeyError


def sector_insert(record: model.Sector, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a new sector record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO sector(name) VALUES (%s);", (record.name,))
        except pymysql.err.IntegrityError as e:
            err_no = e.args[0]
            err_msg = e.args[1]

            if err_no == 1062:
                raise DuplicateKeyError(err_msg)
            else:
                loguru.logger.error(f"Failed to insert sector: {record.name}, error: {err_msg}")
            raise

        return cursor.lastrowid


def sector_update(record: model.Sector, db_conn: pymysql.Connection) -> bool:
    """
    This function updates a sector record, if one exists
    :param record: the record to update
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE sector SET name = %s, is_active = %s, lock_version = lock_version + 1, 
                            updated_at = CURRENT_TIMESTAMP WHERE (id = %s) AND (lock_version = %s);""",
                       (record.name, record.is_active, record.id, record.lock_version))
        return cursor.rowcount == 1


def sector_delete(record_id: int, lock_version: int, db_conn: pymysql.Connection) -> bool:
    """
    This function deletes a record based on the provided parameters
    :param record_id: the id of the record to delete
    :param lock_version: the version flag of the record to delete
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM sector WHERE (id = %s) AND (lock_version = %s);", (record_id, lock_version))
        return cursor.rowcount == 1


def sector_get(record_id: int, db_conn: pymysql.Connection) -> model.Sector | None:
    """
    This function returns a Sector record for the given parameters, if one exists
    :param record_id: the id of the record to load
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, name, IF(is_active = 1, 'True', 'False') AS is_active, lock_version, 
                            created_at, updated_at FROM sector WHERE (id = %s )""", (record_id,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(model.Sector, data)
            return record


def sector_get_all(db_conn: pymysql.Connection) -> list[model.Sector] | None:
    """
    This function returns a Sector record for the given parameters, if one exists
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, name, IF(is_active = 1, 'True', 'False') AS is_active, lock_version, 
                            created_at, updated_at FROM sector ORDER BY name;""")
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.Sector, row)
                records.append(record)

            return records


def sector_get_by_name(name: str, db_conn: pymysql.Connection) -> model.Sector | None:
    """
    This function returns a Sector record for the given parameters, if one exists
    :param name: the name of the record to load
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, name, IF(is_active = 1, 'True', 'False') AS is_active, lock_version, 
                            created_at, updated_at FROM sector WHERE (name = %s )""", (name,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(model.Sector, data)
            return record


def sector_get_audit_records(db_conn: pymysql.Connection) -> list[model.XxxSector] | None:
    """
    This function returns all audit records for the table
    :param db_conn: the database_old connection to use
    :return: list of audit records, if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, logged_at, audit_action, record_id, name, 
                                IF(is_active = 1, 'True', 'False') AS is_active, lock_version  FROM xxx_sector;""")
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxSector, row)
                records.append(record)

            return records


def sector_get_audit_records_by_record(record_id: int, db_conn: pymysql.Connection) -> list[model.XxxSector] | None:
    """
    This function returns all audit records for a given record
    :param record_id: The id for the record to report on
    :param db_conn: the database_old connection to use
    :return: list of audit records, if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, logged_at, audit_action, record_id, name, 
                                IF(is_active = 1, 'True', 'False') AS is_active, lock_version  
                                FROM xxx_sector WHERE (record_id = %s);""", (record_id,))
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxSector, row)
                records.append(record)

            return records
