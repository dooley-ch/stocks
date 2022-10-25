"""quarter constraints

Revision ID: 41c08fa38bce
Revises: e61eec6ec525
Create Date: 2022-10-24 19:31:18.885387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41c08fa38bce'
down_revision = 'e61eec6ec525'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_check_constraint('xxx_quarter_audit_action_check', "xxx_quarter", "audit_action in ('I','U','D')")
    op.create_foreign_key("quarter_company_id_fkey", "quarter", "company", ["company_id"], ["id"])


def downgrade() -> None:
    op.execute("ALTER TABLE xxx_quarter DROP CHECK xxx_quarter_audit_action_check;")
    op.execute("ALTER TABLE quarter DROP FOREIGN KEY quarter_company_id_fkey;")
