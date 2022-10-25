"""z_income_insurance_annual create

Revision ID: e4c18e4e5570
Revises: fb16c9380db6
Create Date: 2022-10-24 17:10:19.675991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4c18e4e5570'
down_revision = 'fb16c9380db6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_income_insurance_annual',
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
    op.create_index('z_income_insurance_annual_ticker', 'z_income_insurance_annual', ['ticker'])
    op.create_index('z_income_insurance_annual_simfin_id', 'z_income_insurance_annual', ['simfin_id'])


def downgrade() -> None:
    op.drop_index('z_income_insurance_annual_ticker', 'z_income_insurance_annual')
    op.drop_index('z_income_insurance_annual_simfin_id', 'z_income_insurance_annual')
    op.drop_table('z_income_insurance_annual')
