"""_seed data insert

Revision ID: f7772faafe3c
Revises: ce6641b8f36f
Create Date: 2022-10-24 20:03:31.196975

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f7772faafe3c'
down_revision = 'ce6641b8f36f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("INSERT INTO company_type(id, name, is_active) VALUES (1, 'General', 1);")
    op.execute("INSERT INTO company_type(id, name, is_active) VALUES (2, 'Bank', 1);")
    op.execute("INSERT INTO company_type(id, name, is_active) VALUES (3, 'Insurance', 1);")
    op.execute("INSERT INTO company_type(id, name, is_active) VALUES (4, 'Unknown', 1);")

    op.execute("INSERT INTO sector(name) VALUES ('Unknown');")
    op.execute("INSERT INTO industry(name, sector_id) VALUES ('Unknown', 1);")


def downgrade() -> None:
    pass
