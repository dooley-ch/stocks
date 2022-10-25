"""zs_peer create

Revision ID: 67c1aa039355
Revises: a251a76ea552
Create Date: 2022-10-24 17:44:22.361115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67c1aa039355'
down_revision = 'a251a76ea552'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('zs_peer',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('ticker', sa.String(length=12), nullable=False),
                    sa.Column('peer', sa.String(length=12), nullable=False))

    op.create_unique_constraint("zs_peer_ukey_ticker_peer", "zs_peer", ["ticker", "peer"])


def downgrade() -> None:
    op.execute("ALTER TABLE zs_peer DROP INDEX zs_peer_ukey_ticker_peer;")
    op.drop_table('zs_peer')
