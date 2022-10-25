"""quarter audit triggers

Revision ID: ce6641b8f36f
Revises: 41c08fa38bce
Create Date: 2022-10-24 19:51:03.707860

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ce6641b8f36f'
down_revision = '41c08fa38bce'
branch_labels = None
depends_on = None

_triggers = [
    """
        CREATE TRIGGER quarter_audit_insert 
            AFTER INSERT ON quarter  FOR EACH ROW 
                INSERT INTO xxx_quarter(record_id, audit_action, year, quarter, fiscal_year, restated, shares_basic, 
                                            shares_diluted, revenue, pretax_income, tax, net_income, net_income_core, 
                                            dividends_paid, net_change_in_cash, company_id, lock_version)
                VALUES (NEW.id, 'I', NEW.year, NEW.quarter, NEW.fiscal_year, NEW.restated, NEW.shares_basic, 
                                            NEW.shares_diluted, NEW.revenue, NEW.pretax_income, NEW.tax, 
                                            NEW.net_income, 
                                            NEW.net_income_core, NEW.dividends_paid, NEW.net_change_in_cash, 
                                            NEW.company_id, NEW.lock_version);
    """,
    """
        CREATE TRIGGER quarter_audit_update 
            AFTER UPDATE ON quarter  FOR EACH ROW 
                INSERT INTO xxx_quarter(record_id, audit_action, year, quarter, fiscal_year, restated, shares_basic, 
                                            shares_diluted, revenue, pretax_income, tax, net_income, net_income_core, 
                                            dividends_paid, net_change_in_cash, company_id, lock_version)
                VALUES (NEW.id, 'U', NEW.year, NEW.quarter, NEW.fiscal_year, NEW.restated, NEW.shares_basic, 
                                            NEW.shares_diluted, NEW.revenue, NEW.pretax_income, NEW.tax, 
                                            NEW.net_income, 
                                            NEW.net_income_core, NEW.dividends_paid, NEW.net_change_in_cash, 
                                            NEW.company_id, NEW.lock_version);
    """,
    """
        CREATE TRIGGER quarter_audit_delete
            AFTER DELETE ON quarter  FOR EACH ROW 
                INSERT INTO xxx_quarter(record_id, audit_action, year, quarter, fiscal_year, restated, shares_basic, 
                                            shares_diluted, revenue, pretax_income, tax, net_income, net_income_core, 
                                            dividends_paid, net_change_in_cash, company_id, lock_version)
                VALUES (OLD.id, 'D', OLD.year, OLD.quarter, OLD.fiscal_year, OLD.restated, OLD.shares_basic, 
                                            OLD.shares_diluted, OLD.revenue, OLD.pretax_income, OLD.tax, 
                                            OLD.net_income, 
                                            OLD.net_income_core, OLD.dividends_paid, OLD.net_change_in_cash, 
                                            OLD.company_id, OLD.lock_version);
    """
]

_drop_triggers = [
    "DROP TRIGGER IF EXISTS quarter_audit_insert;",
    "DROP TRIGGER quarter_audit_update;",
    "DROP TRIGGER quarter_audit_delete;"
]


def upgrade() -> None:
    for trigger in _triggers:
        op.execute(trigger)


def downgrade() -> None:
    for trigger_drop in _drop_triggers:
        op.execute(trigger_drop)
