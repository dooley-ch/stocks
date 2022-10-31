# *******************************************************************************************
#  File:  _z_income.py
#
#  Created: 28-09-2022
#
#  History:
#  28-09-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['zIncomeInsuranceQuarter_insert', 'zIncomeInsuranceQuarter_get_by_ticker',
           'zIncomeInsuranceAnnual_insert', 'zIncomeInsuranceAnnual_get_by_ticker',
           'zIncomeBankQuarter_insert', 'zIncomeBankQuarter_get_by_ticker',
           'zIncomeBankAnnual_insert', 'zIncomeBankAnnual_get_by_ticker',
           'zIncomeGeneralQuarter_insert', 'zIncomeGeneralQuarter_get_by_ticker',
           'zIncomeGeneralAnnual_insert', 'zIncomeGeneralAnnual_get_by_ticker']

import related
import pymysql
from .. model import zIncomeGeneralAnnualRecord, zIncomeGeneralQuarterRecord, zIncomeBankAnnualRecord, \
    zIncomeBankQuarterRecord, zIncomeInsuranceAnnualRecord, zIncomeInsuranceQuarterRecord


def zIncomeInsuranceQuarter_insert(record: zIncomeInsuranceQuarterRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_income_insurance_quarter (ticker, simfin_id, currency, fiscal_year, 
                                fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                revenue, total_claims_losses, operating_income_loss, pretax_income_loss, 
                                income_tax_expense_benefit_net, income_loss_from_affiliates_net_of_taxes, 
                                income_loss_from_continuing_operations, net_extraordinary_gains_losses, net_income, 
                                net_income_common) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.revenue, record.total_claims_losses, record.operating_income_loss,
                        record.pretax_income_loss, record.income_tax_expense_benefit_net,
                        record.income_loss_from_affiliates_net_of_taxes, record.income_loss_from_continuing_operations,
                        record.net_extraordinary_gains_losses, record.net_income, record.net_income_common))
        return cursor.lastrowid


def zIncomeInsuranceQuarter_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zIncomeInsuranceQuarterRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                                restated_date, 
                                IF(shares_basic = '', '0', shares_basic) AS shares_basic, 
                                IF(shares_diluted = '', '0', shares_diluted) AS shares_diluted,
                                IF(revenue = '', 'NaN', revenue) AS revenue, 
                                IF(total_claims_losses = '', 'NaN', total_claims_losses) AS total_claims_losses, 
                                IF(operating_income_loss = '', 'NaN', operating_income_loss) AS operating_income_loss, 
                                IF(pretax_income_loss = '', 'NaN', pretax_income_loss) AS pretax_income_loss, 
                                IF(income_tax_expense_benefit_net = '', 'NaN', income_tax_expense_benefit_net) AS income_tax_expense_benefit_net, 
                                IF(income_loss_from_affiliates_net_of_taxes = '', 'NaN', income_loss_from_affiliates_net_of_taxes) AS income_loss_from_affiliates_net_of_taxes, 
                                IF(income_loss_from_continuing_operations = '', 'NaN', income_loss_from_continuing_operations) AS income_loss_from_continuing_operations, 
                                IF(net_extraordinary_gains_losses = '', 'NaN', net_extraordinary_gains_losses) AS net_extraordinary_gains_losses, 
                                IF(net_income = '', 'NaN', net_income) AS net_income, 
                                IF(net_income = '', 'NaN', net_income) AS net_income  
                            FROM z_income_insurance_quarter WHERE (ticker = %s)
                            ORDER BY fiscal_year DESC, fiscal_period DESC LIMIT 8;""", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zIncomeInsuranceQuarterRecord, row)
                records.append(record)
            return records


def zIncomeInsuranceAnnual_insert(record: zIncomeInsuranceAnnualRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_income_insurance_annual (ticker, simfin_id, currency, fiscal_year, 
                                fiscal_period, report_date, publish_date, restated_date, shares_basic, shares_diluted, 
                                revenue, total_claims_losses, operating_income_loss, pretax_income_loss, 
                                income_tax_expense_benefit_net, income_loss_from_affiliates_net_of_taxes, 
                                income_loss_from_continuing_operations, net_extraordinary_gains_losses, net_income, 
                                net_income_common) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.revenue, record.total_claims_losses, record.operating_income_loss,
                        record.pretax_income_loss, record.income_tax_expense_benefit_net,
                        record.income_loss_from_affiliates_net_of_taxes, record.income_loss_from_continuing_operations,
                        record.net_extraordinary_gains_losses, record.net_income, record.net_income_common))
        return cursor.lastrowid


def zIncomeInsuranceAnnual_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zIncomeInsuranceAnnualRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                                restated_date, shares_basic, shares_diluted, 
                                IF(revenue = '', 'NaN', revenue) AS revenue, 
                                IF(total_claims_losses = '', 'NaN', total_claims_losses) AS total_claims_losses, 
                                IF(operating_income_loss = '', 'NaN', operating_income_loss) AS operating_income_loss, 
                                IF(pretax_income_loss = '', 'NaN', pretax_income_loss) AS pretax_income_loss, 
                                IF(income_tax_expense_benefit_net = '', 'NaN', income_tax_expense_benefit_net) AS income_tax_expense_benefit_net, 
                                IF(income_loss_from_affiliates_net_of_taxes = '', 'NaN', income_loss_from_affiliates_net_of_taxes) AS income_loss_from_affiliates_net_of_taxes, 
                                IF(income_loss_from_continuing_operations = '', 'NaN', income_loss_from_continuing_operations) AS income_loss_from_continuing_operations, 
                                IF(net_extraordinary_gains_losses = '', 'NaN', net_extraordinary_gains_losses) AS net_extraordinary_gains_losses, 
                                IF(net_income = '', 'NaN', net_income) AS net_income, 
                                IF(net_income = '', 'NaN', net_income) AS net_income  
                            FROM z_income_insurance_annual WHERE (ticker = %s) ORDER BY fiscal_year LIMIT 10;""", (ticker,))

        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(zIncomeInsuranceAnnualRecord, row)
                records.append(record)

            return records


def zIncomeGeneralQuarter_insert(record: zIncomeGeneralQuarterRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_income_general_quarter (ticker, simfin_id, currency, fiscal_year, 
        fiscal_period, 
                            report_date, publish_date, restated_date, shares_basic, shares_diluted, revenue, 
                            cost_of_revenue, gross_profit, operating_expenses, selling_general_administrative, 
                            research_development, depreciation_amortization, operating_income, non_operating_income, 
                            interest_expense_net, pretax_income_loss_adj, abnormal_gains_lLosses, pretax_income_loss, 
                            income_tax_expense_benefit_net, income_loss_from_continuing_operations, 
                            net_extraordinary_gains_losses, net_income, net_income_common) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.revenue, record.cost_of_revenue, record.gross_profit,
                        record.operating_income, record.selling_general_administrative, record.research_development,
                        record.depreciation_amortization, record.operating_income, record.non_operating_income,
                        record.interest_expense_net, record.pretax_income_loss_adj, record.abnormal_gains_lLosses,
                        record.pretax_income_loss, record.income_tax_expense_benefit_net,
                        record.income_loss_from_continuing_operations, record.net_extraordinary_gains_losses,
                        record.net_income, record.net_income_common))
        return cursor.lastrowid


def zIncomeGeneralQuarter_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zIncomeGeneralQuarterRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                            restated_date, 
                            IF(shares_basic = '', '0', shares_basic) AS shares_basic, 
                            IF(shares_diluted = '', '0', shares_diluted) AS shares_diluted,
                            IF(revenue = '', 'NaN', revenue) AS revenue, 
                            IF(cost_of_revenue = '', 'NaN', cost_of_revenue) AS cost_of_revenue, 
                            IF(gross_profit = '', 'NaN', gross_profit) AS gross_profit, 
                            IF(operating_expenses = '', 'NaN', operating_expenses) AS operating_expenses, 
                            IF(selling_general_administrative = '', 'NaN', selling_general_administrative) AS selling_general_administrative, 
                            IF(research_development = '', 'NaN', research_development) AS research_development, 
                            IF(depreciation_amortization = '', 'NaN', depreciation_amortization) AS depreciation_amortization, 
                            IF(operating_income = '', 'NaN', operating_income) AS operating_income, 
                            IF(non_operating_income = '', 'NaN', non_operating_income) AS non_operating_income, 
                            IF(interest_expense_net = '', 'NaN', interest_expense_net) AS interest_expense_net, 
                            IF(pretax_income_loss_adj = '', 'NaN', pretax_income_loss_adj) AS pretax_income_loss_adj, 
                            IF(abnormal_gains_lLosses = '', 'NaN', abnormal_gains_lLosses) AS abnormal_gains_lLosses, 
                            IF(pretax_income_loss = '', 'NaN', pretax_income_loss) AS pretax_income_loss, 
                            IF(income_tax_expense_benefit_net = '', 'NaN', income_tax_expense_benefit_net) AS income_tax_expense_benefit_net, 
                            IF(income_loss_from_continuing_operations = '', 'NaN', income_loss_from_continuing_operations) AS income_loss_from_continuing_operations, 
                            IF(net_extraordinary_gains_losses = '', 'NaN', net_extraordinary_gains_losses) AS net_extraordinary_gains_losses, 
                            IF(net_income = '', 'NaN', net_income) AS net_income, 
                            IF(net_income_common = '', 'NaN', net_income_common) AS net_income_common
                            FROM z_income_general_quarter WHERE (ticker = %s) 
                            ORDER BY fiscal_year DESC, fiscal_period DESC LIMIT 8;""", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zIncomeGeneralQuarterRecord, row)
                records.append(record)
            return records


def zIncomeGeneralAnnual_insert(record: zIncomeGeneralAnnualRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_income_general_Annual (ticker, simfin_id, currency, fiscal_year, fiscal_period, 
                            report_date, publish_date, restated_date, shares_basic, shares_diluted, revenue, 
                            cost_of_revenue, gross_profit, operating_expenses, selling_general_administrative, 
                            research_development, depreciation_amortization, operating_income, non_operating_income, 
                            interest_expense_net, pretax_income_loss_adj, abnormal_gains_lLosses, pretax_income_loss, 
                            income_tax_expense_benefit_net, income_loss_from_continuing_operations, 
                            net_extraordinary_gains_losses, net_income, net_income_common) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.revenue, record.cost_of_revenue, record.gross_profit,
                        record.operating_income, record.selling_general_administrative, record.research_development,
                        record.depreciation_amortization, record.operating_income, record.non_operating_income,
                        record.interest_expense_net, record.pretax_income_loss_adj, record.abnormal_gains_lLosses,
                        record.pretax_income_loss, record.income_tax_expense_benefit_net,
                        record.income_loss_from_continuing_operations, record.net_extraordinary_gains_losses,
                        record.net_income, record.net_income_common))
        return cursor.lastrowid


def zIncomeGeneralAnnual_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zIncomeGeneralAnnualRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                            restated_date, shares_basic, shares_diluted, 
                            IF(revenue = '', 'NaN', revenue) AS revenue, 
                            IF(cost_of_revenue = '', 'NaN', cost_of_revenue) AS cost_of_revenue, 
                            IF(gross_profit = '', 'NaN', gross_profit) AS gross_profit, 
                            IF(operating_expenses = '', 'NaN', operating_expenses) AS operating_expenses, 
                            IF(selling_general_administrative = '', 'NaN', selling_general_administrative) AS selling_general_administrative, 
                            IF(research_development = '', 'NaN', research_development) AS research_development, 
                            IF(depreciation_amortization = '', 'NaN', depreciation_amortization) AS depreciation_amortization, 
                            IF(operating_income = '', 'NaN', operating_income) AS operating_income, 
                            IF(non_operating_income = '', 'NaN', non_operating_income) AS non_operating_income, 
                            IF(interest_expense_net = '', 'NaN', interest_expense_net) AS interest_expense_net, 
                            IF(pretax_income_loss_adj = '', 'NaN', pretax_income_loss_adj) AS pretax_income_loss_adj, 
                            IF(abnormal_gains_lLosses = '', 'NaN', abnormal_gains_lLosses) AS abnormal_gains_lLosses, 
                            IF(pretax_income_loss = '', 'NaN', pretax_income_loss) AS pretax_income_loss, 
                            IF(income_tax_expense_benefit_net = '', 'NaN', income_tax_expense_benefit_net) AS income_tax_expense_benefit_net, 
                            IF(income_loss_from_continuing_operations = '', 'NaN', income_loss_from_continuing_operations) AS income_loss_from_continuing_operations, 
                            IF(net_extraordinary_gains_losses = '', 'NaN', net_extraordinary_gains_losses) AS net_extraordinary_gains_losses, 
                            IF(net_income = '', 'NaN', net_income) AS net_income, 
                            IF(net_income_common = '', 'NaN', net_income_common) AS net_income_common
                            FROM z_income_general_annual WHERE (ticker = %s) ORDER BY fiscal_year LIMIT 10;""", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()

            for row in rows:
                record = related.to_model(zIncomeGeneralAnnualRecord, row)
                records.append(record)

            return records


def zIncomeBankQuarter_insert(record: zIncomeBankQuarterRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_income_bank_quarter (ticker, simfin_id, currency, fiscal_year, fiscal_period, 
                            report_date, publish_date, restated_date, shares_basic, shares_diluted, revenue, 
                            provision_for_loan_losses, net_Revenue_after_provisions, total_non_interest_expense, 
                            operating_income_loss, non_operating_income_loss, pretax_income_loss, 
                            income_tax_expense_benefit_net, income_loss_from_continuing_operations, 
                            net_extraordinary_gains_losses, net_income, net_income_Common) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                                %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.revenue, record.provision_for_loan_losses,
                        record.net_Revenue_after_provisions, record.total_non_interest_expense,
                        record.operating_income_loss, record.non_operating_income_loss, record.pretax_income_loss,
                        record.income_tax_expense_benefit_net, record.income_loss_from_continuing_operations,
                        record.net_extraordinary_gains_losses, record.net_income, record.net_income_Common))
        return cursor.lastrowid


def zIncomeBankQuarter_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zIncomeBankQuarterRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                            restated_date, 
                            IF(shares_basic = '', '0', shares_basic) AS shares_basic, 
                            IF(shares_diluted = '', '0', shares_diluted) AS shares_diluted,
                            IF(revenue = '', 'NaN', revenue) AS revenue, 
                            IF(provision_for_loan_losses = '', 'NaN', provision_for_loan_losses) AS provision_for_loan_losses, 
                            IF(net_Revenue_after_provisions = '', 'NaN', net_Revenue_after_provisions) AS net_Revenue_after_provisions, 
                            IF(total_non_interest_expense = '', 'NaN', total_non_interest_expense) AS total_non_interest_expense, 
                            IF(operating_income_loss = '', 'NaN', operating_income_loss) AS operating_income_loss, 
                            IF(non_operating_income_loss = '', 'NaN', non_operating_income_loss) AS non_operating_income_loss, 
                            IF(pretax_income_loss = '', 'NaN', pretax_income_loss) AS pretax_income_loss, 
                            IF(income_tax_expense_benefit_net = '', 'NaN', income_tax_expense_benefit_net) AS income_tax_expense_benefit_net, 
                            IF(income_loss_from_continuing_operations = '', 'NaN', income_loss_from_continuing_operations) AS income_loss_from_continuing_operations, 
                            IF(net_extraordinary_gains_losses = '', 'NaN', net_extraordinary_gains_losses) AS net_extraordinary_gains_losses, 
                            IF(net_income = '', 'NaN', net_income) AS net_income, 
                            IF(net_income_Common = '', 'NaN', net_income_Common) AS net_income_Common
                            FROM z_income_bank_quarter WHERE (ticker = %s)
                            ORDER BY fiscal_year DESC, fiscal_period DESC LIMIT 8;""", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zIncomeBankQuarterRecord, row)
                records.append(record)
            return records


def zIncomeBankAnnual_insert(record: zIncomeBankAnnualRecord, db_conn: pymysql.Connection) -> int | None:
    """
    This function inserts a record in the database_old
    :param record: the record to insert
    :param db_conn: the database_old connection to use
    :return: the id of the new record, or none it fails
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""INSERT INTO z_income_bank_annual (ticker, simfin_id, currency, fiscal_year, fiscal_period, 
                            report_date, publish_date, restated_date, shares_basic, shares_diluted, revenue, 
                            provision_for_loan_losses, net_Revenue_after_provisions, total_non_interest_expense, 
                            operating_income_loss, non_operating_income_loss, pretax_income_loss, 
                            income_tax_expense_benefit_net, income_loss_from_continuing_operations, 
                            net_extraordinary_gains_losses, net_income, net_income_Common) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                       (record.ticker, record.simfin_id, record.currency, record.fiscal_year, record.fiscal_period,
                        record.report_date, record.publish_date, record.restated_date, record.shares_basic,
                        record.shares_diluted, record.revenue, record.provision_for_loan_losses,
                        record.net_Revenue_after_provisions, record.total_non_interest_expense,
                        record.operating_income_loss, record.non_operating_income_loss, record.pretax_income_loss,
                        record.income_tax_expense_benefit_net, record.income_loss_from_continuing_operations,
                        record.net_extraordinary_gains_losses, record.net_income, record.net_income_common))
        return cursor.lastrowid


def zIncomeBankAnnual_get_by_ticker(ticker: str, db_conn: pymysql.Connection) -> list[zIncomeBankAnnualRecord] | None:
    """
    This function returns all record from the table
    :param ticker: the ticker to filter by
    :param db_conn: the database_old connection to use
    :return: the Sector record if one exists
    """
    with db_conn.cursor() as cursor:
        cursor.execute("""SELECT id, ticker, simfin_id, currency, fiscal_year, fiscal_period, report_date, publish_date, 
                            restated_date, shares_basic, shares_diluted, 
                            IF(revenue = '', 'NaN', revenue) AS revenue, 
                            IF(provision_for_loan_losses = '', 'NaN', provision_for_loan_losses) AS provision_for_loan_losses, 
                            IF(net_Revenue_after_provisions = '', 'NaN', net_Revenue_after_provisions) AS net_Revenue_after_provisions, 
                            IF(total_non_interest_expense = '', 'NaN', total_non_interest_expense) AS total_non_interest_expense, 
                            IF(operating_income_loss = '', 'NaN', operating_income_loss) AS operating_income_loss, 
                            IF(non_operating_income_loss = '', 'NaN', non_operating_income_loss) AS non_operating_income_loss, 
                            IF(pretax_income_loss = '', 'NaN', pretax_income_loss) AS pretax_income_loss, 
                            IF(income_tax_expense_benefit_net = '', 'NaN', income_tax_expense_benefit_net) AS income_tax_expense_benefit_net, 
                            IF(income_loss_from_continuing_operations = '', 'NaN', income_loss_from_continuing_operations) AS income_loss_from_continuing_operations, 
                            IF(net_extraordinary_gains_losses = '', 'NaN', net_extraordinary_gains_losses) AS net_extraordinary_gains_losses, 
                            IF(net_income = '', 'NaN', net_income) AS net_income, 
                            IF(net_income_Common = '', 'NaN', net_income_Common) AS net_income_Common
                            FROM z_income_bank_annual WHERE (ticker = %s) ORDER BY fiscal_year LIMIT 10;""", (ticker,))
        rows = cursor.fetchall()
        if rows:
            records = list()
            for row in rows:
                record = related.to_model(zIncomeBankAnnualRecord, row)
                records.append(record)

            return records
