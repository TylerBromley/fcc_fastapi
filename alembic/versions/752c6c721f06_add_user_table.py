"""add user table

Revision ID: 752c6c721f06
Revises: a9fe53059bad
Create Date: 2022-02-23 13:30:37.998543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '752c6c721f06'
down_revision = 'a9fe53059bad'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
        server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('users')
