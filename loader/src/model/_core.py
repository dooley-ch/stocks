# *******************************************************************************************
#  File:  _core.py
#
#  Created: 21-09-2022
#
#  History:
#  21-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['Version', 'AuditAction', 'CompanyType', 'CikNumberField', 'OpenFIGIField', 'TickerField', 'FlagField']

import datetime
import enum
from typing import Any
import related
import attr
import attrs.validators
# noinspection PyPackageRequirements
from future.utils import string_types


@related.immutable()
class Version:
    """
    This class maps to the _version table in the database_old
    """
    id: int = related.IntegerField(required=True)
    major: int = related.IntegerField(required=True)
    minor: int = related.IntegerField(required=True)
    build: int = related.IntegerField(required=True)
    lock_version: int = related.IntegerField(required=True)
    created_at: datetime.datetime = related.DateTimeField(required=True)
    updated_at: datetime.datetime = related.DateTimeField(required=True)

    def is_valid(self, major: int, minor: int, build: int | None = None) -> bool:
        """
        This method returns true if the version number matches, otherwise false
        """
        if build is None:
            return (self.major == major) and (self.minor == minor)

        return (self.major == major) and (self.minor == minor) and (self.build == build)

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.build}"


class CompanyType(enum.IntEnum):
    """
    This class defines the classification of companies in the application
    """
    General = 1
    Bank = 2
    Insurance = 3
    Unknown = 4


class AuditAction(str, enum.Enum):
    """
    This class represents the types of audit activity
    """
    Insert = "I"
    Update = "U"
    Delete = "D"


def _cik_number_converter(value: Any) -> str | None:
    """
    Returns a CIK number if the value is not None.

    :param value: None or a value that can be converted to a CIK number.
    :return: None or CIK number
    """
    if not(value is None or isinstance(value, string_types)):
        value = str(value)

    if len(value) < 12:
        value = value.zfill(10)

    return value


def _openfigi_number_converter(value):
    """
    Returns a OpenFIGI number if the value is not None.

    :param value: None or a value that can be converted to a OpenFIGI number.
    :return: None or OpenFIGI number
    """
    if not(value is None or isinstance(value, string_types)):
        value = str(value)

    if len(value) < 12:
        value = value.zfill(12)

    return value


def _ticker_converter(value):
    """
    Returns a Ticker if the value is not None.

    :param value: None or a value that can be converted to a Ticker.
    :return: None or a Ticker
    """
    if not(value is None or isinstance(value, string_types)):
        value = str(value)

    if value:
        value = value.upper()

    return value


def _flag_converter(value) -> bool:
    """
    Converts text to boolean
    """
    if not(value is None or isinstance(value, string_types)):
        value = str(value)

    if value:
        if value == 'True':
            value = True
        else:
            value = False

    return value


def _init_default(required, default, optional_default):
    """
    Returns optional default if field is not required and
    default was not provided.

    :param bool required: whether the field is required in a given model.
    :param default: default provided by creator of field.
    :param optional_default: default for the data type if none provided.
    :return: default or optional default based on inputs
    """
    if not required and default == attr.NOTHING:
        default = optional_default

    return default


# noinspection PyShadowingBuiltins
def CikNumberField(default=attr.NOTHING, required=True, repr=True, cmp=True, key=None):
    """
    Create new CIK field on a model.

    :param default: any string value
    :param bool required: whether or not the object is invalid if not provided.
    :param bool repr: include this field should appear in object's repr.
    :param bool cmp: include this field in generated comparison.
    :param string key: override name of the value when converted to dict.
    """
    default = _init_default(required, default, None)
    return attr.attrib(default=default, converter=_cik_number_converter,
                       validator=attrs.validators.matches_re('[0-9]{10}'), repr=repr, cmp=cmp,
                       metadata=dict(key=key))


# noinspection PyShadowingBuiltins
def OpenFIGIField(default=attr.NOTHING, required=True, repr=True, cmp=True, key=None):
    """
    Create new CIK field on a model.

    :param default: any string value
    :param bool required: whether or not the object is invalid if not provided.
    :param bool repr: include this field should appear in object's repr.
    :param bool cmp: include this field in generated comparison.
    :param string key: override name of the value when converted to dict.
    """
    default = _init_default(required, default, None)
    return attr.attrib(default=default, converter=_openfigi_number_converter,
                       validator=attrs.validators.matches_re('^[A-Z0-9]{12}$'), repr=repr, cmp=cmp,
                       metadata=dict(key=key))


# noinspection PyShadowingBuiltins
def TickerField(default=attr.NOTHING, required=True, repr=True, cmp=True, key=None):
    """
    Create new Ticker field on a model.

    :param default: any string value
    :param bool required: whether or not the object is invalid if not provided.
    :param bool repr: include this field should appear in object's repr.
    :param bool cmp: include this field in generated comparison.
    :param string key: override name of the value when converted to dict.
    """
    default = _init_default(required, default, None)
    return attr.attrib(default=default, converter=_ticker_converter,
                       validator=attrs.validators.matches_re('^[A-Z0-9._\-]{1,12}$'), repr=repr, cmp=cmp,
                       metadata=dict(key=key))


# noinspection PyShadowingBuiltins
def FlagField(default=attr.NOTHING, required=True, repr=True, cmp=True, key=None):
    """
    Create new IsActive field on a model.

    :param default: any string value
    :param bool required: whether or not the object is invalid if not provided.
    :param bool repr: include this field should appear in object's repr.
    :param bool cmp: include this field in generated comparison.
    :param string key: override name of the value when converted to dict.
    """
    default = _init_default(required, default, None)
    return attr.attrib(default=default, converter=_flag_converter, repr=repr, cmp=cmp, metadata=dict(key=key))
