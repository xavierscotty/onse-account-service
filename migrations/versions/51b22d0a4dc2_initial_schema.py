"""Initial schema

Revision ID: 51b22d0a4dc2
Revises:
Create Date: 2019-01-10 15:51:35.504545

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '51b22d0a4dc2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'accounts',
        sa.Column('account_number', sa.Integer, primary_key=True,
                  autoincrement=True),
        sa.Column('account_status', sa.String(100)),
        sa.Column('customer_id', sa.String(50))
    )


def downgrade():
    op.drop_table('transactions')
