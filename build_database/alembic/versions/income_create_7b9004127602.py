"""income create

Revision ID: 7b9004127602
Revises: 398567e4171e
Create Date: 2022-10-24 16:31:34.848545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b9004127602'
down_revision = '398567e4171e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('income',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('year', sa.Integer(), nullable=True, server_default='0'),
                    sa.Column('fiscal_year', sa.DateTime(), nullable=False),
                    sa.Column('restated', sa.DateTime(), nullable=False),

                    sa.Column('revenue', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('gross_profit', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('depreciation', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('interest_expense', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('pretax_income', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('tax', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('net_income', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('net_income_core', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('bnk_provision_for_loan_losses', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('bnk_operating_income', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('ins_total_claims', sa.String(length=50), nullable=True, server_default='NaN'),
                    sa.Column('ins_operating_income', sa.String(length=50), nullable=True, server_default='NaN'),

                    sa.Column('company_id', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('lock_version', sa.SmallInteger, server_default='1', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now()))

    op.create_table('xxx_income',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('logged_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('audit_action', sa.CHAR(length=1), server_default='I', nullable=False),
                    sa.Column('record_id', sa.Integer(), server_default='0', nullable=False),

                    sa.Column('year', sa.Integer(), nullable=True),
                    sa.Column('fiscal_year', sa.DateTime(), nullable=True),
                    sa.Column('restated', sa.DateTime(), nullable=True),

                    sa.Column('revenue', sa.String(length=50), nullable=True),
                    sa.Column('gross_profit', sa.String(length=50), nullable=True),
                    sa.Column('depreciation', sa.String(length=50), nullable=True),
                    sa.Column('interest_expense', sa.String(length=50), nullable=True),
                    sa.Column('pretax_income', sa.String(length=50), nullable=True),
                    sa.Column('tax', sa.String(length=50), nullable=True),
                    sa.Column('net_income', sa.String(length=50), nullable=True),
                    sa.Column('net_income_core', sa.String(length=50), nullable=True),
                    sa.Column('bnk_provision_for_loan_losses', sa.String(length=50), nullable=True),
                    sa.Column('bnk_operating_income', sa.String(length=50), nullable=True),
                    sa.Column('ins_total_claims', sa.String(length=50), nullable=True),
                    sa.Column('ins_operating_income', sa.String(length=50), nullable=True),

                    sa.Column('company_id', sa.Integer(), nullable=True),
                    sa.Column('lock_version', sa.SmallInteger, nullable=False))


def downgrade() -> None:
    op.drop_table('income')
    op.drop_table('xxx_income')
