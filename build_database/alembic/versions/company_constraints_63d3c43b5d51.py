"""company constraints

Revision ID: 63d3c43b5d51
Revises: 45735dc94c2f
Create Date: 2022-10-24 18:57:37.133638

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '63d3c43b5d51'
down_revision = '45735dc94c2f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("company_ukey_ticker", "company", ["ticker"])
    op.create_index("company_idx_name", "company", ["name"])
    op.create_check_constraint('xxx_company_audit_action_check', "xxx_company", "audit_action in ('I','U','D')")
    op.create_foreign_key("company_industry_id_fkey", "company", "industry", ["industry_id"], ["id"])


def downgrade() -> None:
    op.execute("ALTER TABLE company DROP INDEX company_ukey_ticker;")
    op.drop_index("company_idx_name", "company")
    op.execute("ALTER TABLE xxx_company DROP CHECK xxx_company_audit_action_check;")
    op.execute("ALTER TABLE company DROP FOREIGN KEY company_industry_id_fkey;")
