"""empty message

Revision ID: 78b997ba4ded
Revises: b5432bb4f89f
Create Date: 2021-01-14 21:32:20.085140

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '78b997ba4ded'
down_revision = 'b5432bb4f89f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('quote', 'status',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Integer(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('quote', 'status',
               existing_type=sa.Integer(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    # ### end Alembic commands ###
