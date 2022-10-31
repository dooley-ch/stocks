# *******************************************************************************************
#  File:  _company.py
#
#  Created: 21-09-2022
#
#  History:
#  21-09-2022: Initial version
#
# *******************************************************************************************

from __future__ import annotations

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['BalanceSheet', 'Company', 'Income', 'Industry', 'Peer', 'Sector', 'Quarter']

import related
import datetime
import decimal
from . import _core


@related.immutable()
class Sector:
    """
    This class maps to the sector table
    """
    id: int = related.IntegerField(default=0)
    name: str = related.StringField(default='')
    is_active: bool = _core.FlagField(default=True)
    lock_version: int = related.IntegerField(default=1)
    created_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    updated_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())

    def evolve(self, **kwargs):
        """
        This method returns a new instance of the class, with the given attributes changed
        :param kwargs: the attributes to change
        :return: a new instance of the class with the given attributes changed
        """
        name = kwargs.get('name', self.name)
        is_active = kwargs.get('is_active', self.is_active)

        return Sector(self.id, name, is_active, self.lock_version, self.created_at, self.updated_at)


@related.immutable
class Peer:
    """
    This class maps to the peer table
    """
    id: int = related.IntegerField(default=0)
    company_id: int = related.IntegerField(default=0)
    peer: str = _core.TickerField(default='')
    lock_version: int = related.IntegerField(default=1)
    created_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    updated_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())

    def evolve(self, **kwargs):
        """
        This method returns a new instance of the class, with the given attributes changed
        :param kwargs: the attributes to change
        :return: a new instance of the class with the given attributes changed
        """
        company_id = kwargs.get('company_id', self.company_id)
        peer = kwargs.get('peer', self.peer)

        return Peer(self.id, company_id, peer, self.lock_version, self.created_at, self.updated_at)


@related.immutable
class Industry:
    """
    This class maps to the industry table
    """
    id: int = related.IntegerField(default=0)
    name: str = related.StringField(default='')
    sector_id: int = related.IntegerField(default='')
    is_active: bool = _core.FlagField(default=True)
    lock_version: int = related.IntegerField(default=1)
    created_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    updated_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())

    def evolve(self, **kwargs):
        """
        This method returns a new instance of the class, with the given attributes changed
        :param kwargs: the attributes to change
        :return: a new instance of the class with the given attributes changed
        """
        name = kwargs.get('name', self.name)
        sector_id = kwargs.get('sector_id', self.sector_id)
        is_active = kwargs.get('is_active', self.is_active)

        return Industry(self.id, name, sector_id, is_active, self.lock_version, self.created_at, self.updated_at)


@related.immutable
class Income:
    """
    This class maps to the income table
    """
    id: int = related.IntegerField(default=0)
    year: int = related.IntegerField(default=0)
    fiscal_year: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    restated: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    revenue: decimal.Decimal = related.DecimalField(default='NaN')
    gross_profit: decimal.Decimal = related.DecimalField(default='NaN')
    depreciation: decimal.Decimal = related.DecimalField(default='NaN')
    interest_expense: decimal.Decimal = related.DecimalField(default='NaN')
    pretax_income: decimal.Decimal = related.DecimalField(default='NaN')
    tax: decimal.Decimal = related.DecimalField(default='NaN')
    net_income: decimal.Decimal = related.DecimalField(default='NaN')
    net_income_core: decimal.Decimal = related.DecimalField(default='NaN')
    bnk_provision_for_loan_losses: decimal.Decimal = related.DecimalField(default='NaN')
    bnk_operating_income: decimal.Decimal = related.DecimalField(default='NaN')
    ins_total_claims: decimal.Decimal = related.DecimalField(default='NaN')
    ins_operating_income: decimal.Decimal = related.DecimalField(default='NaN')
    company_id: int = related.IntegerField(default=0)
    lock_version: int = related.IntegerField(default=1)
    created_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    updated_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())

    def evolve(self, **kwargs):
        """
        This method returns a new instance of the class, with the given attributes changed
        :param kwargs: the attributes to change
        :return: a new instance of the class with the given attributes changed
        """
        year = kwargs.get('year', self.year)
        fiscal_year = kwargs.get('fiscal_year', self.fiscal_year)
        restated = kwargs.get('restated', self.restated)
        revenue = kwargs.get('revenue', self.revenue)
        gross_profit = kwargs.get('gross_profit', self.gross_profit)
        depreciation = kwargs.get('depreciation', self.depreciation)
        interest_expense = kwargs.get('interest_expense', self.interest_expense)
        pretax_income = kwargs.get('pretax_income', self.pretax_income)
        tax = kwargs.get('tax', self.tax)
        net_income = kwargs.get('net_income', self.net_income)
        net_income_core = kwargs.get('net_income_core', self.net_income_core)
        bnk_provision_for_loan_losses = kwargs.get('bnk_provision_for_loan_losses', self.bnk_provision_for_loan_losses)
        bnk_operating_income = kwargs.get('bnk_operating_income', self.bnk_operating_income)
        ins_total_claims = kwargs.get('ins_total_claims', self.ins_total_claims)
        ins_operating_income = kwargs.get('ins_total_claims', self.ins_total_claims)
        company_id = kwargs.get('company_id', self.company_id)

        return Income(self.id, year, fiscal_year, restated, revenue, gross_profit,
                      depreciation, interest_expense, pretax_income, tax, net_income, net_income_core,
                      bnk_provision_for_loan_losses, bnk_operating_income, ins_total_claims, ins_operating_income,
                      company_id, self.lock_version, self.created_at, self.updated_at)


@related.immutable
class Company:
    """
    This class maps to the Company table
    """
    id: int = related.IntegerField(default=0)
    ticker: str = _core.TickerField(default='')
    name: str = related.StringField(default='')
    currency: str = related.StringField(default='')
    stock_exchange: str = related.StringField(default='')
    description: str | None = related.StringField(default=None)
    cik_number: str = _core.CikNumberField(default="0000000000")
    figi_code: str = _core.OpenFIGIField(default="000000000000")
    simfin_number: int = related.IntegerField(default=0)
    is_sp100: bool = _core.FlagField(default=False)
    is_sp600: bool = _core.FlagField(default=False)
    is_sp400: bool = _core.FlagField(default=False)
    is_sp500: bool = _core.FlagField(default=False)
    company_type_id: _core.CompanyType = related.ChildField(_core.CompanyType, default=_core.CompanyType.Unknown)
    industry_id: int = related.IntegerField(default=0)
    is_active: bool = _core.FlagField(default=True)
    has_financials: bool = _core.FlagField(default=False)
    lock_version: int = related.IntegerField(default=1)
    created_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    updated_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())

    def evolve(self, **kwargs):
        """
        This method returns a new instance of the class, with the given attributes changed
        :param kwargs: the attributes to change
        :return: a new instance of the class with the given attributes changed
        """
        ticker = kwargs.get('ticker', self.ticker)
        name = kwargs.get('name', self.name)
        currency = kwargs.get('currency', self.currency)
        description = kwargs.get('description', self.description)
        stock_exchange = kwargs.get('stock_exchange', self.stock_exchange)
        cik_number = kwargs.get('cik_number', self.cik_number)
        figi_code = kwargs.get('figi_code', self.figi_code)
        simfin_number = kwargs.get('simfin_number', self.simfin_number)
        is_sp100 = kwargs.get('is_sp100', self.is_sp100)
        is_sp600 = kwargs.get('is_sp600', self.is_sp600)
        is_sp400 = kwargs.get('is_sp400', self.is_sp400)
        is_sp500 = kwargs.get('is_sp500', self.is_sp500)
        company_type_id = kwargs.get('company_type_id', self.company_type_id)
        industry_id = kwargs.get('industry_id', self.industry_id)
        is_active = kwargs.get('is_active', self.is_active)
        has_financials = kwargs.get('has_financials', self.has_financials)

        return Company(self.id, ticker, name, currency, description, stock_exchange, cik_number, figi_code,
                       simfin_number,
                       is_sp100, is_sp600, is_sp400, is_sp500, company_type_id, industry_id, is_active, has_financials,
                       self.lock_version, self.created_at, self.updated_at)


@related.immutable
class BalanceSheet:
    """
    This class maps to the balance sheet table
    """
    id: int = related.IntegerField(default=0)
    year: int = related.IntegerField(default=0)
    fiscal_year: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    restated: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    shares_basic: int = related.IntegerField(default=0)
    shares_diluted: int = related.IntegerField(default=0)
    cash: decimal.Decimal = related.DecimalField(default='NaN')
    accounts_receivable: decimal.Decimal = related.DecimalField(default='NaN')
    inventories: decimal.Decimal = related.DecimalField(default='NaN')
    current_assets: decimal.Decimal = related.DecimalField(default='NaN')
    total_assets: decimal.Decimal = related.DecimalField(default='NaN')
    accounts_payable: decimal.Decimal = related.DecimalField(default='NaN')
    current_liabilities: decimal.Decimal = related.DecimalField(default='NaN')
    long_term_debt: decimal.Decimal = related.DecimalField(default='NaN')
    share_capital: decimal.Decimal = related.DecimalField(default='NaN')
    total_capital: decimal.Decimal = related.DecimalField(default='NaN')
    capital_expenditure: decimal.Decimal = related.DecimalField(default='NaN')
    cashflow: decimal.Decimal = related.DecimalField(default='NaN')
    bnk_inter_bank_assets = related.DecimalField(default='NaN')
    bnk_net_loans = related.DecimalField(default='NaN')
    bnk_total_deposits = related.DecimalField(default='NaN')
    ins_total_investments = related.DecimalField(default='NaN')
    ins_insurance_reserves = related.DecimalField(default='NaN')
    ins_policyholders_equity = related.DecimalField(default='NaN')
    company_id: int = related.IntegerField(default=0)
    lock_version: int = related.IntegerField(default=1)
    created_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    updated_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())

    def evolve(self, **kwargs):
        """
        This method returns a new instance of the class, with the given attributes changed
        :param kwargs: the attributes to change
        :return: a new instance of the class with the given attributes changed
        """
        year = kwargs.get('year', self.year)
        fiscal_year = kwargs.get('fiscal_year', self.fiscal_year)
        restated = kwargs.get('restated', self.restated)
        shares_basic = kwargs.get('shares_basic', self.shares_basic)
        shares_diluted = kwargs.get('shares_diluted', self.shares_diluted)
        cash = kwargs.get('cash', self.cash)
        accounts_receivable = kwargs.get('accounts_receivable', self.accounts_receivable)
        inventories = kwargs.get('inventories', self.inventories)
        current_assets = kwargs.get('current_assets', self.current_assets)
        total_assets = kwargs.get('total_assets', self.total_assets)
        accounts_payable = kwargs.get('accounts_payable', self.accounts_payable)
        current_liabilities = kwargs.get('current_liabilities', self.current_liabilities)
        long_term_debt = kwargs.get('long_term_debt', self.long_term_debt)
        share_capital = kwargs.get('share_capital', self.share_capital)
        total_capital = kwargs.get('total_capital', self.total_capital)
        capital_expenditure = kwargs.get('capital_expenditure', self.capital_expenditure)
        cashflow = kwargs.get('cashflow', self.cashflow)
        bnk_inter_bank_assets = kwargs.get('bnk_inter_bank_assets', self.bnk_inter_bank_assets)
        bnk_net_loans = kwargs.get('bnk_net_loans', self.bnk_net_loans)
        bnk_total_deposits = kwargs.get('bnk_total_deposits', self.bnk_total_deposits)
        ins_total_investments = kwargs.get('ins_total_investments', self.ins_total_investments)
        ins_insurance_reserves = kwargs.get('ins_insurance_reserves', self.ins_insurance_reserves)
        ins_policyholders_equity = kwargs.get('ins_policyholders_equity', self.ins_policyholders_equity)
        company_id = kwargs.get('company_id', self.company_id)

        return BalanceSheet(self.id, year, fiscal_year, restated, shares_basic, shares_diluted, cash,
                            accounts_receivable, inventories, current_assets, total_assets, accounts_payable,
                            current_liabilities, long_term_debt, share_capital, total_capital, capital_expenditure,
                            cashflow, bnk_inter_bank_assets, bnk_net_loans, bnk_total_deposits, ins_total_investments,
                            ins_insurance_reserves, ins_policyholders_equity, company_id,
                            self.lock_version, self.created_at, self.updated_at)


@related.immutable
class Quarter:
    """
    This class maps to the quarter table
    """
    id: int = related.IntegerField(default=0)
    year: int = related.IntegerField(default=0)
    quarter: str = related.StringField(default='Q0')
    fiscal_year: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    restated: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    shares_basic: int = related.IntegerField(default=0)
    shares_diluted: int = related.IntegerField(default=0)
    revenue: decimal.Decimal = related.DecimalField(default='NaN')
    pretax_income: decimal.Decimal = related.DecimalField(default='NaN')
    tax: decimal.Decimal = related.DecimalField(default='NaN')
    net_income: decimal.Decimal = related.DecimalField(default='NaN')
    net_income_core: decimal.Decimal = related.DecimalField(default='NaN')
    dividends_paid: decimal.Decimal = related.DecimalField(default='NaN')
    net_change_in_cash: decimal.Decimal = related.DecimalField(default='NaN')
    company_id: int = related.IntegerField(default=0)
    lock_version: int = related.IntegerField(default=1)
    created_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())
    updated_at: datetime.datetime = related.DateTimeField(default=datetime.datetime.now())

    def evolve(self, **kwargs):
        """
        This method returns a new instance of the class, with the given attributes changed
        :param kwargs: the attributes to change
        :return: a new instance of the class with the given attributes changed
        """
        year = kwargs.get('year', self.year)
        quarter = kwargs.get('quarter', self.quarter)
        fiscal_year = kwargs.get('fiscal_year', self.fiscal_year)
        restated = kwargs.get('restated', self.restated)
        shares_basic = kwargs.get('shares_basic', self.shares_basic)
        shares_diluted = kwargs.get('shares_diluted', self.shares_diluted)
        revenue = kwargs.get('revenue', self.revenue)
        pretax_income = kwargs.get('pretax_income', self.pretax_income)
        tax = kwargs.get('tax', self.tax)
        net_income = kwargs.get('net_income', self.net_income)
        net_income_core = kwargs.get('net_income_core', self.net_income_core)
        dividends_paid = kwargs.get('dividends_paid', self.dividends_paid)
        net_change_in_cash = kwargs.get('net_change_in_cash', self.net_change_in_cash)
        company_id = kwargs.get('company_id', self.company_id)

        return Quarter(self.id, year, quarter, fiscal_year, restated, shares_basic, shares_diluted, revenue, pretax_income, tax,
                       net_income, net_income_core, dividends_paid, net_change_in_cash, company_id, self.lock_version,
                       self.created_at, self.updated_at)
