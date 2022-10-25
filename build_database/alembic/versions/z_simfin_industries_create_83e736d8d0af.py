"""z_simfin_industries create

Revision ID: 83e736d8d0af
Revises: e485bbd22c3e
Create Date: 2022-10-24 17:25:14.381412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83e736d8d0af'
down_revision = 'e485bbd22c3e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_simfin_industries',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('industry_id', sa.Integer(), nullable=False),
                    sa.Column('sector', sa.String(length=250), nullable=False),
                    sa.Column('industry', sa.String(length=250), nullable=False))


def downgrade() -> None:
    op.drop_table("z_simfin_industries")
