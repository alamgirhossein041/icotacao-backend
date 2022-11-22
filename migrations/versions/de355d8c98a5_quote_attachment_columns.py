"""quote_attachment_columns

Revision ID: de355d8c98a5
Revises: adc388b02e2f
Create Date: 2020-12-29 18:13:28.950620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de355d8c98a5'
down_revision = 'adc388b02e2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quote', sa.Column('file_key', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('quote', 'file_key')
    # ### end Alembic commands ###
