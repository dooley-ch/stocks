"""balance_sheet create

Revision ID: 00e44bbb8f0e
Revises: f3e9b676cfc6
Create Date: 2022-10-24 16:24:52.849333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00e44bbb8f0e'
down_revision = 'f3e9b676cfc6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('balance_sheet',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('year', sa.Integer(), nullable=True, server_default='0'),
                    sa.Column('fiscal_year', sa.DateTime(), nullable=False),
                    sa.Column('restated', sa.DateTime(), nullable=False),
                    sa.Column('shares_basic', sa.String(length=50), nullable=False),
                    sa.Column('shares_diluted', sa.String(length=50), nullable=False),

                    sa.Column('cash', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('accounts_receivable', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('inventories', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('current_assets', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('total_assets', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('accounts_payable', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('current_liabilities', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('long_term_debt', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('share_capital', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('total_capital', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('capital_expenditure', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('cashflow', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('bnk_inter_bank_assets', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('bnk_net_loans', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('bnk_total_deposits', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('ins_total_investments', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('ins_insurance_reserves', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('ins_policyholders_equity', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('company_id', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('lock_version', sa.SmallInteger, server_default='1', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now()))

    op.create_table('xxx_balance_sheet',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('logged_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('audit_action', sa.CHAR(length=1), server_default='I', nullable=False),
                    sa.Column('record_id', sa.Integer(), server_default='0', nullable=False),

                    sa.Column('year', sa.Integer(), nullable=True),
                    sa.Column('fiscal_year', sa.DateTime(), nullable=True),
                    sa.Column('restated', sa.DateTime(), nullable=True),
                    sa.Column('shares_basic', sa.String(length=50), nullable=True),
                    sa.Column('shares_diluted', sa.String(length=50), nullable=True),

                    sa.Column('cash', sa.String(length=50), nullable=True),
                    sa.Column('accounts_receivable', sa.String(length=50), nullable=True),
                    sa.Column('inventories', sa.String(length=50), nullable=True),
                    sa.Column('current_assets', sa.String(length=50), nullable=True),
                    sa.Column('total_assets', sa.String(length=50), nullable=True),
                    sa.Column('accounts_payable', sa.String(length=50), nullable=True),
                    sa.Column('current_liabilities', sa.String(length=50), nullable=True),
                    sa.Column('long_term_debt', sa.String(length=50), nullable=True),
                    sa.Column('share_capital', sa.String(length=50), nullable=True),
                    sa.Column('total_capital', sa.String(length=50), nullable=True),
                    sa.Column('capital_expenditure', sa.String(length=50), nullable=True),
                    sa.Column('cashflow', sa.String(length=50), nullable=True),
                    sa.Column('bnk_inter_bank_assets', sa.String(length=50), nullable=True),
                    sa.Column('bnk_net_loans', sa.String(length=50), nullable=True),
                    sa.Column('bnk_total_deposits', sa.String(length=50), nullable=True),
                    sa.Column('ins_total_investments', sa.String(length=50), nullable=True),
                    sa.Column('ins_insurance_reserves', sa.String(length=50), nullable=True),
                    sa.Column('ins_policyholders_equity', sa.String(length=50), nullable=True),

                    sa.Column('company_id', sa.Integer(), nullable=True),

                    sa.Column('lock_version', sa.SmallInteger, nullable=False))


def downgrade() -> None:
    op.drop_table('balance_sheet')
    op.drop_table('xxx_balance_sheet')
