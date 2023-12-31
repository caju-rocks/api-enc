"""adding grade field

Revision ID: 41a6c4b6ae14
Revises: 717a67183018
Create Date: 2023-06-25 11:17:07.471240

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '41a6c4b6ae14'
down_revision = '717a67183018'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('climb_routes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('grade', postgresql.JSON(astext_type=sa.Text()), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('climb_routes', schema=None) as batch_op:
        batch_op.drop_column('grade')

    # ### end Alembic commands ###
