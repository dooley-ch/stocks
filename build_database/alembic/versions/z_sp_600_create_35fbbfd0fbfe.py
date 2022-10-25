"""z_sp_600 create

Revision ID: 35fbbfd0fbfe
Revises: 25f5953d08da
Create Date: 2022-10-24 17:48:54.617300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35fbbfd0fbfe'
down_revision = '25f5953d08da'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_sp_600',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('company', sa.String(length=250), nullable=False),
                    sa.Column('industry', sa.String(length=250), nullable=True))

    op.create_unique_constraint("z_sp_600_ticker", "z_sp_600", ["ticker"])


def downgrade() -> None:
    op.execute("ALTER TABLE z_sp_600 DROP INDEX z_sp_600_ticker;")
    op.drop_table('z_sp_600')
