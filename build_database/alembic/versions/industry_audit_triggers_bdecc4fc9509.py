"""industry audit triggers

Revision ID: bdecc4fc9509
Revises: 03dd2fd24080
Create Date: 2022-10-24 19:21:44.361804

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'bdecc4fc9509'
down_revision = '03dd2fd24080'
branch_labels = None
depends_on = None


_triggers = [
    """
        CREATE TRIGGER industry_audit_insert 
            AFTER INSERT ON industry  FOR EACH ROW 
                INSERT INTO xxx_industry(record_id, audit_action, name, sector_id, is_active, lock_version)
                VALUES (NEW.id, 'I', NEW.name, NEW.sector_id, NEW.is_active, NEW.lock_version);    
    """,
    """
        CREATE TRIGGER industry_audit_update 
            AFTER UPDATE ON industry  FOR EACH ROW 
                INSERT INTO xxx_industry(record_id, audit_action, name, sector_id, is_active, lock_version)
                VALUES (NEW.id, 'U', NEW.name, NEW.sector_id, NEW.is_active, NEW.lock_version);    
    """,
    """
        CREATE TRIGGER industry_audit_delete
            AFTER DELETE ON industry  FOR EACH ROW 
                INSERT INTO xxx_industry(record_id, audit_action, name, sector_id, is_active, lock_version)
                VALUES (OLD.id, 'D', OLD.name, OLD.sector_id, OLD.is_active, OLD.lock_version);    
    """
]

_drop_triggers = [
    "DROP TRIGGER industry_audit_insert;",
    "DROP TRIGGER industry_audit_update;",
    "DROP TRIGGER industry_audit_delete;"
]


def upgrade() -> None:
    for trigger in _triggers:
        op.execute(trigger)


def downgrade() -> None:
    for trigger_drop in _drop_triggers:
        op.execute(trigger_drop)
