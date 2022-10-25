"""z_income_bank_annual create

Revision ID: f8bd2db61544
Revises: 64c497f2e52f
Create Date: 2022-10-24 16:42:56.273919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8bd2db61544'
down_revision = '64c497f2e52f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_income_bank_annual',
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

                    sa.Column('revenue', sa.String(length=50), nullable=True),
                    sa.Column('provision_for_loan_losses', sa.String(length=50), nullable=True),
                    sa.Column('net_Revenue_after_provisions', sa.String(length=50), nullable=True),
                    sa.Column('total_non_interest_expense', sa.String(length=50), nullable=True),
                    sa.Column('operating_income_loss', sa.String(length=50), nullable=True),
                    sa.Column('non_operating_income_loss', sa.String(length=50), nullable=True),
                    sa.Column('pretax_income_loss', sa.String(length=50), nullable=True),
                    sa.Column('income_tax_expense_benefit_net', sa.String(length=50), nullable=True),
                    sa.Column('income_loss_from_continuing_operations', sa.String(length=50), nullable=True),
                    sa.Column('net_extraordinary_gains_losses', sa.String(length=50), nullable=True),
                    sa.Column('net_income', sa.String(length=50), nullable=True),
                    sa.Column('net_income_Common', sa.String(length=50), nullable=True))
    op.create_index('z_income_bank_annual_ticker', 'z_income_bank_annual', ['ticker'])
    op.create_index('z_income_bank_annual_simfin_id', 'z_income_bank_annual', ['simfin_id'])



def downgrade() -> None:
    op.drop_index('z_income_bank_annual_ticker', 'z_income_bank_annual')
    op.drop_index('z_income_bank_annual_simfin_id', 'z_income_bank_annual')
    op.drop_table('z_income_bank_annual')
