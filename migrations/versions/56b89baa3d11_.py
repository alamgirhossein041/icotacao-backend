"""empty message

Revision ID: 56b89baa3d11
Revises: 5e19e4dc3dd7
Create Date: 2021-01-28 16:27:26.080626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56b89baa3d11'
down_revision = '5e19e4dc3dd7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('costumer_address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('code_post', sa.String(length=256), nullable=True),
    sa.Column('street', sa.String(length=256), nullable=True),
    sa.Column('number', sa.String(length=256), nullable=True),
    sa.Column('district', sa.String(length=256), nullable=True),
    sa.Column('complement', sa.String(length=256), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('costumer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['costumer_id'], ['costumer.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('costumer_address')
    # ### end Alembic commands ###
