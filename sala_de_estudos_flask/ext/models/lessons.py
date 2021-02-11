from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models.professors import Professor
from sala_de_estudos_flask.ext.models.subjects import Subject


class Lesson(db.Model):
    __tablename__ = "lessons"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    lesson_index = db.Column("lesson_index", db.Unicode(10), nullable=False, index=True)
    title = db.Column("title", db.Unicode(100), nullable=False)
    length = db.Column("length", db.Time())
    original_url = db.Column("original_url", db.Unicode(), nullable=False)
    xml_file = db.Column("xml_file", db.Unicode(length=100), nullable=False)
    index_file = db.Column("index_file", db.Unicode(100), nullable=False)
    sync_file = db.Column("sync_file", db.Unicode(100), nullable=False)
    mp4_video_file = db.Column("mp4_video_file", db.Unicode(150), nullable=False)
    webm_video_file = db.Column("webm_video_file", db.Unicode(150), nullable=False)
    thumbnail = db.Column("thumbnail", db.Unicode(100), nullable=False)

    subject_id = db.Column(
        "subject_id", db.Integer, db.ForeignKey("subjects.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    created_at = db.Column("created_at", db.DateTime(), server_default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(), server_default=db.func.now(), onupdate=db.func.now())

    subject = db.relationship(Subject, backref="lesson")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Lesson: {self.lesson_index}, " f"title: {self.title}" f">"


class ProfessorLesson(db.Model):
    __tablename__ = "professors_lessons"
    lesson_id = db.Column(
        "lesson_id", db.Integer, db.ForeignKey("lessons.id", ondelete="CASCADE", onupdate="CASCADE"), primary_key=True
    )
    subject_id = db.Column(
        "subject_id", db.Integer, db.ForeignKey("subjects.id", onupdate="CASCADE"), primary_key=True
    )
    professor_id = db.Column(
        "professor_id",
        db.Integer,
        db.ForeignKey("professors.id", ondelete="SET NULL", onupdate="CASCADE"),
        primary_key=True,
    )

    lesson = db.relationship(Lesson, backref="professor_lesson")
    subject = db.relationship(Subject, backref="professor_lesson")
    professor = db.relationship(Professor, backref="professor_lesson")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<ProfessorSubject: " f"subject_id: {self.subject_id}, " f"professor_id: {self.professor_id}" f">"
