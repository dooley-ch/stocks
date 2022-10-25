"""per_share create

Revision ID: 73a497626058
Revises: 3f2ea4ee110f
Create Date: 2022-10-24 16:35:34.351732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73a497626058'
down_revision = '3f2ea4ee110f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('per_share',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('year', sa.Integer(), nullable=True, server_default='0'),
                    sa.Column('fiscal_year', sa.DateTime(), nullable=False),
                    sa.Column('restated', sa.DateTime(), nullable=False),

                    sa.Column('book_value', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('cashflow', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('earnings', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('dividends', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('payout_ratio', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('price_low', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('price_high', sa.String(length=50), nullable=True, server_default='NaN'),

                    sa.Column('company_id', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('lock_version', sa.SmallInteger, server_default='1', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now()))

    op.create_table('xxx_per_share',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('logged_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('audit_action', sa.CHAR(length=1), server_default='I', nullable=False),
                    sa.Column('record_id', sa.Integer(), server_default='0', nullable=False),

                    sa.Column('year', sa.Integer(), nullable=True),
                    sa.Column('fiscal_year', sa.DateTime(), nullable=True),
                    sa.Column('restated', sa.DateTime(), nullable=True),

                    sa.Column('book_value', sa.String(length=50), nullable=True),
                    sa.Column('cashflow', sa.String(length=50), nullable=True),
                    sa.Column('earnings', sa.String(length=50), nullable=True),
                    sa.Column('dividends', sa.String(length=50), nullable=True),
                    sa.Column('payout_ratio', sa.String(length=50), nullable=True),
                    sa.Column('price_low', sa.String(length=50), nullable=True),
                    sa.Column('price_high', sa.String(length=50), nullable=True),

                    sa.Column('company_id', sa.Integer(), nullable=True),

                    sa.Column('lock_version', sa.SmallInteger, nullable=False))


def downgrade() -> None:
    op.drop_table('per_share')
    op.drop_table('xxx_per_share')
