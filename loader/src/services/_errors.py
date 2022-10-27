# *******************************************************************************************
#  File:  errors.py
#
#  Created: 31-08-2022
#
#  History:
#  31-08-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['ServiceError', 'ServiceLimitExceeded']


class ServiceError(Exception):
    """
    Base classes for service errors
    """
    pass


class ServiceLimitExceeded(ServiceError):
    """
    Raised if a service exceeds its usage limits
    """
    pass
