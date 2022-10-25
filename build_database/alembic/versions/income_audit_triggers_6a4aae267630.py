"""income audit triggers

Revision ID: 6a4aae267630
Revises: bdecc4fc9509
Create Date: 2022-10-24 19:24:08.939927

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '6a4aae267630'
down_revision = 'bdecc4fc9509'
branch_labels = None
depends_on = None


_triggers = [
    """
        CREATE TRIGGER income_audit_insert 
            AFTER INSERT ON income  FOR EACH ROW 
                INSERT INTO xxx_income(record_id, audit_action, fiscal_year,
                    restated, revenue, gross_profit, depreciation, interest_expense, pretax_income, tax,
                    net_income, net_income_core, bnk_provision_for_loan_losses, bnk_operating_income, ins_total_claims, 
                    ins_operating_income, company_id, lock_version)
                VALUES (NEW.id, 'I', NEW.fiscal_year, NEW.restated, 
                        NEW.revenue, NEW.gross_profit, NEW.depreciation, NEW.interest_expense, NEW.pretax_income, 
                        NEW.tax, NEW.net_income, NEW.net_income_core, NEW.bnk_provision_for_loan_losses, 
                        NEW.bnk_operating_income, NEW.ins_total_claims, NEW.ins_operating_income, NEW.company_id, 
                        NEW.lock_version);
    """,
    """
        CREATE TRIGGER income_audit_update 
            AFTER UPDATE ON income  FOR EACH ROW 
                INSERT INTO xxx_income(record_id, audit_action, fiscal_year,
                    restated, revenue, gross_profit, depreciation, interest_expense, pretax_income, tax,
                    net_income, net_income_core, bnk_provision_for_loan_losses, bnk_operating_income, ins_total_claims, 
                    ins_operating_income, company_id, lock_version)
                VALUES (NEW.id, 'U', NEW.fiscal_year, NEW.restated, 
                        NEW.revenue, NEW.gross_profit, NEW.depreciation, NEW.interest_expense, NEW.pretax_income, 
                        NEW.tax, NEW.net_income, NEW.net_income_core, NEW.bnk_provision_for_loan_losses, 
                        NEW.bnk_operating_income, NEW.ins_total_claims, NEW.ins_operating_income, NEW.company_id, 
                        NEW.lock_version);
    """,
    """
        CREATE TRIGGER income_audit_delete
            AFTER DELETE ON income  FOR EACH ROW 
                INSERT INTO xxx_income(record_id, audit_action, fiscal_year,
                    restated, revenue, gross_profit, depreciation, interest_expense, pretax_income, tax,
                    net_income, net_income_core, bnk_provision_for_loan_losses, bnk_operating_income, ins_total_claims, 
                    ins_operating_income, company_id, lock_version)
                VALUES (OLD.id, 'D', OLD.fiscal_year, OLD.restated, 
                        OLD.revenue, OLD.gross_profit, OLD.depreciation, OLD.interest_expense, OLD.pretax_income, 
                        OLD.tax, OLD.net_income, OLD.net_income_core, OLD.bnk_provision_for_loan_losses, 
                        OLD.bnk_operating_income, OLD.ins_total_claims, OLD.ins_operating_income, OLD.company_id, 
                        OLD.lock_version);
    """
]

_drop_triggers = [
    "DROP TRIGGER income_audit_insert;",
    "DROP TRIGGER income_audit_update;",
    "DROP TRIGGER income_audit_delete;"
]


def upgrade() -> None:
    for trigger in _triggers:
        op.execute(trigger)


def downgrade() -> None:
    for trigger_drop in _drop_triggers:
        op.execute(trigger_drop)
