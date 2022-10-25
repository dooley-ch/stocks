"""peer audit triggers

Revision ID: 55cae9a0d8cd
Revises: 8f1231f43c78
Create Date: 2022-10-24 19:16:36.297157

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '55cae9a0d8cd'
down_revision = '8f1231f43c78'
branch_labels = None
depends_on = None


_triggers = [
    """
        CREATE TRIGGER peer_audit_insert 
            AFTER INSERT ON peer  FOR EACH ROW 
                INSERT INTO xxx_peer(record_id, audit_action, company_id, peer, lock_version)
                VALUES (NEW.id, 'I', NEW.company_id, NEW.peer, NEW.lock_version);
    """,
    """
        CREATE TRIGGER peer_audit_update 
            AFTER UPDATE ON peer  FOR EACH ROW 
                INSERT INTO xxx_peer(record_id, audit_action, company_id, peer, lock_version)
                VALUES (NEW.id, 'U', NEW.company_id, NEW.peer, NEW.lock_version);
    """,
    """
        CREATE TRIGGER peer_audit_delete
            AFTER DELETE ON peer  FOR EACH ROW 
                INSERT INTO xxx_peer(record_id, audit_action, company_id, peer, lock_version)
                VALUES (OLD.id, 'D', OLD.company_id, OLD.peer, OLD.lock_version);
    """
]

_drop_triggers = [
    "DROP TRIGGER peer_audit_insert;",
    "DROP TRIGGER peer_audit_update;",
    "DROP TRIGGER peer_audit_delete;"
]


def upgrade() -> None:
    for trigger in _triggers:
        op.execute(trigger)


def downgrade() -> None:
    for trigger_drop in _drop_triggers:
        op.execute(trigger_drop)
