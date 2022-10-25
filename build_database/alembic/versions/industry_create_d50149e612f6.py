"""industry create

Revision ID: d50149e612f6
Revises: 7b9004127602
Create Date: 2022-10-24 16:32:57.404628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd50149e612f6'
down_revision = '7b9004127602'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('industry',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('name', sa.String(length=250), nullable=False),
                    sa.Column('sector_id', sa.Integer(), server_default='0', nullable=False),
                    sa.Column('is_active', sa.Boolean(), server_default='0', nullable=False),
                    sa.Column('lock_version', sa.SmallInteger, server_default='1', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.func.now()))

    op.create_table('xxx_industry',
                    sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
                    sa.Column('logged_at', sa.TIMESTAMP, server_default=sa.func.now()),
                    sa.Column('audit_action', sa.CHAR(length=1), server_default='I', nullable=False),
                    sa.Column('record_id', sa.Integer(), server_default='0', nullable=False),

                    sa.Column('name', sa.String(length=250), nullable=True),
                    sa.Column('sector_id', sa.Integer(), nullable=True),
                    sa.Column('is_active', sa.Boolean(), nullable=True),

                    sa.Column('lock_version', sa.SmallInteger, nullable=False))


def downgrade() -> None:
    op.drop_table('industry')
    op.drop_table('xxx_industry')

