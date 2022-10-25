"""industry constraints

Revision ID: 45735dc94c2f
Revises: b0d25c4b3279
Create Date: 2022-10-24 18:14:53.212872

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '45735dc94c2f'
down_revision = 'b0d25c4b3279'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("industry_ukey_name", "industry", ["name", "sector_id"])
    op.create_check_constraint('xxx_industry_audit_action_check', "xxx_industry", "audit_action in ('I','U','D')")
    op.create_foreign_key("industry_sector_id_fkey", "industry", "sector", ["sector_id"], ["id"])


def downgrade() -> None:
    op.execute("ALTER TABLE industry DROP INDEX industry_ukey_name;")
    op.execute("ALTER TABLE xxx_industry DROP CHECK xxx_industry_audit_action_check;")
    op.execute("ALTER TABLE industry DROP FOREIGN KEY industry_sector_id_fkey;")
