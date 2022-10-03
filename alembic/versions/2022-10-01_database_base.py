"""database base

Revision ID: 0a5f57588ddb
Revises: 
Create Date: 2022-10-01 21:17:55.768147

"""
from enum import unique
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a5f57588ddb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False)
    ),
    op.create_table('products',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('currency', sa.String(), nullable=False),
    ),
    op.create_table('sales',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('state', sa.String(), nullable=False),
        sa.Column('value', sa.Float(), nullable=False),
        sa.Column('fee', sa.Float(), nullable=False),
        sa.Column('currency', sa.String(), nullable=False),
        sa.Column('client', sa.String(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table('users')
    op.drop_table('products')
    op.drop_table('sales')
    # ### end Alembic commands ###
