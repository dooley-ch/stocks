"""company_type constraints

Revision ID: aadbbd8b3bf6
Revises: 63d3c43b5d51
Create Date: 2022-10-24 19:03:16.687225

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'aadbbd8b3bf6'
down_revision = '63d3c43b5d51'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("company_type_ukey_name", "company_type", ["name"])
    op.create_check_constraint('xxx_company_type_audit_action_check', "xxx_company_type",
                               "audit_action in ('I','U','D')")
    # Foreign key on Company
    op.create_foreign_key("company_company_type_id_fkey", "company", "company_type", ["company_type_id"], ["id"])


def downgrade() -> None:
    op.execute("ALTER TABLE company_type DROP INDEX company_type_ukey_name;")
    op.execute("ALTER TABLE xxx_company_type DROP CHECK xxx_company_type_audit_action_check;")
    op.execute("ALTER TABLE company DROP FOREIGN KEY company_company_type_id_fkey;")
