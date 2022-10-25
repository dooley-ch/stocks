"""z_sp_500 create

Revision ID: 147fd37ca3be
Revises: bfa9c0319f0f
Create Date: 2022-10-24 17:51:57.894136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '147fd37ca3be'
down_revision = 'bfa9c0319f0f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_sp_500',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('company', sa.String(length=250), nullable=False),
                    sa.Column('industry', sa.String(length=250), nullable=True))
    op.create_unique_constraint("z_sp_500_ticker", "z_sp_500", ["ticker"])


def downgrade() -> None:
    op.execute("ALTER TABLE z_sp_500 DROP INDEX z_sp_500_ticker;")
    op.drop_table('z_sp_500')
