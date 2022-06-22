"""create phone number for user col

Revision ID: e5f97ac9f64a
Revises: 
Create Date: 2022-06-22 16:57:14.563749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5f97ac9f64a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))


def downgrade() -> None:
    op.drop_column('users','phone_number')
