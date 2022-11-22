"""quote_product

Revision ID: beacf07d6bcb
Revises: ced169b59f8e
Create Date: 2020-12-26 19:59:10.393790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beacf07d6bcb'
down_revision = 'ced169b59f8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quote_product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('product_name', sa.String(length=256), nullable=False),
    sa.Column('manufacturer', sa.String(length=256), nullable=False),
    sa.Column('observation', sa.Text(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('quote_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quote_id'], ['quote.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quote_product')
    # ### end Alembic commands ###
