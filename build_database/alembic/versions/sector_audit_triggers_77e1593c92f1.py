"""sector audit triggers

Revision ID: 77e1593c92f1
Revises: ef36688f6f8c
Create Date: 2022-10-24 19:27:21.472123

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '77e1593c92f1'
down_revision = 'ef36688f6f8c'
branch_labels = None
depends_on = None


_triggers = [
    """
        CREATE TRIGGER sector_audit_insert 
            AFTER INSERT ON sector  FOR EACH ROW 
                INSERT INTO xxx_sector(record_id, audit_action, name, is_active, lock_version)
                VALUES (NEW.id, 'I', NEW.name, NEW.is_active, NEW.lock_version);
    """,
    """
        CREATE TRIGGER sector_audit_update 
            AFTER UPDATE ON sector  FOR EACH ROW 
                INSERT INTO xxx_sector(record_id, audit_action, name, is_active, lock_version)
                VALUES (NEW.id, 'U', NEW.name, NEW.is_active, NEW.lock_version);
    """,
    """
        CREATE TRIGGER sector_audit_delete
            AFTER DELETE ON sector  FOR EACH ROW 
                INSERT INTO xxx_sector(record_id, audit_action, name, is_active, lock_version)
                VALUES (OLD.id, 'D', OLD.name, OLD.is_active, OLD.lock_version);
    """
]

_drop_triggers = [
    "DROP TRIGGER sector_audit_insert;",
    "DROP TRIGGER sector_audit_update;",
    "DROP TRIGGER sector_audit_delete;"
]


def upgrade() -> None:
    for trigger in _triggers:
        op.execute(trigger)


def downgrade() -> None:
    for trigger_drop in _drop_triggers:
        op.execute(trigger_drop)
