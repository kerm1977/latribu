"""empty message

Revision ID: 3b8f8fdebd39
Revises: 545ba4aac6ac
Create Date: 2024-08-15 15:13:52.831550

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3b8f8fdebd39'
down_revision = '545ba4aac6ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('multimedia', schema=None) as batch_op:
        batch_op.drop_constraint('multimedia_ibfk_1', type_='foreignkey')
        batch_op.drop_column('poster_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('multimedia', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poster_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('multimedia_ibfk_1', 'user', ['poster_id'], ['id'])

    # ### end Alembic commands ###