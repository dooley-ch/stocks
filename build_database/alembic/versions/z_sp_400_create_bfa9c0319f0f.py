"""z_sp_400 create

Revision ID: bfa9c0319f0f
Revises: 35fbbfd0fbfe
Create Date: 2022-10-24 17:50:12.285447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfa9c0319f0f'
down_revision = '35fbbfd0fbfe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_sp_400',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('company', sa.String(length=250), nullable=False),
                    sa.Column('industry', sa.String(length=250), nullable=True))
    op.create_unique_constraint("z_sp_400_ticker", "z_sp_400", ["ticker"])


def downgrade() -> None:
    op.execute("ALTER TABLE z_sp_400 DROP INDEX z_sp_400_ticker;")
    op.drop_table('z_sp_400')
