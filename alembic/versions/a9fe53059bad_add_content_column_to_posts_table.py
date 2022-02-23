"""add content column to posts table

Revision ID: a9fe53059bad
Revises: 8529b3428fcf
Create Date: 2022-02-23 13:26:02.590355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9fe53059bad'
down_revision = '8529b3428fcf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
