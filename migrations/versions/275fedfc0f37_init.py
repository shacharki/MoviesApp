"""init

Revision ID: 275fedfc0f37
Revises: 
Create Date: 2024-02-05 00:33:30.570738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '275fedfc0f37'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###
