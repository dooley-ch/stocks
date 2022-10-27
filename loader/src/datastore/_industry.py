# *******************************************************************************************
#  File:  _industry.py
#
#  Created: 23-09-2022
#
#  History:
#  23-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['industry_insert', 'industry_update', 'industry_delete', 'industry_get', 'industry_get_by_sector',
           'industry_get_audit_records', 'industry_get_audit_records_by_record']

import loguru
import related
import pymysql
from .. import model
from . _errors import DuplicateKeyError


def industry_insert(record: model.Industry, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a new industry record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO industry(name, sector_id) VALUES (%s, %s);",
                           (record.name, record.sector_id))
        except pymysql.err.IntegrityError as e:
            err_no = e.args[0]
            err_msg = e.args[1]

            if err_no == 1062:
                raise DuplicateKeyError(err_msg)
            else:
                loguru.logger.error(f"Failed to insert industry: {record.name}, error: {err_msg}")
            raise

        return cursor.lastrowid


def industry_update(record: model.Industry, db_conn: pymysql.Connection) -> int | None:
    """
    This function updates an industry record, if one exists
    :param record: the record to update
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE industry SET name = %s, sector_id = %s, is_active = %s,  
                            lock_version = lock_version + 1,  updated_at = CURRENT_TIMESTAMP 
                            WHERE (id = %s) AND (lock_version = %s);""",
                       (record.name, record.sector_id, record.is_active, record.id, record.lock_version))
        return cursor.rowcount == 1


def industry_delete(record_id: int, lock_version: int, db_conn: pymysql.Connection) -> int | None:
    """
    This function deletes records based on the provided parameters
    :param record_id: the id of the record to delete
    :param lock_version: the version flag of the record to delete
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM industry WHERE (id = %s) AND (lock_version = %s);", (record_id, lock_version))
        return cursor.rowcount == 1


def industry_get(record_id: int, db_conn: pymysql.Connection) -> model.Industry | None:
    """
    This function returns an Industry record for the given parameters, if one exists
    :param record_id: the id of the record to load
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, name, sector_id, IF(is_active = 1, 'True', 'False') AS is_active, 
                            lock_version, created_at, updated_at  FROM industry WHERE (id = %s )""", (record_id,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(model.Industry, data)
            return record


def industry_get_by_sector(sector_id: int, db_conn: pymysql.Connection) -> list[model.Industry] | None:
    """
    This function returns the industries associated with the given sector id
    :param sector_id: The sector id to filter by
    :param db_conn: the database_old connection to use
    :return: list of industries if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, name, sector_id, IF(is_active = 1, 'True', 'False') AS is_active, 
                            lock_version, created_at, updated_at FROM industry WHERE (sector_id = %s )""", (sector_id,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(model.Industry, row)
                records.append(record)
            return records


def industry_get_audit_records(db_conn: pymysql.Connection) -> list[model.XxxIndustry] | None:
    """
    This function returns all audit records for the table
    :param db_conn: the database_old connection to use
    :return: list of audit records, if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, logged_at, audit_action, record_id, name, sector_id, 
                                IF(is_active = 1, 'True', 'False') AS is_active, lock_version  FROM xxx_industry;""")
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxIndustry, row)
                records.append(record)

            return records


def industry_get_audit_records_by_record(record_id: int, db_conn: pymysql.Connection) -> list[model.XxxIndustry] | None:
    """
    This function returns all audit records for a given record
    :param record_id: The id for the record to report on
    :param db_conn: the database_old connection to use
    :return: list of audit records, if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, logged_at, audit_action, record_id, name, sector_id, 
                                IF(is_active = 1, 'True', 'False') AS is_active, lock_version FROM xxx_industry 
                                WHERE (record_id = %s);""", (record_id,))
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxIndustry, row)
                records.append(record)

            return records
