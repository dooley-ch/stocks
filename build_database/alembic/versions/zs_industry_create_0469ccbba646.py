"""zs_industry create

Revision ID: 0469ccbba646
Revises: a995d20f8645
Create Date: 2022-10-24 17:58:56.706304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0469ccbba646'
down_revision = 'a995d20f8645'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('zs_industry',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('name', sa.String(length=250), nullable=False),
                    sa.Column('sector_id', sa.Integer(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False))


def downgrade() -> None:
    op.drop_table('zs_industry')
