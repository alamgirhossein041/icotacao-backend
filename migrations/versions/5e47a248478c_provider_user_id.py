"""provider_user_id

Revision ID: 5e47a248478c
Revises: a792fe004dcb
Create Date: 2021-01-07 14:39:09.368620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e47a248478c'
down_revision = 'a792fe004dcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('supplier', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'supplier', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'supplier', type_='foreignkey')
    op.drop_column('supplier', 'user_id')
    # ### end Alembic commands ###
