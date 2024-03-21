"""empty message

Revision ID: 60646d688c63
Revises: 
Create Date: 2024-03-22 00:22:41.293781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60646d688c63'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logtable',
    sa.Column('log_id', sa.Integer(), nullable=False),
    sa.Column('operation', sa.String(length=255), nullable=True),
    sa.Column('createdBy', sa.String(length=344), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('log_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=233), nullable=True),
    sa.Column('password', sa.String(length=234), nullable=True),
    sa.Column('log_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['log_id'], ['logtable.log_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('logtable')
    # ### end Alembic commands ###
