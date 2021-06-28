"""empty message

Revision ID: 37ec846e06cc
Revises: b59ccd5d8157
Create Date: 2021-06-28 00:11:45.627203

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '37ec846e06cc'
down_revision = 'b59ccd5d8157'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artists',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('city', sa.String(length=120), nullable=True),
                    sa.Column('state', sa.String(length=120), nullable=True),
                    sa.Column('phone', sa.String(length=120), nullable=True),
                    sa.Column('genres', sa.String(length=120), nullable=True),
                    sa.Column('image_link', sa.String(length=500), nullable=True),
                    sa.Column('facebook_link', sa.String(length=120), nullable=True),
                    sa.Column('website_link', sa.String(length=120), nullable=True),
                    sa.Column('seeking_venue', sa.Boolean(), nullable=True),
                    sa.Column('seeking_description', sa.String(length=1000), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('Shows',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('venue_id', sa.Integer(), nullable=True),
                    sa.Column('artist_id', sa.Integer(), nullable=True),
                    sa.Column('start_time', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('Venues',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('city', sa.String(length=120), nullable=True),
                    sa.Column('state', sa.String(length=120), nullable=True),
                    sa.Column('address', sa.String(length=120), nullable=True),
                    sa.Column('phone', sa.String(length=120), nullable=True),
                    sa.Column('image_link', sa.String(length=500), nullable=True),
                    sa.Column('facebook_link', sa.String(length=120), nullable=True),
                    sa.Column('genres', sa.String(length=120), nullable=True),
                    sa.Column('website_link', sa.String(length=120), nullable=True),
                    sa.Column('seeking_venue', sa.Boolean(), nullable=True),
                    sa.Column('seeking_description', sa.String(length=1000), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.drop_table('Artist')
    op.drop_table('Venue')
    op.drop_table('Show')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Show_id_seq"\'::regclass)'),
                              autoincrement=True, nullable=False),
                    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=True),
                    sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='Show_pkey')
                    )
    op.create_table('Venue',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Venue_id_seq"\'::regclass)'),
                              autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('address', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
                    sa.Column('facebook_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('website_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('seeking_description', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
                    sa.Column('seeking_venue', sa.BOOLEAN(), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='Venue_pkey')
                    )
    op.create_table('Artist',
                    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Artist_id_seq"\'::regclass)'),
                              autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
                    sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('state', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
                    sa.Column('facebook_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('website_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
                    sa.Column('seeking_venue', sa.BOOLEAN(), autoincrement=False, nullable=True),
                    sa.Column('seeking_description', sa.VARCHAR(length=1000), autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='Artist_pkey')
                    )
    op.drop_table('Venues')
    op.drop_table('Shows')
    op.drop_table('Artists')
    # ### end Alembic commands ###
