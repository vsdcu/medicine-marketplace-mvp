"""move uuid generation to db

Revision ID: 659b836fa149
Revises: c94870745b54
Create Date: 2026-03-13 22:20:45.957182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '659b836fa149'
down_revision: Union[str, Sequence[str], None] = 'c94870745b54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    tables = [
        "users",
        "addresses",
        "medicines",
        "chemists",
        "chemist_prices",
        "prescriptions",
        "prescription_items",
        "orders",
        "order_items",
        "substitution_consents",
        "deliveries"
    ]

    for table in tables:
        op.alter_column(
            table,
            "id",
            server_default=sa.text("gen_random_uuid()")
        )


def downgrade():
    tables = [
        "users",
        "addresses",
        "medicines",
        "chemists",
        "chemist_prices",
        "prescriptions",
        "prescription_items",
        "orders",
        "order_items",
        "substitution_consents",
        "deliveries"
    ]

    for table in tables:
        op.alter_column(
            table,
            "id",
            server_default=None
        )