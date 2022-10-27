# *******************************************************************************************
#  File:  _errors.py
#
#  Created: 26-09-2022
#
#  History:
#  26-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['DatastoreError', 'DuplicateKeyError']


class DatastoreError(Exception):
    """
    Base class for Datastore errors
    """
    pass


class DuplicateKeyError(DatastoreError):
    """
    This class is raised when an attempt to enter a duplicate record in a table
    """
    pass
