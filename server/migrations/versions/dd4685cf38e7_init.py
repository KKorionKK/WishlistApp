"""init

Revision ID: dd4685cf38e7
Revises: 
Create Date: 2023-09-16 13:40:47.832788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from services.models import Base


# revision identifiers, used by Alembic.
revision: str = "dd4685cf38e7"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("user_uid", sa.String, primary_key=True),
        sa.Column("email", sa.String, nullable=False, unique=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("nickname", sa.String, nullable=False, unique=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("gender", sa.String, nullable=True),
        sa.Column("birthday", sa.DateTime(timezone=True), nullable=True),
        sa.Column("zodiac", sa.String, nullable=True),
    )
    op.create_table(
        "items",
        sa.Column("item_id", sa.String, primary_key=True),
        sa.Column("header", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("reference", sa.String, nullable=True),
        sa.Column("picture_path", sa.String, nullable=True),
    )
    op.create_table(
        "user_and_items",
        sa.Column("id", sa.Integer, autoincrement=True, primary_key=True),
        sa.Column("item_id", sa.String, nullable=False),
        sa.Column("user_uid", sa.String, nullable=False),
    )
    op.create_table(
        "parties",
        sa.Column("party_uid", sa.String, primary_key=True),
        sa.Column("owner_uid", sa.String, nullable=False),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("invite_token", sa.String, nullable=False, unique=True),
        sa.Column("max_participants", sa.Integer, nullable=False),
        sa.Column("participants", sa.Integer, nullable=False, default=0),
    )
    op.create_table(
        "party_and_users",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("party_uid", sa.String, nullable=False),
        sa.Column("user_uid", sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("items")
    op.drop_table("user_and_items")
    op.drop_table("parties")
    op.drop_table("party_and_users")
