from enum import Enum

from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models.professors import Professor


class SubjectTypeEnum(Enum):
    OBRIGATORIA = 1
    OPCIONAL = 2


class Subject(db.Model):
    __tablename__ = "subjects"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)

    code = db.Column("code", db.Unicode(8), unique=True, nullable=False)
    name = db.Column("name", db.Unicode(70), nullable=False)
    type = db.Column("type", db.Enum(SubjectTypeEnum), nullable=False)

    workload = db.Column("workload", db.Integer, nullable=False)
    amount_lessons = db.Column("amount_lessons", db.Integer, nullable=False, default=0)

    drive_link = db.Column("drive_link", db.Unicode())
    whatsapp_link = db.Column("whatsapp_link", db.Unicode())
    telegram_link = db.Column("telegram_link", db.Unicode())
    github_link = db.Column("github_link", db.Unicode())

    material_design_icon = db.Column("material_design_icon", db.Unicode())

    created_at = db.Column("created_at", db.DateTime(), server_default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(), server_default=db.func.now(), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Subject: {self.name}, " f"code: {self.code}" f">"


class ProfessorSubject(db.Model):
    __tablename__ = "professors_subjects"
    subject_id = db.Column(
        "subject_id", db.Integer, db.ForeignKey("subjects.id", onupdate="CASCADE"), primary_key=True
    )
    professor_id = db.Column(
        "professor_id",
        db.Integer,
        db.ForeignKey("professors.id", ondelete="SET NULL", onupdate="CASCADE"),
        primary_key=True,
    )

    subject = db.relationship(Subject, backref="professor_subject")
    professor = db.relationship(Professor, backref="professor_subject")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<ProfessorSubject: " f"subject: {self.subject.name}, " f"professor: {self.professor.name}" f">"
