"""z_morningstar_profile create

Revision ID: dcfafc513598
Revises: 147fd37ca3be
Create Date: 2022-10-24 17:54:04.155350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcfafc513598'
down_revision = '147fd37ca3be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_morningstar_profile',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('company_name', sa.String(length=250), nullable=True),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('sector', sa.String(length=50), nullable=True),
                    sa.Column('industry', sa.String(length=50), nullable=True),
                    sa.Column('recent_earnings', sa.String(length=50), nullable=True),
                    sa.Column('fiscal_year_end', sa.String(length=50), nullable=True),
                    sa.Column('stock_type', sa.String(length=50), nullable=True),
                    sa.Column('employees', sa.String(length=50), nullable=True))
    op.create_index('z_morningstar_profile_ticker', 'z_morningstar_profile', ['ticker'])


def downgrade() -> None:
    op.drop_index('z_morningstar_profile_ticker', 'z_morningstar_profile')
    op.drop_table('z_morningstar_profile')
