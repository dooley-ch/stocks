# *******************************************************************************************
#  File:  _core.py
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

__all__ = ['get_connection', 'CursorContext']

import typing
from contextlib import contextmanager
import pymysql
import pymysql.cursors


# noinspection PyPropertyDefinition
@typing.runtime_checkable
class ConnectionInfoProtocol(typing.Protocol):
    """
    This class defines the parameters needed to connect to the database_old
    """

    @property
    def user(self) -> str:
        ...

    @property
    def password(self) -> str:
        ...

    @property
    def database(self) -> str:
        ...

    @property
    def autocommit(self) -> bool:
        ...

    @property
    def host(self) -> str:
        ...

    @property
    def port(self) -> int:
        ...


def get_connection(conn_info: ConnectionInfoProtocol) -> pymysql.Connection:
    """
    Creates and returns a connection to the database_old
    """
    return pymysql.connect(host=conn_info.host, user=conn_info.user, password=conn_info.password,
                           database=conn_info.database, charset='utf8mb4', autocommit=conn_info.autocommit,
                           cursorclass=pymysql.cursors.DictCursor)


@contextmanager
def CursorContext(db_conn: pymysql.Connection | ConnectionInfoProtocol) -> pymysql.cursors.Cursor:
    """
    This method returns am open database_old cursor
    """
    can_close_cursor: bool = False

    if isinstance(db_conn, ConnectionInfoProtocol):
        db_con = get_connection(db_conn)
        can_close_cursor = True

    cursor = None

    try:
        cursor = db_conn.cursor()
        yield cursor
    finally:
        if cursor:
            cursor.close()

        if can_close_cursor:
            db_conn.close()
