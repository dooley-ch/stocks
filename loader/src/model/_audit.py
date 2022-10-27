# *******************************************************************************************
#  File:  _audit.py
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

__all__ = ['XxxBalanceSheet', 'XxxCompany', 'XxxIncome', 'XxxIndustry', 'XxxPeer', 'XxxSector', 'XxxQuarter']

import datetime
import decimal
import related
from . import _core


@related.immutable
class XxxBalanceSheet:
    """
    This class maps to the xxx_company table and holds audit information for the company table
    """
    id: int = related.IntegerField(required=True)
    logged_at: datetime.datetime = related.DateTimeField(required=True)
    record_id: int = related.IntegerField(required=True)
    lock_version: int = related.IntegerField(required=True)
    audit_action: _core.AuditAction = related.ChildField(_core.AuditAction, required=True)
    fiscal_year: datetime.datetime = related.DateTimeField()
    restated: datetime.datetime = related.DateTimeField()
    shares_basic: int = related.IntegerField()
    shares_diluted: int = related.IntegerField()
    cash: decimal.Decimal = related.DecimalField()
    accounts_receivable: decimal.Decimal = related.DecimalField()
    inventories: decimal.Decimal = related.DecimalField()
    current_assets: decimal.Decimal = related.DecimalField()
    total_assets: decimal.Decimal = related.DecimalField()
    accounts_payable: decimal.Decimal = related.DecimalField()
    current_liabilities: decimal.Decimal = related.DecimalField()
    long_term_debt: decimal.Decimal = related.DecimalField()
    share_capital: decimal.Decimal = related.DecimalField()
    total_capital: decimal.Decimal = related.DecimalField()
    capital_expenditure: decimal.Decimal = related.DecimalField()
    cashflow: decimal.Decimal = related.DecimalField()
    bnk_inter_bank_assets = related.DecimalField()
    bnk_net_loans = related.DecimalField()
    bnk_total_deposits = related.DecimalField()
    ins_total_investments = related.DecimalField()
    ins_insurance_reserves = related.DecimalField()
    ins_policyholders_equity = related.DecimalField()
    company_id: decimal.Decimal = related.DecimalField()


@related.immutable
class XxxCompany:
    """
    This class maps to the xxx_company table and holds audit information for the company table
    """
    id: int = related.IntegerField(required=True)
    logged_at: datetime.datetime = related.DateTimeField(required=True)
    record_id: int = related.IntegerField(required=True)
    lock_version: int = related.IntegerField(required=True)
    audit_action: _core.AuditAction = related.ChildField(_core.AuditAction, required=True)
    company_name: str = related.StringField()
    description: str = related.StringField()
    stock_exchange: str = related.StringField()
    cik_number: str = related.StringField()
    figi_code: str = related.StringField()
    simfin_number: int = related.IntegerField()
    is_sp100: bool = related.BooleanField()
    is_sp600: bool = related.BooleanField()
    is_sp400: bool = related.BooleanField()
    is_sp500: bool = related.BooleanField()
    company_type: str = related.StringField()
    industry_id: bool = related.BooleanField()
    is_active: bool = related.BooleanField()
    has_financials: bool = related.BooleanField()


@related.immutable
class XxxIncome:
    """
    This class maps to the xxx_income table and holds audit information for the income table
    """
    id: int = related.IntegerField(required=True)
    logged_at: datetime.datetime = related.DateTimeField(required=True)
    record_id: int = related.IntegerField(required=True)
    lock_version: int = related.IntegerField(required=True)
    audit_action: _core.AuditAction = related.ChildField(_core.AuditAction, required=True)
    fiscal_year: datetime.datetime = related.DateTimeField(required=True)
    restated: datetime.datetime = related.DateTimeField()

    revenue: decimal.Decimal = related.DecimalField()
    gross_profit: decimal.Decimal = related.DecimalField()
    depreciation: decimal.Decimal = related.DecimalField()
    interest_expense: decimal.Decimal = related.DecimalField()
    pretax_income: decimal.Decimal = related.DecimalField()
    tax: decimal.Decimal = related.DecimalField()
    net_income: decimal.Decimal = related.DecimalField()
    net_income_core: decimal.Decimal = related.DecimalField()
    bnk_provision_for_loan_losses = related.DecimalField()
    bnk_operating_income = related.DecimalField()
    ins_total_claims = related.DecimalField()
    ins_operating_income = related.DecimalField()
    company_id: decimal.Decimal = related.DecimalField()


@related.immutable
class XxxIndustry:
    """
    This class maps to the xxx_industry table and holds audit information for the industry table
    """
    id: int = related.IntegerField(required=True)
    logged_at: datetime.datetime = related.DateTimeField(required=True)
    record_id: int = related.IntegerField(required=True)
    lock_version: int = related.IntegerField(required=True)
    audit_action: _core.AuditAction = related.ChildField(_core.AuditAction, required=True)
    name: str = related.StringField()
    sector_id: int = related.IntegerField(required=True)
    is_active: bool = _core.FlagField()


@related.immutable
class XxxPeer:
    """
    This class maps to the xxx_peer table and holds audit information for the peer table
    """
    id: int = related.IntegerField(required=True)
    logged_at: datetime.datetime = related.DateTimeField(required=True)
    record_id: int = related.IntegerField(required=True)
    lock_version: int = related.IntegerField(required=True)
    audit_action: _core.AuditAction = related.ChildField(_core.AuditAction, required=True)
    company_id: int = related.IntegerField()
    peer: str = _core.TickerField()


@related.immutable
class XxxSector:
    """
    This class maps to the xxx_sector table and holds audit information for the sector table
    """
    id: int = related.IntegerField(required=True)
    logged_at: datetime.datetime = related.DateTimeField(required=True)
    record_id: int = related.IntegerField(required=True)
    lock_version: int = related.IntegerField(required=True)
    audit_action: _core.AuditAction = related.ChildField(_core.AuditAction, required=True)
    name: str = related.StringField()
    is_active: bool = _core.FlagField()


@related.immutable
class XxxQuarter:
    """
    This class maps to the xxx_quarter table and holds audit information for the quarter table
    """
    id: int = related.IntegerField(required=True)
    logged_at: datetime.datetime = related.DateTimeField(required=True)
    record_id: int = related.IntegerField(required=True)
    audit_action: _core.AuditAction = related.ChildField(_core.AuditAction, required=True)
    year: int = related.IntegerField(required=False)
    quarter: str = related.StringField(required=False)
    fiscal_year: datetime.datetime = related.DateTimeField(required=False)
    restated: datetime.datetime = related.DateTimeField(required=False)
    shares_basic: int = related.IntegerField(required=False)
    shares_diluted: int = related.IntegerField(required=False)
    revenue: decimal.Decimal = related.DecimalField(required=False)
    pretax_income: decimal.Decimal = related.DecimalField(required=False)
    tax: decimal.Decimal = related.DecimalField(required=False)
    net_income: decimal.Decimal = related.DecimalField(required=False)
    net_income_core: decimal.Decimal = related.DecimalField(required=False)
    dividends_paid: decimal.Decimal = related.DecimalField(required=False)
    net_change_in_cash: decimal.Decimal = related.DecimalField(required=False)
    company_id: int = related.IntegerField(required=False)
    lock_version: int = related.IntegerField(required=False)
