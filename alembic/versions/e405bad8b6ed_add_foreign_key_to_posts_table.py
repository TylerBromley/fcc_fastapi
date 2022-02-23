"""add foreign key to posts table

Revision ID: e405bad8b6ed
Revises: 752c6c721f06
Create Date: 2022-02-23 13:41:39.609543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e405bad8b6ed'
down_revision = '752c6c721f06'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", 
                          source_table="posts", 
                          referent_table="users", 
                          local_cols=['owner_id'], 
                          remote_cols=['id'], 
                          ondelete="CASCADE"
                          )


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
