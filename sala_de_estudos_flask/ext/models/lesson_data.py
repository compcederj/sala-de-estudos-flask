from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models.lessons import Lesson


class LessonData(db.Model):
    __tablename__ = "lesson_data"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    raw_xml = db.Column("xml_raw_data", db.Text)
    json_xml = db.Column("json_xml", db.JSON)
    raw_index = db.Column("raw_index", db.Text)
    json_index = db.Column("json_index", db.JSON)
    raw_sync = db.Column("raw_sync", db.Text)
    json_sync = db.Column("json_sync", db.JSON)

    lesson_id = db.Column(
        "lesson_id",
        db.Integer,
        db.ForeignKey("lessons.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        unique=True
    )

    created_at = db.Column("created_at", db.DateTime(), server_default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(), server_default=db.func.now(), onupdate=db.func.now())

    lesson = db.relationship(Lesson, backref="LessonData")
