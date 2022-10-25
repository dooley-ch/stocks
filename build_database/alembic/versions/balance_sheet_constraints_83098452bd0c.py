"""balance_sheet constraints

Revision ID: 83098452bd0c
Revises: aadbbd8b3bf6
Create Date: 2022-10-24 19:05:47.283212

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '83098452bd0c'
down_revision = 'aadbbd8b3bf6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_check_constraint('xxx_balance_sheet_audit_action_check', "xxx_balance_sheet", "audit_action in ('I','U','D')")
    op.create_foreign_key("balance_sheet_company_id_fkey", "balance_sheet", "company", ["company_id"], ["id"])


def downgrade() -> None:
    op.execute("ALTER TABLE xxx_balance_sheet DROP CHECK xxx_balance_sheet_audit_action_check;")
    op.execute("ALTER TABLE balance_sheet DROP FOREIGN KEY balance_sheet_company_id_fkey;")
