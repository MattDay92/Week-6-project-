"""empty message

Revision ID: 12216c223098
Revises: 1b69127ee553
Create Date: 2023-01-28 09:48:31.624662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12216c223098'
down_revision = '1b69127ee553'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('img_url', sa.String(), nullable=False),
    sa.Column('details', sa.String(length=1000), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###
