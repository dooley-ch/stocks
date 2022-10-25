"""z_peer_map create

Revision ID: e52b25ca5bdb
Revises: 67c1aa039355
Create Date: 2022-10-24 17:45:56.887194

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e52b25ca5bdb'
down_revision = '67c1aa039355'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('z_peer_map',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=30), nullable=False),
                    sa.Column('peer', sa.String(length=30), nullable=True))

    op.create_index('z_peer_map_ticker', 'z_peer_map', ['ticker'])


def downgrade() -> None:
    op.drop_index('z_peer_map_ticker', 'z_peer_map')
    op.drop_table('z_peer_map')
