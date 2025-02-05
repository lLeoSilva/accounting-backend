"""Add new fields to users table

Revision ID: cd13797c0b1f
Revises: afcf5e92a84d
Create Date: 2025-02-04 21:54:31.144600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd13797c0b1f'
down_revision: Union[str, None] = 'afcf5e92a84d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('fname', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('lname', sa.String(length=100), nullable=True))
    op.add_column('users', sa.Column('role', sa.String(length=20), nullable=False))
    op.add_column('users', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('NOW()'), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('NOW()'), nullable=True))
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'is_active')
    op.drop_column('users', 'role')
    op.drop_column('users', 'lname')
    op.drop_column('users', 'fname')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
