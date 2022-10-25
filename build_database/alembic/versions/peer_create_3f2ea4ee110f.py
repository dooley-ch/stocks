"""peer create

Revision ID: 3f2ea4ee110f
Revises: d50149e612f6
Create Date: 2022-10-24 16:34:13.085460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f2ea4ee110f'
down_revision = 'd50149e612f6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('peer',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('peer', sa.String(length=12), nullable=False),
                    sa.Column('company_id', sa.Integer(), nullable=False),
                    sa.Column('lock_version', sa.SmallInteger, server_default='1', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now()))

    op.create_table('xxx_peer',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('logged_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('audit_action', sa.CHAR(length=1), server_default='I', nullable=False),
                    sa.Column('record_id', sa.Integer(), server_default='0', nullable=False),

                    sa.Column('company_id', sa.Integer(), nullable=True),
                    sa.Column('peer', sa.String(length=12), nullable=True),

                    sa.Column('lock_version', sa.SmallInteger, nullable=False))


def downgrade() -> None:
    op.drop_table('peer')
    op.drop_table('xxx_peer')
