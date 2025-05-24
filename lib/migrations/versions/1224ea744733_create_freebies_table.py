"""Create freebies table

Revision ID: 1224ea744733
Revises: 5f72c58bf48c
Create Date: 2025-05-25 01:08:20.394784

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1224ea744733'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=True),
        sa.Column('value', sa.Integer(), nullable=True),
        sa.Column('dev_id', sa.Integer(), nullable=True),
        sa.Column('company_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], name='fk_freebies_dev_id_devs'),
        sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name='fk_freebies_company_id_companies'),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('freebies')