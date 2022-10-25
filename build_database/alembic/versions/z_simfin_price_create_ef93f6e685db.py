"""z_simfin_price create

Revision ID: ef93f6e685db
Revises: 83e736d8d0af
Create Date: 2022-10-24 17:27:15.064302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef93f6e685db'
down_revision = '83e736d8d0af'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_simfin_price',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('simfin_id', sa.Integer(), nullable=False),
                    sa.Column('price_date', sa.String(length=50), nullable=True),
                    sa.Column('open_price', sa.String(length=50), nullable=True),
                    sa.Column('low_price', sa.String(length=50), nullable=True),
                    sa.Column('high_price', sa.String(length=50), nullable=True),
                    sa.Column('close_price', sa.String(length=50), nullable=True),
                    sa.Column('adjusted_close_price', sa.String(length=50), nullable=True),
                    sa.Column('dividend', sa.String(length=50), nullable=True),
                    sa.Column('volume', sa.String(length=50), nullable=True),
                    sa.Column('shares_outstanding', sa.String(length=50), nullable=True))

    op.create_index("z_simfin_price_ticker", "z_simfin_price", ["ticker"])
    op.create_index("z_simfin_price_simfin_id", "z_simfin_price", ["simfin_id"])


def downgrade() -> None:
    op.drop_index("z_simfin_price_ticker", "z_simfin_price")
    op.drop_index("z_simfin_price_simfin_id", "z_simfin_price")
    op.drop_table("z_simfin_price")
