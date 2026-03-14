"""add user roles

Revision ID: ef721419d9b2
Revises: 004c4a238639
Create Date: 2026-03-13 23:09:54.522747
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


revision: str = 'ef721419d9b2'
down_revision: Union[str, Sequence[str], None] = '004c4a238639'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    userrole = sa.Enum(
        'customer',
        'chemist',
        'admin',
        name='userrole'
    )

    userrole.create(op.get_bind(), checkfirst=True)

    op.add_column(
        'users',
        sa.Column(
            'role',
            sa.Enum('customer','chemist','admin', name='userrole'),
            nullable=False,
            server_default='customer'
        )
    )


def downgrade() -> None:

    op.drop_column('users', 'role')

    sa.Enum(
        'customer',
        'chemist',
        'admin',
        name='userrole'
    ).drop(op.get_bind(), checkfirst=True)