"""per_share constraints

Revision ID: 8f1231f43c78
Revises: a5d18faa8aff
Create Date: 2022-10-24 19:14:29.624446

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '8f1231f43c78'
down_revision = 'a5d18faa8aff'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_check_constraint('xxx_per_share_audit_action_check', "xxx_per_share", "audit_action in ('I','U','D')")
    op.create_foreign_key("per_share_company_id_fkey", "per_share", "company", ["company_id"], ["id"])
    op.create_unique_constraint("per_share_ukey_company_id", "per_share", ["company_id"])


def downgrade() -> None:
    op.execute("ALTER TABLE xxx_per_share DROP CHECK xxx_per_share_audit_action_check;")
    op.execute("ALTER TABLE per_share DROP FOREIGN KEY per_share_company_id_fkey;")
    op.execute("ALTER TABLE per_share DROP INDEX per_share_ukey_company_id;")
