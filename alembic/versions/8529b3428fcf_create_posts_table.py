"""create posts table

Revision ID: 8529b3428fcf
Revises: 
Create Date: 2022-02-23 13:16:21.715902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8529b3428fcf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
