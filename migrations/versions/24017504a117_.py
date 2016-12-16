"""empty message

Revision ID: 24017504a117
Revises: 0ac3fd02c230
Create Date: 2016-08-20 11:07:34.670947

"""

# revision identifiers, used by Alembic.
revision = '24017504a117'
down_revision = '0ac3fd02c230'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('page', sa.String(), nullable=True),
    sa.Column('size', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image_sizes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_width', sa.Integer(), nullable=True),
    sa.Column('full_height', sa.Integer(), nullable=True),
    sa.Column('icon_width', sa.Integer(), nullable=True),
    sa.Column('icon_height', sa.Integer(), nullable=True),
    sa.Column('thumbnail_width', sa.Integer(), nullable=True),
    sa.Column('thumbnail_height', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image_sizes')
    op.drop_table('image_config')
    ### end Alembic commands ###