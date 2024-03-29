"""empty message

Revision ID: 7f1d14d8406d
Revises: 
Create Date: 2024-03-18 12:16:18.095775

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7f1d14d8406d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('alergias',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('cronico',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('medicamentos',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('nacimiento',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
        batch_op.drop_index('confirmpassword')
        batch_op.drop_index('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('password', ['password'], unique=True)
        batch_op.create_index('confirmpassword', ['confirmpassword'], unique=True)
        batch_op.alter_column('nacimiento',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
        batch_op.alter_column('medicamentos',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('cronico',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('alergias',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###
