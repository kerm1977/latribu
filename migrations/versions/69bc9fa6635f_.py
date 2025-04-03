"""empty message

Revision ID: 69bc9fa6635f
Revises: 1a7c73395852
Create Date: 2025-04-02 22:42:27.914904

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '69bc9fa6635f'
down_revision = '1a7c73395852'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file')
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img_Flyer', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('img_Flyer')

    op.create_table('file',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('filename', mysql.VARCHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
