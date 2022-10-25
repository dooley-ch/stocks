"""zs_sector create

Revision ID: a995d20f8645
Revises: 97d83133cb16
Create Date: 2022-10-24 17:57:49.572956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a995d20f8645'
down_revision = '97d83133cb16'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('zs_sector',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('name', sa.String(length=250), nullable=False),
                    sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False))


def downgrade() -> None:
    op.drop_table('zs_sector')
