"""add last few columns to posts table

Revision ID: 0ca9f2b87a6c
Revises: e405bad8b6ed
Create Date: 2022-02-23 13:49:34.159749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ca9f2b87a6c'
down_revision = 'e405bad8b6ed'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),
    )
    op.add_column("posts", sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'))
    )


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
