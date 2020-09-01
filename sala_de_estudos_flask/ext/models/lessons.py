from datetime import datetime

from sala_de_estudos_flask.ext.db import db


class Lesson(db.Model):
    __tablename__ = "lessons"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    index = db.Column("index", db.Integer, nullable=False)
    title = db.Column("title", db.Unicode(100))
    length = db.Column("length", db.Time())
    url = db.Column("url", db.Unicode(), nullable=False)
    subject_id = db.Column(
        "subject_id",
        db.Integer,
        db.ForeignKey("subjects.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
    )
    created_at = db.Column("created_at", db.DateTime(), server_default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(), server_default=db.func.now(), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"<Lesson: "
                f"id: {self.id}, "
                f"index: {self.index}, "
                f"title: {self.title}, "
                f"length: {self.length}, "
                f"url: {self.url}, "
                f"subject_id: {self.subject_id}"
                f">")


class ProfessorLesson(db.Model):
    __tablename__ = "professors_lessons"
    lesson_id = db.Column(
        "lesson_id",
        db.Integer,
        db.ForeignKey("lessons.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True
    )
    subject_id = db.Column(
        "subject_id",
        db.Integer,
        db.ForeignKey("subjects.id", onupdate="CASCADE"),
        primary_key=True
    )
    professor_id = db.Column(
        "professor_id",
        db.Integer,
        db.ForeignKey("professors.id", ondelete="SET NULL", onupdate="CASCADE"),
        primary_key=True
    )

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"<ProfessorSubject: "
                f"subject_id: {self.subject_id}, "
                f"professor_id: {self.professor_id}"
                f">")
