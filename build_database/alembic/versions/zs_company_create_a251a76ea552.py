"""zs_company create

Revision ID: a251a76ea552
Revises: 67eb8b08c24b
Create Date: 2022-10-24 17:41:49.168963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a251a76ea552'
down_revision = '67eb8b08c24b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('zs_company',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('name', sa.String(length=250), nullable=False),
                    sa.Column('currency', sa.String(length=3), nullable=False, server_default='USD'),
                    sa.Column('description', sa.TEXT()),
                    sa.Column('stock_exchange', sa.String(length=50)),
                    sa.Column('cik_number', sa.CHAR(length=10), server_default='0000000000', nullable=False),
                    sa.Column('figi_code', sa.CHAR(length=12), server_default='000000000000', nullable=False),
                    sa.Column('simfin_number', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('is_sp100', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('is_sp600', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('is_sp400', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('is_sp500', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('company_type_id', sa.Integer(), server_default='4', nullable=False),
                    sa.Column('industry_id', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('is_active', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('has_financials', sa.Boolean(), server_default='0', nullable=False))

    op.create_unique_constraint("zs_company_ukey_ticker", "zs_company", ["ticker"])


def downgrade() -> None:
    op.execute("ALTER TABLE zs_company DROP INDEX zs_company_ukey_ticker;")
    op.drop_table('zs_company')
