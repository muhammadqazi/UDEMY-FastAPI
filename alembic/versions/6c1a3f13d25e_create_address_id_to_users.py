"""create address_id to users

Revision ID: 6c1a3f13d25e
Revises: 842d28748c36
Create Date: 2022-06-22 17:22:03.745534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c1a3f13d25e'
down_revision = '842d28748c36'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column(
        'address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk',
                          source_table="users", referent_table="address" , local_cols=["address_id"] , remote_cols=["id"] , ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('address_users_fk' , table_name="users")
    op.drop_column('users' , 'address_id')
