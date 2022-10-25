"""income constraints

Revision ID: a5d18faa8aff
Revises: db17042e612e
Create Date: 2022-10-24 19:12:37.070551

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a5d18faa8aff'
down_revision = 'db17042e612e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_check_constraint('xxx_income_audit_action_check', "xxx_income", "audit_action in ('I','U','D')")
    op.create_foreign_key("income_company_id_fkey", "income", "company", ["company_id"], ["id"])


def downgrade() -> None:
    op.execute("ALTER TABLE xxx_income DROP CHECK xxx_income_audit_action_check;")
    op.execute("ALTER TABLE income DROP FOREIGN KEY income_company_id_fkey;")
