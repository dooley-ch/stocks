"""z_simfin_companies create

Revision ID: e485bbd22c3e
Revises: 73632a111a90
Create Date: 2022-10-24 17:23:51.898881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e485bbd22c3e'
down_revision = '73632a111a90'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_simfin_companies',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('company', sa.String(length=250), nullable=False),
                    sa.Column('simfin_id', sa.Integer(), nullable=False),
                    sa.Column('industry_id', sa.Integer(), nullable=False))

    op.create_index("z_simfin_companies_ticker", "z_simfin_companies", ["ticker"])


def downgrade() -> None:
    op.drop_index("z_simfin_companies_ticker", "z_simfin_companies")
    op.drop_table("z_simfin_companies")
