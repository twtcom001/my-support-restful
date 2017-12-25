"""empty message

Revision ID: 44e33da91223
Revises: 
Create Date: 2017-12-24 03:20:16.044511

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44e33da91223'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('op_time', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('local_id', sa.String(length=64), nullable=True),
    sa.Column('familia', sa.String(length=64), nullable=True),
    sa.Column('genus', sa.String(length=40), nullable=True),
    sa.Column('genus_id', sa.String(length=40), nullable=True),
    sa.Column('icbn_name', sa.String(length=255), nullable=True),
    sa.Column('chinese_name', sa.String(length=100), nullable=True),
    sa.Column('info_url', sa.String(length=255), nullable=True),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('local_id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_role_default'), 'role', ['default'], unique=False)
    op.create_table('introduce',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('introduce_id', sa.String(length=40), nullable=True),
    sa.Column('introduce_from', sa.String(length=100), nullable=True),
    sa.Column('introduce_price', sa.String(length=20), nullable=True),
    sa.Column('introduce_date', sa.String(length=20), nullable=True),
    sa.Column('palnts_id', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['palnts_id'], ['plants.local_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('avatar_hash', sa.String(length=32), nullable=True),
    sa.Column('head_img', sa.String(length=200), nullable=True),
    sa.Column('is_valid', sa.Boolean(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('introduce')
    op.drop_index(op.f('ix_role_default'), table_name='role')
    op.drop_table('role')
    op.drop_table('plants')
    op.drop_table('logs')
    # ### end Alembic commands ###
