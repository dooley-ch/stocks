"""quarter create

Revision ID: b0d25c4b3279
Revises: dce2401104be
Create Date: 2022-10-24 18:03:44.526942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0d25c4b3279'
down_revision = 'dce2401104be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('quarter',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('year', sa.Integer(), nullable=True, server_default='0'),
                    sa.Column('quarter', sa.String(length=2), nullable=True, server_default='Q0'),
                    sa.Column('fiscal_year', sa.DateTime(), nullable=False),
                    sa.Column('restated', sa.DateTime(), nullable=False),
                    sa.Column('shares_basic', sa.String(length=50), nullable=False),
                    sa.Column('shares_diluted', sa.String(length=50), nullable=False),

                    # Income
                    sa.Column('revenue', sa.String(length=50), nullable=True),
                    sa.Column('pretax_income', sa.String(length=50), nullable=True),
                    sa.Column('tax', sa.String(length=50), nullable=True),
                    sa.Column('net_income', sa.String(length=50), nullable=True),
                    sa.Column('net_income_core', sa.String(length=50), nullable=True),

                    # Cashflow
                    sa.Column('dividends_paid', sa.String(length=50), nullable=True),
                    sa.Column('net_change_in_cash', sa.String(length=50), nullable=True),

                    sa.Column('company_id', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('lock_version', sa.SmallInteger, server_default='1', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now()))

    op.create_table('xxx_quarter',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('logged_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('audit_action', sa.CHAR(length=1), server_default='I', nullable=False),
                    sa.Column('record_id', sa.Integer(), server_default='0', nullable=False),

                    sa.Column('year', sa.Integer(), nullable=True),
                    sa.Column('quarter', sa.String(length=2), nullable=True),
                    sa.Column('fiscal_year', sa.DateTime(), nullable=True),
                    sa.Column('restated', sa.DateTime(), nullable=True),
                    sa.Column('shares_basic', sa.String(length=50), nullable=True),
                    sa.Column('shares_diluted', sa.String(length=50), nullable=True),

                    sa.Column('revenue', sa.String(length=50), nullable=True),
                    sa.Column('pretax_income', sa.String(length=50), nullable=True),
                    sa.Column('tax', sa.String(length=50), nullable=True),
                    sa.Column('net_income', sa.String(length=50), nullable=True),
                    sa.Column('net_income_core', sa.String(length=50), nullable=True),

                    sa.Column('dividends_paid', sa.String(length=50), nullable=True),
                    sa.Column('net_change_in_cash', sa.String(length=50), nullable=True),

                    sa.Column('company_id', sa.Integer(), nullable=True),
                    sa.Column('lock_version', sa.SmallInteger, nullable=True))


def downgrade() -> None:
    op.drop_table('quarter')
    op.drop_table('xxx_quarter')
