"""Add academic term constraints

Revision ID: d0737ab4ae52
Revises: 142028b27402
Create Date: 2026-11-04 00:23:43.123945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0737ab4ae52'
down_revision: Union[str, Sequence[str], None] = '142028b27402'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""

    op.create_unique_constraint(
        'uq_academic_term_name_year',
        'academic_terms',
        ['name', 'academic_year']
    )

    op.create_check_constraint(
        'check_academic_term_dates',
        'academic_terms',
        'end_date >= start_date'
    )

    op.alter_column(
        'teachers',
        'full_name',
        existing_type=sa.VARCHAR(length=50),
        type_=sa.String(length=150),
        existing_nullable=False
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.alter_column(
        'teachers',
        'full_name',
        existing_type=sa.String(length=150),
        type_=sa.VARCHAR(length=50),
        existing_nullable=False
    )

    op.drop_constraint(
        'check_academic_term_dates',
        'academic_terms',
        type_='check'
    )

    op.drop_constraint(
        'uq_academic_term_name_year',
        'academic_terms',
        type_='unique'
    )

