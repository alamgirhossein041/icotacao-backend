"""empty message

Revision ID: 20d7d737863e
Revises: bd79f6cc4c43
Create Date: 2021-01-14 12:48:09.732781

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '20d7d737863e'
down_revision = 'bd79f6cc4c43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('id', table_name='provider_segment')
    op.drop_table('provider_segment')
    op.drop_constraint('quote_proposal_ibfk_2', 'quote_proposal', type_='foreignkey')
    op.drop_column('quote_proposal', 'provider_id')
    try:
        op.drop_index('id', table_name='provider')
        op.drop_table('provider')
        op.create_table('supplier',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('social_name', sa.String(length=256), nullable=False),
        sa.Column('email', sa.String(length=256), nullable=False),
        sa.Column('cell_phone', sa.String(length=256), nullable=False),
        sa.Column('cnpj', sa.String(length=256), nullable=True),
        sa.Column('status', sa.Boolean(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('id')
        )
    except:
        pass
    op.create_table('supplier_address',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('code_post', sa.String(length=256), nullable=True),
    sa.Column('street', sa.String(length=256), nullable=True),
    sa.Column('number', sa.String(length=256), nullable=True),
    sa.Column('district', sa.String(length=256), nullable=True),
    sa.Column('complement', sa.String(length=256), nullable=True),
    sa.Column('lat', sa.String(length=256), nullable=True),
    sa.Column('long', sa.String(length=256), nullable=True),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('supplier_segment',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.Column('segment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['segment_id'], ['segment.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.add_column('quote_proposal', sa.Column('supplier_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'quote_proposal', 'supplier', ['supplier_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quote_proposal', sa.Column('provider_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'quote_proposal', type_='foreignkey')
    op.create_foreign_key('quote_proposal_ibfk_2', 'quote_proposal', 'provider', ['provider_id'], ['id'])
    op.drop_column('quote_proposal', 'supplier_id')
    op.create_table('provider_segment',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
    sa.Column('provider_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('segment_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['provider_id'], ['provider.id'], name='provider_segment_ibfk_1'),
    sa.ForeignKeyConstraint(['segment_id'], ['segment.id'], name='provider_segment_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'provider_segment', ['id'], unique=True)
    try:
        op.create_table('provider',
        sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
        sa.Column('created_at', mysql.DATETIME(), nullable=True),
        sa.Column('updated_at', mysql.DATETIME(), nullable=True),
        sa.Column('deleted_at', mysql.DATETIME(), nullable=True),
        sa.Column('email', mysql.VARCHAR(length=256), nullable=False),
        sa.Column('cell_phone', mysql.VARCHAR(length=256), nullable=False),
        sa.Column('cnpj', mysql.VARCHAR(length=256), nullable=True),
        sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
        sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
        sa.Column('social_name', mysql.VARCHAR(length=256), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='provider_ibfk_1'),
        sa.PrimaryKeyConstraint('id'),
        mysql_default_charset='latin1',
        mysql_engine='InnoDB'
        )
        op.create_index('id', 'provider', ['id'], unique=True)
        op.drop_table('supplier')
    except:
        pass
    op.drop_table('supplier_segment')
    op.drop_table('supplier_address')
    # ### end Alembic commands ###
