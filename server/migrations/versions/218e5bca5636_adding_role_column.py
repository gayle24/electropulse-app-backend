"""adding role column

Revision ID: 218e5bca5636
Revises: fd0e34b92b6d
Create Date: 2023-11-09 15:18:06.453623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '218e5bca5636'
down_revision = 'fd0e34b92b6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###
