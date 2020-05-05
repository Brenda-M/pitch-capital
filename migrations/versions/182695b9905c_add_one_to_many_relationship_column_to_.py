"""add one to many relationship column to the user and post column

Revision ID: 182695b9905c
Revises: 68df9e4f77a2
Create Date: 2020-05-05 05:02:11.042058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '182695b9905c'
down_revision = '68df9e4f77a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upvote', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('upvotes')
    # ### end Alembic commands ###
