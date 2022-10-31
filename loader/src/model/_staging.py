# *******************************************************************************************
#  File:  _staging.py
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

__all__ = ['zBalanceSheetBankAnnualRecord', 'zBalanceSheetBankQuarterRecord',
           'zBalanceSheetGeneralAnnualRecord', 'zBalanceSheetGeneralQuarterRecord',
           'zBalanceSheetInsuranceAnnualRecord', 'zBalanceSheetInsuranceQuarterRecord',
           'zCashflowBankAnnualRecord', 'zCashflowBankQuarterRecord', 'zCashflowGeneralAnnualRecord',
           'zCashflowGeneralQuarterRecord',
           'zCashflowInsuranceQuarterRecord', 'zCashflowInsuranceAnnualRecord', 'zCikRecord',
           'zIncomeBankAnnualRecord', 'zIncomeBankQuarterRecord', 'zIncomeGeneralAnnualRecord',
           'zIncomeGeneralQuarterRecord', 'zIncomeInsuranceAnnualRecord', 'zIncomeInsuranceQuarterRecord',
           'zMasterTickerRecord', 'zMorningstarProfileRecord', 'zOpenFIGIRecord', 'zPeerMapRecord',
           'zSimFinCompaniesRecord', 'zSimFinIndustriesRecord', 'zSimFinPrice', 'zSp100Record', 'zSp400Record',
           'zSp500Record', 'zSp600Record', 'zsCompanyRecord', 'zsPeerRecord', 'zsSectorRecord', 'zsIndustryRecord']

import related
from . import _core


@related.immutable
class _zBalanceSheetBankRecord:
    """
    Base class for implementing the general balance sheet statement
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    currency: str = related.StringField(default='')
    fiscal_year: str = related.StringField(default='')
    fiscal_period: str = related.StringField(default='')
    report_date: str = related.StringField(default='')
    publish_date: str = related.StringField(default='')
    restated_date: str = related.StringField(default='')
    shares_basic: str = related.StringField(default='NaN')
    shares_diluted: str = related.StringField(default='NaN')

    cash_cash_equivalents_short_term_investments: str = related.StringField(default='NaN')
    interbank_Assets: str = related.StringField(default='NaN')
    short_long_term_investments: str = related.StringField(default='NaN')
    accounts_notes_receivable: str = related.StringField(default='NaN')
    net_loans: str = related.StringField(default='NaN')
    net_fixed_assets: str = related.StringField(default='NaN')
    total_assets: str = related.StringField(default='NaN')
    total_deposits: str = related.StringField(default='NaN')
    short_term_debt: str = related.StringField(default='NaN')
    long_term_debt: str = related.StringField(default='NaN')
    total_liabilities: str = related.StringField(default='NaN')
    preferred_equity: str = related.StringField(default='NaN')
    share_capital_additional_paid_in_capital: str = related.StringField(default='NaN')
    treasury_stock: str = related.StringField(default='NaN')
    retained_earnings: str = related.StringField(default='NaN')
    total_equity: str = related.StringField(default='NaN')
    total_liabilities_equity: str = related.StringField(default='NaN')


@related.immutable
class zBalanceSheetBankAnnualRecord(_zBalanceSheetBankRecord):
    """
    This class maps to the z_balance_sheet_bank_annual table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zBalanceSheetBankQuarterRecord(_zBalanceSheetBankRecord):
    """
    This class maps to the z_balance_sheet_bank_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class _zBalanceSheetGeneralRecord:
    """
    Base class for implementing the general balance sheet statement
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    currency: str = related.StringField(default='')
    fiscal_year: str = related.StringField(default='')
    fiscal_period: str = related.StringField(default='')
    report_date: str = related.StringField(default='')
    publish_date: str = related.StringField(default='')
    restated_date: str = related.StringField(default='')
    shares_basic: str = related.StringField(default='NaN')
    shares_diluted: str = related.StringField(default='NaN')

    cash_cash_equivalents_short_term_investments: str = related.StringField(default='NaN')
    accounts_notes_receivable: str = related.StringField(default='NaN')
    inventories: str = related.StringField(default='NaN')
    total_current_assets: str = related.StringField(default='NaN')
    property_plant_equipment_net: str = related.StringField(default='NaN')
    long_term_investments_receivables: str = related.StringField(default='NaN')
    other_long_term_assets: str = related.StringField(default='NaN')
    total_noncurrent_assets: str = related.StringField(default='NaN')
    total_assets: str = related.StringField(default='NaN')
    payables_accruals: str = related.StringField(default='NaN')
    short_term_debt: str = related.StringField(default='NaN')
    total_current_liabilities: str = related.StringField(default='NaN')
    long_term_debt: str = related.StringField(default='NaN')
    total_noncurrent_liabilities: str = related.StringField(default='NaN')
    total_liabilities: str = related.StringField(default='NaN')
    share_capital_additional_paid_in_capital: str = related.StringField(default='NaN')
    treasury_stock: str = related.StringField(default='NaN')
    retained_earnings: str = related.StringField(default='NaN')
    total_equity: str = related.StringField(default='NaN')
    total_liabilities_equity: str = related.StringField(default='NaN')


@related.immutable
class zBalanceSheetGeneralAnnualRecord(_zBalanceSheetGeneralRecord):
    """
    This class maps to the z_balance_sheet_insurance_annual table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zBalanceSheetGeneralQuarterRecord(_zBalanceSheetGeneralRecord):
    """
    This class maps to the z_balance_sheet_insurance_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class _zBalanceSheetInsuranceRecord:
    """
    Base class for implementing the insurance balance sheet statement
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    currency: str = related.StringField(default='')
    fiscal_year: str = related.StringField(default='')
    fiscal_period: str = related.StringField(default='')
    report_date: str = related.StringField(default='')
    publish_date: str = related.StringField(default='')
    restated_date: str = related.StringField(default='')
    shares_basic: str = related.StringField(default='NaN')
    shares_diluted: str = related.StringField(default='NaN')

    total_investments: str = related.StringField(default='NaN')
    cash_cash_equivalents_short_term_investments: str = related.StringField(default='NaN')
    accounts_notes_receivable: str = related.StringField(default='NaN')
    property_plant_equipment_net: str = related.StringField(default='NaN')
    total_assets: str = related.StringField(default='NaN')
    insurance_reserves: str = related.StringField(default='NaN')
    short_term_debt: str = related.StringField(default='NaN')
    long_term_debt: str = related.StringField(default='NaN')
    total_liabilities: str = related.StringField(default='NaN')
    preferred_equity: str = related.StringField(default='NaN')
    policyholders_equity: str = related.StringField(default='NaN')
    share_capital_additional_paid_in_capital: str = related.StringField(default='NaN')
    treasury_stock: str = related.StringField(default='NaN')
    retained_earnings: str = related.StringField(default='NaN')
    total_equity: str = related.StringField(default='NaN')
    total_liabilities_equity: str = related.StringField(default='NaN')


@related.immutable
class zBalanceSheetInsuranceAnnualRecord(_zBalanceSheetInsuranceRecord):
    """
    This class maps to the z_balance_sheet_insurance_annual table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zBalanceSheetInsuranceQuarterRecord(_zBalanceSheetInsuranceRecord):
    """
    This class maps to the z_balance_sheet_insurance_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class _zCashflowBankRecord:
    """
    Base class for implementing the bank cashflow statement
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    currency: str = related.StringField(default='')
    fiscal_year: str = related.StringField(default='')
    fiscal_period: str = related.StringField(default='')
    report_date: str = related.StringField(default='')
    publish_date: str = related.StringField(default='')
    restated_date: str = related.StringField(default='')
    shares_basic: str = related.StringField(default='NaN')
    shares_diluted: str = related.StringField(default='NaN')

    net_income_starting_line: str = related.StringField(default='NaN')
    depreciation_amortization: str = related.StringField(default='NaN')
    provision_for_loan_losses: str = related.StringField(default='NaN')
    non_cash_items: str = related.StringField(default='NaN')
    change_in_working_capital: str = related.StringField(default='NaN')
    net_cash_from_operating_activities: str = related.StringField(default='NaN')
    change_in_fixed_assets_intangibles: str = related.StringField(default='NaN')
    net_change_in_loans_interbank: str = related.StringField(default='NaN')
    net_cash_from_acquisitions_divestitures: str = related.StringField(default='NaN')
    net_cash_from_investing_activities: str = related.StringField(default='NaN')
    dividends_paid: str = related.StringField(default='NaN')
    cash_from_repayment_of_debt: str = related.StringField(default='NaN')
    cash_from_repurchase_of_equity: str = related.StringField(default='NaN')
    net_cash_from_financing_activities: str = related.StringField(default='NaN')
    effect_of_foreign_exchange_rates: str = related.StringField(default='NaN')
    net_change_in_cash: str = related.StringField(default='NaN')


@related.immutable
class zCashflowBankAnnualRecord(_zCashflowBankRecord):
    """
    This class maps to the z_cashflow_bank_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zCashflowBankQuarterRecord(_zCashflowBankRecord):
    """
    This class maps to the z_cashflow_bank_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class _zCashflowGeneralRecord:
    """
    Base class for implementing the general cashflow statement
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    currency: str = related.StringField(default='')
    fiscal_year: str = related.StringField(default='')
    fiscal_period: str = related.StringField(default='')
    report_date: str = related.StringField(default='')
    publish_date: str = related.StringField(default='')
    restated_date: str = related.StringField(default='')
    shares_basic: str = related.StringField(default='NaN')
    shares_diluted: str = related.StringField(default='NaN')

    net_income_starting_line: str = related.StringField(default='NaN')
    depreciation_amortization: str = related.StringField(default='NaN')
    non_cash_items: str = related.StringField(default='NaN')
    change_in_working_capital: str = related.StringField(default='NaN')
    change_in_accounts_receivable: str = related.StringField(default='NaN')
    change_in_inventories: str = related.StringField(default='NaN')
    change_in_accounts_payable: str = related.StringField(default='NaN')
    change_in_other: str = related.StringField(default='NaN')
    net_cash_from_operating_Activities: str = related.StringField(default='NaN')
    change_in_fixed_assets_intangibles: str = related.StringField(default='NaN')
    net_change_in_long_term_investment: str = related.StringField(default='NaN')
    net_cash_from_acquisitions_divestitures: str = related.StringField(default='NaN')
    net_cash_from_investing_activities: str = related.StringField(default='NaN')
    dividends_paid: str = related.StringField(default='NaN')
    cash_from_repayment_of_debt: str = related.StringField(default='NaN')
    cash_from_repurchase_of_equity: str = related.StringField(default='NaN')
    net_cash_from_financing_activities: str = related.StringField(default='NaN')
    net_change_in_cash: str = related.StringField(default='NaN')


@related.immutable
class zCashflowGeneralAnnualRecord(_zCashflowGeneralRecord):
    """
    This class maps to the z_cashflow_general_annual table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zCashflowGeneralQuarterRecord(_zCashflowGeneralRecord):
    """
    This class maps to the z_cashflow_general_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class _zCashflowInsuranceRecord:
    """
    Base class for implementing the insurance cashflow statement
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    currency: str = related.StringField(default='')
    fiscal_year: str = related.StringField(default='')
    fiscal_period: str = related.StringField(default='')
    report_date: str = related.StringField(default='')
    publish_date: str = related.StringField(default='')
    restated_date: str = related.StringField(default='')
    shares_basic: str = related.StringField(default='NaN')
    shares_diluted: str = related.StringField(default='NaN')

    net_income_starting_line: str = related.StringField(default='NaN')
    depreciation_amortization: str = related.StringField(default='NaN')
    non_cash_items: str = related.StringField(default='NaN')
    net_cash_from_operating_activities: str = related.StringField(default='NaN')
    change_in_fixed_Assets_intangibles: str = related.StringField(default='NaN')
    net_change_in_investments: str = related.StringField(default='NaN')
    net_cash_from_investing_activities: str = related.StringField(default='NaN')
    dividends_paid: str = related.StringField(default='NaN')
    cash_from_repayment_of_debt: str = related.StringField(default='NaN')
    cash_from_repurchase_of_equity: str = related.StringField(default='NaN')
    net_cash_from_financing_activities: str = related.StringField(default='NaN')
    effect_of_foreign_exchange_rates: str = related.StringField(default='NaN')
    net_change_in_cash: str = related.StringField(default='NaN')


@related.immutable
class zCashflowInsuranceAnnualRecord(_zCashflowInsuranceRecord):
    """
    This class maps to the z_cashflow_insurance_annual table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zCashflowInsuranceQuarterRecord(_zCashflowInsuranceRecord):
    """
    This class maps to the z_cashflow_insurance_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zCikRecord:
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    company: str = related.StringField(default='')
    exchange: str = related.StringField(default='')
    cik: str = _core.CikNumberField(default='0000000000')


@related.immutable
class _zIncomeBankRecord:
    """
    Base class for implementing the bank income statement
    """
    id: int = related.IntegerField(default=0)
    ticker: str = _core.TickerField(default='')
    simfin_id: int = related.IntegerField(default=0)
    currency: str = related.StringField(default='')
    fiscal_year: str = related.StringField(default='')
    fiscal_period: str = related.StringField(default='')
    report_date: str = related.StringField(default='')
    publish_date: str = related.StringField(default='')
    restated_date: str = related.StringField(default='')
    shares_basic: str = related.StringField(default='NaN')
    shares_diluted: str = related.StringField(default='NaN')

    revenue: str = related.StringField(default='NaN')
    provision_for_loan_losses: str = related.StringField(default='NaN')
    net_Revenue_after_provisions: str = related.StringField(default='NaN')
    total_non_interest_expense: str = related.StringField(default='NaN')
    operating_income_loss: str = related.StringField(default='NaN')
    non_operating_income_loss: str = related.StringField(default='NaN')
    pretax_income_loss: str = related.StringField(default='NaN')
    income_tax_expense_benefit_net: str = related.StringField(default='NaN')
    income_loss_from_continuing_operations: str = related.StringField(default='NaN')
    net_extraordinary_gains_losses: str = related.StringField(default='NaN')
    net_income: str = related.StringField(default='NaN')
    net_income_common: str = related.StringField(default='NaN')


@related.immutable
class zIncomeBankAnnualRecord(_zIncomeBankRecord):
    """
    This class maps to the z_income_bank_annual table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zIncomeBankQuarterRecord(_zIncomeBankRecord):
    """
    This class maps to the z_income_bank_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class _zIncomeGeneralRecord:
    """
    Base class for implementing the general income statement
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    currency: str = related.StringField(default='')
    fiscal_year: str = related.StringField(default='')
    fiscal_period: str = related.StringField(default='')
    report_date: str = related.StringField(default='')
    publish_date: str = related.StringField(default='')
    restated_date: str = related.StringField(default='')
    shares_basic: str = related.StringField(default='NaN')
    shares_diluted: str = related.StringField(default='NaN')

    revenue: str = related.StringField(default='NaN')
    cost_of_revenue: str = related.StringField(default='NaN')
    gross_profit: str = related.StringField(default='NaN')
    operating_expenses: str = related.StringField(default='NaN')
    selling_general_administrative: str = related.StringField(default='NaN')
    research_development: str = related.StringField(default='NaN')
    depreciation_amortization: str = related.StringField(default='NaN')
    operating_income: str = related.StringField(default='NaN')
    non_operating_income: str = related.StringField(default='NaN')
    interest_expense_net: str = related.StringField(default='NaN')
    pretax_income_loss_adj: str = related.StringField(default='NaN')
    abnormal_gains_lLosses: str = related.StringField(default='NaN')
    pretax_income_loss: str = related.StringField(default='NaN')
    income_tax_expense_benefit_net: str = related.StringField(default='NaN')
    income_loss_from_continuing_operations: str = related.StringField(default='NaN')
    net_extraordinary_gains_losses: str = related.StringField(default='NaN')
    net_income: str = related.StringField(default='NaN')
    net_income_common: str = related.StringField(default='NaN')


@related.immutable
class zIncomeGeneralAnnualRecord(_zIncomeGeneralRecord):
    """
    This class maps to the z_income_general_annual table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zIncomeGeneralQuarterRecord(_zIncomeGeneralRecord):
    """
    This class maps to the z_income_general_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class _zIncomeInsuranceRecord:
    """
    Base class for implementing the insurance income statement
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    currency: str = related.StringField(default='')
    fiscal_year: str = related.StringField(default='')
    fiscal_period: str = related.StringField(default='')
    report_date: str = related.StringField(default='')
    publish_date: str = related.StringField(default='')
    restated_date: str = related.StringField(default='')
    shares_basic: str = related.StringField(default='NaN')
    shares_diluted: str = related.StringField(default='NaN')

    revenue: str = related.StringField(default='NaN')
    total_claims_losses: str = related.StringField(default='NaN')
    operating_income_loss: str = related.StringField(default='NaN')
    pretax_income_loss: str = related.StringField(default='NaN')
    income_tax_expense_benefit_net: str = related.StringField(default='NaN')
    income_loss_from_affiliates_net_of_taxes: str = related.StringField(default='NaN')
    income_loss_from_continuing_operations: str = related.StringField(default='NaN')
    net_extraordinary_gains_losses: str = related.StringField(default='NaN')
    net_income: str = related.StringField(default='NaN')
    net_income_common: str = related.StringField(default='NaN')


@related.immutable
class zIncomeInsuranceQuarterRecord(_zIncomeInsuranceRecord):
    """
    This class maps to the z_income_insurance_quarter table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zIncomeInsuranceAnnualRecord(_zIncomeInsuranceRecord):
    """
    This class maps to the z_income_insurance_annual table in the database_old and is used
    import the required data
    """
    pass


@related.immutable
class zMasterTickerRecord:
    """
    This class maps to the z_master_ticker table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = _core.TickerField(default='')
    company: str = related.StringField(default='')


@related.immutable
class zMorningstarProfileRecord:
    """
    This class maps to the z_morningstar_profile table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = _core.TickerField(default='')
    company_name: str = related.StringField(default='')
    description: str = related.StringField(default='')
    sector: str = related.StringField(default='')
    industry: str = related.StringField(default='')
    recent_earnings: str = related.StringField(default='')
    fiscal_year_end: str = related.StringField(default='')
    stock_type: str = related.StringField(default='')
    employees: str = related.StringField(default='')


@related.immutable
class zOpenFIGIRecord:
    """
    This class maps to the z_openfigi table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = _core.TickerField(default='')
    open_figi: str = _core.OpenFIGIField(default='0000000000')


@related.immutable
class zPeerMapRecord:
    """
    This class maps to the z_peer_map table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    peer: str = related.StringField(default='')


@related.immutable
class zSimFinCompaniesRecord:
    """
    This class maps to the z_simfin_companies table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    company: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default='')
    industry_id: int = related.IntegerField(default='')


@related.immutable
class zSimFinIndustriesRecord:
    """
    This class maps to the z_simfin_industries table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    industry_id: int = related.IntegerField(default=0)
    sector: str = related.StringField(default='')
    industry: str = related.StringField(default='')


@related.immutable
class zSimFinPrice:
    """
    This class maps to the z_simfin_price table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    price_date: str = related.StringField(default='')
    open_price: str = related.StringField(default='')
    low_price: str = related.StringField(default='')
    high_price: str = related.StringField(default='')
    close_price: str = related.StringField(default='')
    adjusted_close_price: str = related.StringField(default='')
    dividend: str = related.StringField(default='')
    volume: str = related.StringField(default='')
    shares_outstanding: str = related.StringField(default='')


@related.immutable
class zSp100Record:
    """
    This class maps to the z_sp_100 table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    company: str = related.StringField(default='')
    industry: str = related.StringField(default='')


@related.immutable
class zSp400Record:
    """
    This class maps to the z_sp_400 table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    company: str = related.StringField(default='')
    industry: str = related.StringField(default='')


@related.immutable
class zSp500Record:
    """
    This class maps to the z_sp_500 table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    company: str = related.StringField(default='')
    industry: str = related.StringField(default='')


@related.immutable
class zSp600Record:
    """
    This class maps to the z_sp_600 table in the database_old and is used
    import the required data
    """
    id: int = related.IntegerField(default=0)
    ticker: str = related.StringField(default='')
    company: str = related.StringField(default='')
    industry: str = related.StringField(default='')


@related.immutable
class zsCompanyRecord:
    """
    This class maps to the zs_company table in the database_old and is used
    to stage the peers data for updating of the company tables
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


@related.immutable
class zsPeerRecord:
    """
    This class maps to the zs_peer table in the database_old and is used
    to stage the peers data for updating of the company tables
    """
    id: int = related.IntegerField(default=0)
    ticker: str = _core.TickerField(default='')
    peer: str = _core.TickerField(default='')


@related.immutable
class zsSectorRecord:
    """
    This class maps to the zs_sector table in the database_old and is used
    to stage the sectors data for updating of the company tables
    """
    id: int = related.IntegerField(default=0)
    name: str = related.StringField(default='')
    is_active: bool = _core.FlagField(default=True)


@related.immutable
class zsIndustryRecord:
    """
    This class maps to the zs_industry table in the database_old and is used
    to stage the sectors data for updating of the company tables
    """
    id: int = related.IntegerField(default=0)
    name: str = related.StringField(default='')
    sector_id: int = related.IntegerField(default=0)
    is_active: bool = _core.FlagField(default=True)
