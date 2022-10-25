"""z_balance_sheet_general_annual create

Revision ID: 7f82bfdf36dc
Revises: f41fc5a6f343
Create Date: 2022-10-24 17:02:12.431296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f82bfdf36dc'
down_revision = 'f41fc5a6f343'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_balance_sheet_general_annual',
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

                    sa.Column('cash_cash_equivalents_short_term_investments', sa.String(length=50), nullable=True),
                    sa.Column('accounts_notes_receivable', sa.String(length=50), nullable=True),
                    sa.Column('inventories', sa.String(length=50), nullable=True),
                    sa.Column('total_current_assets', sa.String(length=50), nullable=True),
                    sa.Column('property_plant_equipment_net', sa.String(length=50), nullable=True),
                    sa.Column('long_term_investments_receivables', sa.String(length=50), nullable=True),
                    sa.Column('other_long_term_assets', sa.String(length=50), nullable=True),
                    sa.Column('total_noncurrent_assets', sa.String(length=50), nullable=True),
                    sa.Column('total_assets', sa.String(length=50), nullable=True),
                    sa.Column('payables_accruals', sa.String(length=50), nullable=True),
                    sa.Column('short_term_debt', sa.String(length=50), nullable=True),
                    sa.Column('total_current_liabilities', sa.String(length=50), nullable=True),
                    sa.Column('long_term_debt', sa.String(length=50), nullable=True),
                    sa.Column('total_noncurrent_liabilities', sa.String(length=50), nullable=True),
                    sa.Column('total_liabilities', sa.String(length=50), nullable=True),
                    sa.Column('share_capital_additional_paid_in_capital', sa.String(length=50), nullable=True),
                    sa.Column('treasury_stock', sa.String(length=50), nullable=True),
                    sa.Column('retained_earnings', sa.String(length=50), nullable=True),
                    sa.Column('total_equity', sa.String(length=50), nullable=True),
                    sa.Column('total_liabilities_equity', sa.String(length=50), nullable=True))
    op.create_index('z_balance_sheet_general_annual_ticker', 'z_balance_sheet_general_annual', ['ticker'])
    op.create_index('z_balance_sheet_general_annual_simfin_id', 'z_balance_sheet_general_annual', ['simfin_id'])


def downgrade() -> None:
    op.drop_index('z_balance_sheet_general_annual_ticker', 'z_balance_sheet_general_annual')
    op.drop_index('z_balance_sheet_general_annual_simfin_id', 'z_balance_sheet_general_annual')
    op.drop_table('z_balance_sheet_general_annual')
