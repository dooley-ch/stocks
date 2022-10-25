"""z_sp_100 create

Revision ID: 25f5953d08da
Revises: e52b25ca5bdb
Create Date: 2022-10-24 17:47:53.520482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25f5953d08da'
down_revision = 'e52b25ca5bdb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_sp_100',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('company', sa.String(length=250), nullable=False),
                    sa.Column('industry', sa.String(length=250), nullable=True))

    op.create_unique_constraint("z_sp_100_ticker", "z_sp_100", ["ticker"])


def downgrade() -> None:
    op.execute("ALTER TABLE z_sp_100 DROP INDEX z_sp_100_ticker;")
    op.drop_table('z_sp_100')
