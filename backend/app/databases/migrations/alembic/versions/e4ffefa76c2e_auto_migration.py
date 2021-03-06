"""Auto migration

Revision ID: e4ffefa76c2e
Revises: 
Create Date: 2021-08-23 22:48:51.421410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4ffefa76c2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=500), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('update_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='apot'
    )
    op.create_index(op.f('ix_apot_user_id'), 'user', ['id'], unique=False, schema='apot')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_apot_user_id'), table_name='user', schema='apot')
    op.drop_table('user', schema='apot')
    # ### end Alembic commands ###