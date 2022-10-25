"""z_income_insurance_quarter create

Revision ID: d891f70e9811
Revises: 7c62cdcb73fb
Create Date: 2022-10-24 17:16:42.722366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd891f70e9811'
down_revision = '7c62cdcb73fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_income_insurance_quarter',
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
                    sa.Column('total_claims_losses', sa.String(length=50), nullable=True),
                    sa.Column('operating_income_loss', sa.String(length=50), nullable=True),
                    sa.Column('pretax_income_loss', sa.String(length=50), nullable=True),
                    sa.Column('income_tax_expense_benefit_net', sa.String(length=50), nullable=True),
                    sa.Column('income_loss_from_affiliates_net_of_taxes', sa.String(length=50), nullable=True),
                    sa.Column('income_loss_from_continuing_operations', sa.String(length=50), nullable=True),
                    sa.Column('net_extraordinary_gains_losses', sa.String(length=50), nullable=True),
                    sa.Column('net_income', sa.String(length=50), nullable=True),
                    sa.Column('net_income_common', sa.String(length=50), nullable=True))
    op.create_index('z_income_insurance_quarter_ticker', 'z_income_insurance_quarter', ['ticker'])
    op.create_index('z_income_insurance_quarter_simfin_id', 'z_income_insurance_quarter', ['simfin_id'])


def downgrade() -> None:
    op.drop_index('z_income_insurance_quarter_ticker', 'z_income_insurance_quarter')
    op.drop_index('z_income_insurance_quarter_simfin_id', 'z_income_insurance_quarter')
    op.drop_table('z_income_insurance_quarter')
