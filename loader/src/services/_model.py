# *******************************************************************************************
#  File:  _services.py
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

__all__ = ['IndexComponent', 'CikComponent', 'FigiData', 'MorningstarProfile', 'SimFinCompany', 'SimFinIndustry',
           'SimFinPrice']

import related
import source.shared.model as model


@related.immutable()
class IndexComponent:
    """
    This class represents a component in one of the S&P indexes
    """
    ticker = related.StringField(required=True)
    name = related.StringField(required=True)
    industry = related.StringField(required=True)

    def to_zSp100(self) -> model.zSp100Record:
        return model.zSp100Record(ticker=self.ticker, company=self.name, industry=self.industry)

    def to_zSp600(self) -> model.zSp600Record:
        return model.zSp600Record(ticker=self.ticker, company=self.name, industry=self.industry)

    def to_zSp400(self) -> model.zSp400Record:
        return model.zSp400Record(ticker=self.ticker, company=self.name, industry=self.industry)

    def to_zSp500(self) -> model.zSp500Record:
        return model.zSp500Record(ticker=self.ticker, company=self.name, industry=self.industry)


@related.immutable()
class CikComponent:
    """
    This class represents a CIK record downloaded from the SEC website
    """
    cik = related.StringField(required=True)
    name = related.StringField(required=True)
    ticker = related.StringField(required=True)
    exchange = related.StringField(required=True)

    def to_zCikRecord(self) -> model.zCikRecord:
        """
        This method converts the object to a database_old record
        """
        return model.zCikRecord(ticker=self.ticker, company=self.name, exchange=self.exchange, cik=self.cik)


@related.immutable()
class FigiData:
    ticker: str = related.StringField()
    name: str = related.StringField(default='')
    figi: str = related.StringField(default='')


@related.immutable()
class MorningstarProfile:
    """
    This class represents the data returned from downloading a profile
    """
    ticker = related.StringField(required=True)
    name = related.StringField(required=True)
    description = related.StringField()
    sector = related.StringField()
    industry = related.StringField()
    recent_earnings = related.StringField()
    fiscal_year_end = related.StringField()
    stock_type = related.StringField()
    employees = related.StringField()

    def to_zMorningstarProfileRecord(self) -> model.zMorningstarProfileRecord:
        """
        This method converts an instance to a zMorningstarProfileRecord instance
        """
        return model.zMorningstarProfileRecord(ticker=self.ticker, company_name=self.name, description=self.description,
                                               sector=self.sector, industry=self.industry,
                                               recent_earnings=self.recent_earnings,
                                               fiscal_year_end=self.fiscal_year_end,
                                               stock_type=self.stock_type, employees=self.employees)


@related.immutable
class SimFinCompany:
    """
    This class represents a company record downloaded from the service provider's website
    """
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    company_name: str = related.StringField(default='')
    industry_id: int = related.IntegerField(default=0)

    def to_zSimFinCompaniesRecord(self) -> model.zSimFinCompaniesRecord:
        return model.zSimFinCompaniesRecord(ticker=self.ticker, company=self.company_name, simfin_id=self.simfin_id,
                                            industry_id=self.industry_id)


@related.immutable
class SimFinIndustry:
    """
    This class represents an industry record downloaded from the service provider
    """
    industry_id: int = related.IntegerField(default=0)
    sector: str = related.StringField(default='')
    industry: str = related.StringField(default='')

    def to_zSimFinIndustriesRecord(self) -> model.zSimFinIndustriesRecord:
        return model.zSimFinIndustriesRecord(industry_id=self.industry_id, sector=self.sector, industry=self.industry)


@related.immutable
class SimFinPrice:
    """
    This class represents a price record downloaded from the service providers website
    """
    ticker: str = related.StringField(default='')
    simfin_id: int = related.IntegerField(default=0)
    date: str = related.StringField(default='')
    open: str = related.StringField(default='')
    low: str = related.StringField(default='')
    high: str = related.StringField(default='')
    close: str = related.StringField(default='')
    adj_close: str = related.StringField(default='')
    dividend: str = related.StringField(default='')
    volume: str = related.StringField(default='')
    shares_outstanding: str = related.StringField(default='')

    def to_zSimFinPrice(self) -> model.zSimFinPrice:
        return model.zSimFinPrice(ticker=self.ticker, simfin_id=self.simfin_id, price_date=self.date,
                                  open_price=self.open, low_price=self.low, high_price=self.high,
                                  close_price=self.close, adjusted_close_price=self.adj_close,
                                  dividend=self.dividend, volume=self.volume,
                                  shares_outstanding=self.shares_outstanding)
