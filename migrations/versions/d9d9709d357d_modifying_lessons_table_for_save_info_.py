"""Modifying Lessons table for save info from lesson's metadata files

Revision ID: d9d9709d357d
Revises: d682e7dfd646
Create Date: 2020-09-10 00:22:54.003105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9d9709d357d'
down_revision = 'd682e7dfd646'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lessons', sa.Column('index_file', sa.Unicode(length=100), nullable=False))
    op.add_column('lessons', sa.Column('mp4_video_file', sa.Unicode(length=100), nullable=False))
    op.add_column('lessons', sa.Column('original_url', sa.Unicode(), nullable=False))
    op.add_column('lessons', sa.Column('sync_file', sa.Unicode(length=100), nullable=False))
    op.add_column('lessons', sa.Column('thumbnail', sa.Unicode(length=100), nullable=False))
    op.add_column('lessons', sa.Column('webm_video_file', sa.Unicode(length=100), nullable=False))
    op.alter_column('lessons', 'title',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.create_index(op.f('ix_lessons_index'), 'lessons', ['index'], unique=False)
    op.drop_column('lessons', 'url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lessons', sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_lessons_index'), table_name='lessons')
    op.alter_column('lessons', 'title',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.drop_column('lessons', 'webm_video_file')
    op.drop_column('lessons', 'thumbnail')
    op.drop_column('lessons', 'sync_file')
    op.drop_column('lessons', 'original_url')
    op.drop_column('lessons', 'mp4_video_file')
    op.drop_column('lessons', 'index_file')
    # ### end Alembic commands ###
