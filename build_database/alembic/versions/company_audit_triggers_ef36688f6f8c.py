"""company audit triggers

Revision ID: ef36688f6f8c
Revises: 6a4aae267630
Create Date: 2022-10-24 19:25:49.954463

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ef36688f6f8c'
down_revision = '6a4aae267630'
branch_labels = None
depends_on = None


_triggers = [
    """
        CREATE TRIGGER company_audit_insert 
            AFTER INSERT ON company  FOR EACH ROW 
                INSERT INTO xxx_company(record_id, audit_action, ticker, name, currency, description, stock_exchange, 
                                        cik_number, figi_code, simfin_number, is_sp100, is_sp400, is_sp500, is_sp600, 
                                        company_type_id, industry_id, is_active, has_financials, lock_version)
                VALUES (NEW.id, 'I', NEW.ticker, NEW.name, NEW.currency, NEW.description, NEW.stock_exchange, NEW.cik_number,
                        NEW.figi_code, NEW.simfin_number, NEW.is_sp100, NEW.is_sp400, NEW.is_sp500, NEW.is_sp600,
                        NEW.company_type_id, NEW.industry_id, NEW.is_active, NEW.has_financials, NEW.lock_version);
    """,
    """
       CREATE TRIGGER company_audit_update 
            AFTER UPDATE ON company  FOR EACH ROW 
                INSERT INTO xxx_company(record_id, audit_action, ticker, name, currency, description, stock_exchange, 
                                        cik_number, figi_code, simfin_number, is_sp100, is_sp400, is_sp500, is_sp600, 
                                        company_type_id, industry_id, is_active, has_financials, lock_version)
                VALUES (NEW.id, 'U', NEW.ticker, NEW.name, NEW.currency, NEW.description, NEW.stock_exchange, NEW.cik_number,
                        NEW.figi_code, NEW.simfin_number, NEW.is_sp100, NEW.is_sp400, NEW.is_sp500, NEW.is_sp600,
                        NEW.company_type_id, NEW.industry_id, NEW.is_active, NEW.has_financials, NEW.lock_version);
    """,
    """
       CREATE TRIGGER company_audit_delete 
            AFTER DELETE ON company  FOR EACH ROW 
                INSERT INTO xxx_company(record_id, audit_action, ticker, name, currency, description, stock_exchange, 
                                        cik_number, figi_code, simfin_number, is_sp100, is_sp400, is_sp500, is_sp600, 
                                        company_type_id, industry_id, is_active, has_financials, lock_version)
                VALUES (OLD.id, 'D', OLD.ticker, OLD.name, OLD.currency, OLD.description, OLD.stock_exchange, OLD.cik_number,
                        OLD.figi_code, OLD.simfin_number, OLD.is_sp100, OLD.is_sp400, OLD.is_sp500, OLD.is_sp600,
                        OLD.company_type_id, OLD.industry_id, OLD.is_active, OLD.has_financials, OLD.lock_version);
    """
]

_drop_triggers = [
    "DROP TRIGGER company_audit_insert;",
    "DROP TRIGGER company_audit_update;",
    "DROP TRIGGER company_audit_delete;",
]


def upgrade() -> None:
    for trigger in _triggers:
        op.execute(trigger)


def downgrade() -> None:
    for trigger_drop in _drop_triggers:
        op.execute(trigger_drop)
