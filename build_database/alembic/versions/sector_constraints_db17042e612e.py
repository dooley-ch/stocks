"""sector constraints

Revision ID: db17042e612e
Revises: de5e59d3e48b
Create Date: 2022-10-24 19:10:49.569858

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'db17042e612e'
down_revision = 'de5e59d3e48b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint("sector_ukey_name", "sector", ["name"])
    op.create_check_constraint('xxx_sector_audit_action_check', "xxx_sector", "audit_action in ('I','U','D')")


def downgrade() -> None:
    op.execute("ALTER TABLE sector DROP INDEX sector_ukey_name;")
    op.execute("ALTER TABLE xxx_sector DROP CHECK xxx_sector_audit_action_check;")
