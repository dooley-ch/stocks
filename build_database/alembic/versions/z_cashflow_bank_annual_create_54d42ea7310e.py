"""z_cashflow_bank_annual create

Revision ID: 54d42ea7310e
Revises: f8bd2db61544
Create Date: 2022-10-24 16:45:31.050001

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '54d42ea7310e'
down_revision = 'f8bd2db61544'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_cashflow_bank_annual',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('simfin_id', sa.Integer(), nullable=False),

                    sa.Column('currency', sa.String(length=50), nullable=True),
                    sa.Column('fiscal_year', sa.String(length=50), nullable=True),
                    sa.Column('fiscal_period', sa.String(length=50), nullable=True),
                    sa.Column('report_date', sa.String(length=50), nullable=True),
                    sa.Column('publish_date', sa.String(length=50), nullable=True),
                    sa.Column('restated_date', sa.String(length=50), nullable=True),
                    sa.Column('shares_basic', sa.String(length=50), nullable=True),
                    sa.Column('shares_diluted', sa.String(length=50), nullable=True),

                    sa.Column('net_income_starting_line', sa.String(length=50), nullable=True),
                    sa.Column('depreciation_amortization', sa.String(length=50), nullable=True),
                    sa.Column('provision_for_loan_losses', sa.String(length=50), nullable=True),
                    sa.Column('non_cash_items', sa.String(length=50), nullable=True),
                    sa.Column('change_in_working_capital', sa.String(length=50), nullable=True),
                    sa.Column('net_cash_from_operating_activities', sa.String(length=50), nullable=True),
                    sa.Column('change_in_fixed_assets_intangibles', sa.String(length=50), nullable=True),
                    sa.Column('net_change_in_loans_interbank', sa.String(length=50), nullable=True),
                    sa.Column('net_cash_from_acquisitions_divestitures', sa.String(length=50), nullable=True),
                    sa.Column('net_cash_from_investing_activities', sa.String(length=50), nullable=True),
                    sa.Column('dividends_paid', sa.String(length=50), nullable=True),
                    sa.Column('cash_from_repayment_of_debt', sa.String(length=50), nullable=True),
                    sa.Column('cash_from_repurchase_of_equity', sa.String(length=50), nullable=True),
                    sa.Column('net_cash_from_financing_activities', sa.String(length=50), nullable=True),
                    sa.Column('effect_of_foreign_exchange_rates', sa.String(length=50), nullable=True),
                    sa.Column('net_change_in_cash', sa.String(length=50), nullable=True))
    op.create_index('z_cashflow_bank_annual_ticker', 'z_cashflow_bank_annual', ['ticker'])
    op.create_index('z_cashflow_bank_annual_simfin_id', 'z_cashflow_bank_annual', ['simfin_id'])


def downgrade() -> None:
    op.drop_index('z_cashflow_bank_annual_ticker', 'z_cashflow_bank_annual')
    op.drop_index('z_cashflow_bank_annual_simfin_id', 'z_cashflow_bank_annual')
    op.drop_table('z_cashflow_bank_annual')
