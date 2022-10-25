"""balance_sheet audit triggers

Revision ID: 03dd2fd24080
Revises: 55cae9a0d8cd
Create Date: 2022-10-24 19:18:31.668086

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '03dd2fd24080'
down_revision = '55cae9a0d8cd'
branch_labels = None
depends_on = None


_triggers = [
    """
        CREATE TRIGGER balance_sheet_audit_insert 
            AFTER INSERT ON balance_sheet  FOR EACH ROW 
                INSERT INTO xxx_balance_sheet(record_id, audit_action, year, fiscal_year, restated, shares_basic,
                    shares_diluted, cash, accounts_receivable, inventories, current_assets, total_assets, 
                    accounts_payable, current_liabilities, long_term_debt, share_capital, total_capital, 
                    capital_expenditure, cashflow, bnk_inter_bank_assets, bnk_net_loans, bnk_total_deposits, 
                    ins_total_investments, ins_insurance_reserves, ins_policyholders_equity, company_id, lock_version)
                VALUES (NEW.id, 'I', NEW.year, NEW.fiscal_year, NEW.restated, NEW.shares_basic, NEW.shares_diluted, 
                        NEW.cash, NEW.accounts_receivable, NEW.inventories, NEW.current_assets, NEW.total_assets, 
                        NEW.accounts_payable, NEW.current_liabilities, NEW.long_term_debt, NEW.share_capital, 
                        NEW.total_capital, NEW.capital_expenditure, NEW.cashflow, NEW.bnk_inter_bank_assets, 
                        NEW.bnk_net_loans, NEW.bnk_total_deposits, NEW.ins_total_investments, NEW.ins_insurance_reserves, 
                        NEW.ins_policyholders_equity, NEW.company_id, NEW.lock_version);
    """,
    """
        CREATE TRIGGER balance_sheet_audit_update 
            AFTER UPDATE ON balance_sheet  FOR EACH ROW 
                INSERT INTO xxx_balance_sheet(record_id, audit_action, year, fiscal_year, restated, shares_basic,
                    shares_diluted, cash, accounts_receivable, inventories, current_assets, total_assets, 
                    accounts_payable, current_liabilities, long_term_debt, share_capital, total_capital, 
                    capital_expenditure, cashflow, bnk_inter_bank_assets, bnk_net_loans, bnk_total_deposits, 
                    ins_total_investments, ins_insurance_reserves, ins_policyholders_equity, company_id, lock_version)
                VALUES (NEW.id, 'U', NEW.year, NEW.fiscal_year, NEW.restated, NEW.shares_basic, NEW.shares_diluted, 
                        NEW.cash, NEW.accounts_receivable, NEW.inventories, NEW.current_assets, NEW.total_assets, 
                        NEW.accounts_payable, NEW.current_liabilities, NEW.long_term_debt, NEW.share_capital, 
                        NEW.total_capital, NEW.capital_expenditure, NEW.cashflow, NEW.bnk_inter_bank_assets, 
                        NEW.bnk_net_loans, NEW.bnk_total_deposits, NEW.ins_total_investments, NEW.ins_insurance_reserves, 
                        NEW.ins_policyholders_equity, NEW.company_id, NEW.lock_version);
    """,
    """
        CREATE TRIGGER balance_sheet_audit_delete
            AFTER DELETE ON balance_sheet  FOR EACH ROW 
                INSERT INTO xxx_balance_sheet(record_id, audit_action, year, fiscal_year, restated, shares_basic,
                    shares_diluted, cash, accounts_receivable, inventories, current_assets, total_assets, 
                    accounts_payable, current_liabilities, long_term_debt, share_capital, total_capital, 
                    capital_expenditure, cashflow, bnk_inter_bank_assets, bnk_net_loans, bnk_total_deposits, 
                    ins_total_investments, ins_insurance_reserves, ins_policyholders_equity, company_id, lock_version)
                VALUES (OLD.id, 'D', OLD.year, OLD.fiscal_year, OLD.restated, OLD.shares_basic, OLD.shares_diluted, 
                        OLD.cash, OLD.accounts_receivable, OLD.inventories, OLD.current_assets, OLD.total_assets, 
                        OLD.accounts_payable, OLD.current_liabilities, OLD.long_term_debt, OLD.share_capital, 
                        OLD.total_capital, OLD.capital_expenditure, OLD.cashflow, OLD.bnk_inter_bank_assets, 
                        OLD.bnk_net_loans, OLD.bnk_total_deposits, OLD.ins_total_investments, OLD.ins_insurance_reserves, 
                        OLD.ins_policyholders_equity, OLD.company_id, OLD.lock_version);
    """
]

_drop_triggers = [
    "DROP TRIGGER IF EXISTS balance_sheet_audit_insert;",
    "DROP TRIGGER balance_sheet_audit_update;",
    "DROP TRIGGER balance_sheet_audit_delete;"
]


def upgrade() -> None:
    for trigger in _triggers:
        op.execute(trigger)


def downgrade() -> None:
    for trigger_drop in _drop_triggers:
        op.execute(trigger_drop)
