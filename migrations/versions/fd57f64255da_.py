"""empty message

Revision ID: fd57f64255da
Revises: d9d9709d357d
Create Date: 2020-09-10 19:42:44.057734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd57f64255da'
down_revision = 'd9d9709d357d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lessons', sa.Column('lesson_index', sa.Unicode(length=10), nullable=False))
    op.add_column('lessons', sa.Column('xml_file', sa.Unicode(length=100), nullable=False))
    op.create_index(op.f('ix_lessons_lesson_index'), 'lessons', ['lesson_index'], unique=False)
    op.drop_index('ix_lessons_index', table_name='lessons')
    op.drop_column('lessons', 'index')
    op.alter_column(
        "lessons",
        "webm_video_file",
        existing_type=sa.Unicode(length=100),
        type_=sa.Unicode(length=150),
        existing_nullable=False
    )
    op.alter_column(
        "lessons",
        "mp4_video_file",
        existing_type=sa.Unicode(length=100),
        type_=sa.Unicode(length=150),
        existing_nullable=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lessons', sa.Column('index', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_index('ix_lessons_index', 'lessons', ['index'], unique=False)
    op.drop_index(op.f('ix_lessons_lesson_index'), table_name='lessons')
    op.drop_column('lessons', 'lesson_index')
    op.drop_column('lessons', 'xml_file')
    op.alter_column(
        "lessons",
        "webm_video_file",
        existing_type=sa.Unicode(length=150),
        type_=sa.Unicode(length=100),
        existing_nullable=False
    )
    op.alter_column(
        "lessons",
        "mp4_video_file",
        existing_type=sa.Unicode(length=150),
        type_=sa.Unicode(length=100),
        existing_nullable=False
    )
    # ### end Alembic commands ###
