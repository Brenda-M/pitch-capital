"""add category column into pitchtable

Revision ID: b1c17d28e72e
Revises: 829ac919ab68
Create Date: 2020-05-05 07:05:48.824776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1c17d28e72e'
down_revision = '829ac919ab68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###