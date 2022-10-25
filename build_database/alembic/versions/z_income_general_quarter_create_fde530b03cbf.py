"""z_income_general_quarter create

Revision ID: fde530b03cbf
Revises: 7f82bfdf36dc
Create Date: 2022-10-24 17:04:12.770263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fde530b03cbf'
down_revision = '7f82bfdf36dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_income_general_quarter',
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
                    sa.Column('cost_of_revenue', sa.String(length=50), nullable=True),
                    sa.Column('gross_profit', sa.String(length=50), nullable=True),
                    sa.Column('operating_expenses', sa.String(length=50), nullable=True),
                    sa.Column('selling_general_administrative', sa.String(length=50), nullable=True),
                    sa.Column('research_development', sa.String(length=50), nullable=True),
                    sa.Column('depreciation_amortization', sa.String(length=50), nullable=True),
                    sa.Column('operating_income', sa.String(length=50), nullable=True),
                    sa.Column('non_operating_income', sa.String(length=50), nullable=True),
                    sa.Column('interest_expense_net', sa.String(length=50), nullable=True),
                    sa.Column('pretax_income_loss_adj', sa.String(length=50), nullable=True),
                    sa.Column('abnormal_gains_lLosses', sa.String(length=50), nullable=True),
                    sa.Column('pretax_income_loss', sa.String(length=50), nullable=True),
                    sa.Column('income_tax_expense_benefit_net', sa.String(length=50), nullable=True),
                    sa.Column('income_loss_from_continuing_operations', sa.String(length=50), nullable=True),
                    sa.Column('net_extraordinary_gains_losses', sa.String(length=50), nullable=True),
                    sa.Column('net_income', sa.String(length=50), nullable=True),
                    sa.Column('net_income_common', sa.String(length=50), nullable=True)
                    )
    op.create_index('z_income_general_quarter_ticker', 'z_income_general_quarter', ['ticker'])
    op.create_index('z_income_general_quarter_simfin_id', 'z_income_general_quarter', ['simfin_id'])


def downgrade() -> None:
    op.drop_index('z_income_general_quarter_ticker', 'z_income_general_quarter')
    op.drop_index('z_income_general_quarter_simfin_id', 'z_income_general_quarter')
    op.drop_table('z_income_general_quarter')
