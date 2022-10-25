"""z_master_ticker create

Revision ID: 67eb8b08c24b
Revises: ef93f6e685db
Create Date: 2022-10-24 17:29:18.701758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67eb8b08c24b'
down_revision = 'ef93f6e685db'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_master_ticker',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('company', sa.String(length=250), nullable=False))

    op.create_unique_constraint("z_master_ticker_ticker", "z_master_ticker", ["ticker"])


def downgrade() -> None:
    op.execute("ALTER TABLE z_master_ticker DROP INDEX z_master_ticker_ticker;")
    op.drop_table('z_master_ticker')
