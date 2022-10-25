"""company create

Revision ID: d4f61c6b4dfb
Revises: 00e44bbb8f0e
Create Date: 2022-10-24 16:27:29.186662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4f61c6b4dfb'
down_revision = '00e44bbb8f0e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('company',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('name', sa.String(length=250), nullable=False),
                    sa.Column('currency', sa.String(length=3), nullable=False, server_default='USD'),
                    sa.Column('description', sa.TEXT()),
                    sa.Column('stock_exchange', sa.String(length=50), server_default='Unknown'),
                    sa.Column('cik_number', sa.CHAR(length=10), server_default='0000000000', nullable=False),
                    sa.Column('figi_code', sa.CHAR(length=12), server_default='000000000000', nullable=False),
                    sa.Column('simfin_number', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('is_sp100', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('is_sp600', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('is_sp400', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('is_sp500', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('company_type_id', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('industry_id', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False),
                    sa.Column('has_financials', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('lock_version', sa.SmallInteger, server_default='1', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now()))

    op.create_table('xxx_company',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('logged_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('audit_action', sa.CHAR(length=1), server_default='I', nullable=False),
                    sa.Column('record_id', sa.Integer(), server_default='0', nullable=False),

                    sa.Column('ticker', sa.String(length=12), nullable=True),
                    sa.Column('name', sa.String(length=250), nullable=True),
                    sa.Column('currency', sa.String(length=3), nullable=True),
                    sa.Column('description', sa.TEXT(), nullable=True),
                    sa.Column('stock_exchange', sa.String(length=50), nullable=True),
                    sa.Column('cik_number', sa.CHAR(length=10), nullable=True),
                    sa.Column('figi_code', sa.CHAR(length=12), nullable=True),
                    sa.Column('simfin_number', sa.Integer(), nullable=True),
                    sa.Column('is_sp100', sa.Boolean(), nullable=True),
                    sa.Column('is_sp600', sa.Boolean(), nullable=True),
                    sa.Column('is_sp400', sa.Boolean(), nullable=True),
                    sa.Column('is_sp500', sa.Boolean(), nullable=True),
                    sa.Column('company_type_id', sa.Integer(), nullable=True),
                    sa.Column('industry_id', sa.Integer(), nullable=True),
                    sa.Column('is_active', sa.Boolean(), nullable=True),
                    sa.Column('has_financials', sa.Boolean(), nullable=True),

                    sa.Column('lock_version', sa.SmallInteger, nullable=False),
                    )


def downgrade() -> None:
    op.drop_table('company')
    op.drop_table('xxx_company')
