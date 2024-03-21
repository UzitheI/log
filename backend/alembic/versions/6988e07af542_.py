"""empty message

Revision ID: 6988e07af542
Revises: ceb14e23c129
Create Date: 2024-03-22 01:08:59.863146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6988e07af542'
down_revision: Union[str, None] = 'ceb14e23c129'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('logtable', sa.Column('user_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('logtable', 'user_id')
    # ### end Alembic commands ###