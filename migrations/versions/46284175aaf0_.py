"""empty message

Revision ID: 46284175aaf0
Revises: b4b142cfe63b
Create Date: 2020-05-05 21:06:33.625678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46284175aaf0'
down_revision = 'b4b142cfe63b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'pitch_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'pitch_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###