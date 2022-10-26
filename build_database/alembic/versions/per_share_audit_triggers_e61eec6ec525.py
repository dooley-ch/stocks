"""per_share audit triggers

Revision ID: e61eec6ec525
Revises: 77e1593c92f1
Create Date: 2022-10-24 19:29:01.625125

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'e61eec6ec525'
down_revision = '77e1593c92f1'
branch_labels = None
depends_on = None


_triggers = [
    """
        CREATE TRIGGER per_share_audit_insert 
            AFTER INSERT ON per_share  FOR EACH ROW 
                INSERT INTO xxx_per_share(record_id, audit_action, year, fiscal_year, restated, book_value, cashflow, earnings, 
                                dividends, payout_ratio, company_id, lock_version)
                VALUES (NEW.id, 'I', NEW.year, NEW.fiscal_year, NEW.restated, 
                        NEW.book_value, NEW.cashflow, NEW.earnings, NEW.dividends, NEW.payout_ratio, NEW.company_id, NEW.lock_version);
    """,
    """
        CREATE TRIGGER per_share_audit_update 
            AFTER UPDATE ON per_share  FOR EACH ROW 
                INSERT INTO xxx_per_share(record_id, audit_action, year, fiscal_year, restated, book_value, cashflow, earnings, 
                    dividends, payout_ratio, company_id, lock_version)
                VALUES (NEW.id, 'U', NEW.year, NEW.fiscal_year, NEW.restated,  NEW.book_value, NEW.cashflow, NEW.earnings, 
                        NEW.dividends, NEW.payout_ratio, NEW.company_id, NEW.lock_version);
    """,
    """
        CREATE TRIGGER per_share_audit_delete
            AFTER DELETE ON per_share  FOR EACH ROW 
                INSERT INTO xxx_per_share(record_id, audit_action, year, fiscal_year, restated, book_value, cashflow, earnings, 
                    dividends, payout_ratio, company_id, lock_version)
                VALUES (OLD.id, 'D', OLD.year, OLD.fiscal_year, OLD.restated,  OLD.book_value, OLD.cashflow, OLD.earnings, 
                        OLD.dividends, OLD.payout_ratio, OLD.company_id, OLD.lock_version);
    """
]

_drop_triggers = [
    "DROP TRIGGER per_share_audit_insert;",
    "DROP TRIGGER per_share_audit_update;",
    "DROP TRIGGER per_share_audit_delete;"
]


def upgrade() -> None:
    for trigger in _triggers:
        op.execute(trigger)


def downgrade() -> None:
    for trigger_drop in _drop_triggers:
        op.execute(trigger_drop)
