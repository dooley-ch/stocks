# *******************************************************************************************
#  File:  _peer.py
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

__all__ = ['peer_insert', 'peer_update', 'peer_delete', 'peer_get', 'peer_get_by_company', 'peer_get_by_peer',
           'peer_get_audit_records', 'peer_get_audit_records_by_record']

import loguru
import related
import pymysql
from .. import model
from . _errors import DuplicateKeyError


def peer_insert(record: model.Peer, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a new peer record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO peer(company_id, peer) VALUES (%s, %s);", (record.company_id, record.peer,))
        except pymysql.err.IntegrityError as e:
            err_no = e.args[0]
            err_msg = e.args[1]

            if err_no == 1062:
                raise DuplicateKeyError(err_msg)
            else:
                loguru.logger.error(f"Failed to insert peer record: ({record.company_id}, {record.peer}), error: {err_msg}")
            raise

        return cursor.lastrowid


def peer_update(record: model.Peer, db_conn: pymysql.Connection) -> int | None:
    """
    This function updates a peer record, if one exists
    :param record: the record to update
    :param db_conn: the database_old connection to use
    :return: True if successful
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""UPDATE peer SET company_id = %s, peer = %s, lock_version = lock_version + 1, 
                            updated_at = CURRENT_TIMESTAMP WHERE (id = %s) AND (lock_version = %s);""",
                       (record.company_id, record.peer, record.id, record.lock_version))
        return cursor.rowcount == 1


def peer_delete(record_id: int, lock_version: int, db_conn: pymysql.Connection) -> int | None:
    """
     This function deletes records based on the provided parameters
     :param record_id: the id of the record to delete
     :param lock_version: the version flag of the record to delete
     :param db_conn: the database_old connection to use
     :return: True if successful
     """
    with db_conn.cursor() as cursor:
        cursor.execute("DELETE FROM peer WHERE (id = %s) AND (lock_version = %s);", (record_id, lock_version))
        return cursor.rowcount == 1


def peer_get(record_id: int, db_conn: pymysql.Connection) -> model.Peer | None:
    """
    This function returns a peer record for the given parameters, if one exists
    :param record_id: the id of the record to load
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, company_id, peer, lock_version, created_at, updated_at 
                            FROM peer WHERE (id = %s )""", (record_id,))
        data = cursor.fetchone()
        if data:
            record = related.to_model(model.Peer, data)
            return record


def peer_get_by_company(company_id: int, db_conn: pymysql.Connection) -> list[model.Peer] | None:
    """
    This function returns peer records for the given company ticker, if any exists
    :param company_id: The id of the company to return peers for
    :param db_conn: the database_old connection to use
    :return: the peer records if any exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, company_id, peer, lock_version, created_at, updated_at 
                            FROM peer WHERE (company_id = %s )""", (company_id,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(model.Peer, row)
                records.append(record)
            return records


def peer_get_by_peer(peer: str, db_conn: pymysql.Connection) -> list[model.Peer] | None:
    """
    This function returns records for the given peer ticker, if any exists
    :param peer: the company ticker to search for
    :param db_conn: the database_old connection to use
    :return: the peer records if any exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute(f"""SELECT id, company_id, peer, lock_version, created_at, updated_at 
                            FROM peer WHERE (peer = %s )""", (peer,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(model.Peer, row)
                records.append(record)
            return records


def peer_get_audit_records(db_conn: pymysql.Connection) -> list[model.XxxPeer] | None:
    """
    This function returns all audit records for the table
    :param db_conn: the database_old connection to use
    :return: list of audit records, if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute("SELECT id, logged_at, audit_action, record_id, company_id, peer, lock_version FROM xxx_peer;")
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxPeer, row)
                records.append(record)

            return records


def peer_get_audit_records_by_record(record_id: int, db_conn: pymysql.Connection) -> list[model.XxxPeer] | None:
    """
    This function returns all audit records for a given record
    :param record_id: The id to report on
    :param db_conn: the database_old connection to use
    :return: list of audit records, if any
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, logged_at, audit_action, record_id, company_id, peer, lock_version FROM xxx_peer 
                                WHERE (record_id = %s);""", (record_id,))
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(model.XxxPeer, row)
                records.append(record)

            return records
