"""Add omer_id colun in heroes table 

Revision ID: 365bd6957782
Revises: 
Create Date: 2026-02-04 16:29:44.120903

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '365bd6957782'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('heroes', sa.Column("owner_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "fk_heroes_owner_id",
        "heroes",
        "players",
        ["owner_id"],
        ["id"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("fk_heroes_owner_id_players", "heroes", type_="foreignkey")
    op.drop_column("heroes", "owner_id")

