# *******************************************************************************************
#  File:  _version.py
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

__all__ = ['get_version']

import pymysql.cursors
import related
from .. import model


def get_version(db_conn: pymysql.Connection) -> model.Version | None:
    """
    This function returns the version record from the database_old
    """
    with db_conn:
        with db_conn.cursor() as cursor:
            cursor.execute("SELECT id, major, minor, build, lock_version, created_at, updated_at FROM version;")
            data = cursor.fetchone()
            if data:
                record = related.to_model(model.Version, data)
                return record
