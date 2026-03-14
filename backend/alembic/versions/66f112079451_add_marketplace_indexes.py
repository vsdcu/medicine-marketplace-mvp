"""add marketplace indexes

Revision ID: 66f112079451
Revises: 659b836fa149
Create Date: 2026-03-13 22:25:15.369193

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66f112079451'
down_revision: Union[str, Sequence[str], None] = '659b836fa149'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    # chemist price lookup
    op.create_index(
        "ix_chemist_prices_chemist_medicine",
        "chemist_prices",
        ["chemist_id", "medicine_id"]
    )

    # orders by user
    op.create_index(
        "ix_orders_user_status",
        "orders",
        ["user_id", "status"]
    )

    # prescription item lookup
    op.create_index(
        "ix_prescription_items_prescription",
        "prescription_items",
        ["prescription_id"]
    )

    # chemist order queries
    op.create_index(
        "ix_orders_chemist_status",
        "orders",
        ["chemist_id", "status"]
    )


def downgrade():

    op.drop_index("ix_orders_chemist_status")
    op.drop_index("ix_prescription_items_prescription")
    op.drop_index("ix_orders_user_status")
    op.drop_index("ix_chemist_prices_chemist_medicine")
