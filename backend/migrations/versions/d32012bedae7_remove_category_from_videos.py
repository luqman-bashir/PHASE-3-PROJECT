"""Remove category from videos

Revision ID: d32012bedae7
Revises: aafcc606f494
Create Date: 2024-12-20 16:34:46.412569

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd32012bedae7'
down_revision: Union[str, None] = 'aafcc606f494'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('videos', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('videos', 'youtube_url',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('videos', 'uploaded_by',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_index(op.f('ix_videos_id'), 'videos', ['id'], unique=False)
    op.create_index(op.f('ix_videos_title'), 'videos', ['title'], unique=False)
    op.create_index(op.f('ix_videos_youtube_url'), 'videos', ['youtube_url'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_videos_youtube_url'), table_name='videos')
    op.drop_index(op.f('ix_videos_title'), table_name='videos')
    op.drop_index(op.f('ix_videos_id'), table_name='videos')
    op.alter_column('videos', 'uploaded_by',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('videos', 'youtube_url',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('videos', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
