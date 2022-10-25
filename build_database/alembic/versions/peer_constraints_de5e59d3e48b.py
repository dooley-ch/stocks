"""peer constraints

Revision ID: de5e59d3e48b
Revises: 83098452bd0c
Create Date: 2022-10-24 19:08:06.572405

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'de5e59d3e48b'
down_revision = '83098452bd0c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("peer_ukey_ticker_peer", "peer", ["company_id", "peer"])

    op.create_index("peer_idx_company_id", "peer", ["company_id"])
    op.create_index("peer_idx_peer", "peer", ["peer"])

    op.create_check_constraint('xxx_peer_audit_action_check', "xxx_peer", "audit_action in ('I','U','D')")
    op.create_foreign_key("peer_company_id_fkey", "peer", "company", ["company_id"], ["id"])


def downgrade() -> None:
    op.execute("ALTER TABLE peer DROP INDEX peer_ukey_ticker_peer;")

    op.execute("ALTER TABLE peer DROP FOREIGN KEY peer_company_id_fkey;")

    op.drop_index("peer_idx_company_id", "peer")
    op.drop_index("peer_idx_peer", "peer")

    op.execute("ALTER TABLE xxx_peer DROP CHECK xxx_peer_audit_action_check;")
