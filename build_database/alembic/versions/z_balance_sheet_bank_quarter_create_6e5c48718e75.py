"""z_balance_sheet_bank_quarter create

Revision ID: 6e5c48718e75
Revises: 0f7af8326d3e
Create Date: 2022-10-24 16:54:40.662760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e5c48718e75'
down_revision = '0f7af8326d3e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_balance_sheet_bank_quarter',
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
                    sa.Column('interbank_Assets', sa.String(length=50), nullable=True),
                    sa.Column('short_long_term_investments', sa.String(length=50), nullable=True),
                    sa.Column('accounts_notes_receivable', sa.String(length=50), nullable=True),
                    sa.Column('net_loans', sa.String(length=50), nullable=True),
                    sa.Column('net_fixed_assets', sa.String(length=50), nullable=True),
                    sa.Column('total_assets', sa.String(length=50), nullable=True),
                    sa.Column('total_deposits', sa.String(length=50), nullable=True),
                    sa.Column('short_term_debt', sa.String(length=50), nullable=True),
                    sa.Column('long_term_debt', sa.String(length=50), nullable=True),
                    sa.Column('total_liabilities', sa.String(length=50), nullable=True),
                    sa.Column('preferred_equity', sa.String(length=50), nullable=True),
                    sa.Column('share_capital_additional_paid_in_capital', sa.String(length=50), nullable=True),
                    sa.Column('treasury_stock', sa.String(length=50), nullable=True),
                    sa.Column('retained_earnings', sa.String(length=50), nullable=True),
                    sa.Column('total_equity', sa.String(length=50), nullable=True),
                    sa.Column('total_liabilities_equity', sa.String(length=50), nullable=True)
                    )
    op.create_index('z_balance_sheet_bank_quarter_ticker', 'z_balance_sheet_bank_quarter', ['ticker'])
    op.create_index('z_balance_sheet_bank_quarter_simfin_id', 'z_balance_sheet_bank_quarter', ['simfin_id'])


def downgrade() -> None:
    op.drop_index('z_balance_sheet_bank_quarter_ticker', 'z_balance_sheet_bank_quarter')
    op.drop_index('z_balance_sheet_bank_quarter_simfin_id', 'z_balance_sheet_bank_quarter')
    op.drop_table('z_balance_sheet_bank_quarter')
