"""z_openfigi create

Revision ID: 97d83133cb16
Revises: dcfafc513598
Create Date: 2022-10-24 17:56:05.638335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97d83133cb16'
down_revision = 'dcfafc513598'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_openfigi',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('open_figi', sa.String(length=12), nullable=True))

    op.create_index('z_openfigi_ticker', 'z_openfigi', ['ticker'])


def downgrade() -> None:
    op.drop_index('z_openfigi_ticker', 'z_openfigi')
    op.drop_table('z_openfigi')
