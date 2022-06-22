"""create address table

Revision ID: 842d28748c36
Revises: e5f97ac9f64a
Create Date: 2022-06-22 17:13:09.333656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '842d28748c36'
down_revision = 'e5f97ac9f64a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postalcode', sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('address')
