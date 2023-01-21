"""empty message

Revision ID: bae3670ad80c
Revises: 099a27b88983
Create Date: 2023-01-18 19:17:32.805638

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bae3670ad80c'
down_revision = '099a27b88983'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('request')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('index', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('response_time', mysql.FLOAT(), nullable=True),
    sa.Column('date', mysql.DATETIME(), nullable=True),
    sa.Column('method', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('size', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('status_code', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('path', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('user_agent', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('remote_address', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('exception', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('referrer', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('browser', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('platform', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('mimetype', mysql.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('index'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###