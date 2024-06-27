"""empty message

Revision ID: dd598e496bb3
Revises: 540c07746c32
Create Date: 2024-06-27 13:51:49.024244

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd598e496bb3'
down_revision = '540c07746c32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.alter_column('etiqueta',
               existing_type=mysql.VARCHAR(length=200),
               type_=sa.String(length=500),
               existing_nullable=False)
        batch_op.alter_column('descripcion',
               existing_type=mysql.VARCHAR(length=200),
               type_=sa.String(length=500),
               existing_nullable=True)
        batch_op.alter_column('atributos',
               existing_type=mysql.VARCHAR(length=200),
               type_=sa.String(length=500),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.alter_column('atributos',
               existing_type=sa.String(length=500),
               type_=mysql.VARCHAR(length=200),
               existing_nullable=True)
        batch_op.alter_column('descripcion',
               existing_type=sa.String(length=500),
               type_=mysql.VARCHAR(length=200),
               existing_nullable=True)
        batch_op.alter_column('etiqueta',
               existing_type=sa.String(length=500),
               type_=mysql.VARCHAR(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###
