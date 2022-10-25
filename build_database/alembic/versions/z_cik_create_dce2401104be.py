"""z_cik create

Revision ID: dce2401104be
Revises: 0469ccbba646
Create Date: 2022-10-24 18:00:56.425325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dce2401104be'
down_revision = '0469ccbba646'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_cik',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('company', sa.String(length=250), nullable=False),
                    sa.Column('exchange', sa.String(length=50), nullable=False),
                    sa.Column('cik', sa.String(length=10), nullable=False))

    op.create_unique_constraint("z_cik_ticker", "z_cik", ["ticker"])


def downgrade() -> None:
    op.execute("ALTER TABLE z_cik DROP INDEX z_cik_ticker;")
    op.drop_table('z_cik')
