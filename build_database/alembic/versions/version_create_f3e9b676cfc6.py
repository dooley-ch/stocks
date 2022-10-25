"""version create

Revision ID: f3e9b676cfc6
Revises: 
Create Date: 2022-10-24 16:22:02.184161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3e9b676cfc6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('version',
                    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column('major', sa.SmallInteger, nullable=False),
                    sa.Column('minor', sa.SmallInteger, nullable=False),
                    sa.Column('build', sa.SmallInteger, nullable=False),
                    sa.Column('lock_version', sa.SmallInteger, server_default='1', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now()))

    op.execute("INSERT INTO version(major, minor, build)  VALUES (1, 0, 1)")


def downgrade() -> None:
    op.drop_table('version')
