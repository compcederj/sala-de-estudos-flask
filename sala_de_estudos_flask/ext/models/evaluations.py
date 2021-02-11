from enum import Enum

from sala_de_estudos_flask.ext.db import db
# from sala_de_estudos_flask.ext.models import Subject
from sala_de_estudos_flask.ext.models.subjects import Subject


class EvaluationTypeEnum(Enum):
    GABARITO = 1
    QUESTOES = 2
    RESPOSTAS = 3


class PeriodEnum(Enum):
    PRIMEIRO = 1
    SEGUNDO = 2


class EvaluationKey(db.Model):
    __tablename__ = "evaluation_keys"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    description = db.Column("description", db.Unicode(45), nullable=False, unique=True)
    created_at = db.Column("created_at", db.DateTime(), server_default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(), server_default=db.func.now(), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<EvaluationKey: " f"id: {self.id}, " f"description: {self.description}" f">"

    def __str__(self):
        return self.description


class Evaluation(db.Model):
    __tablename__ = "evaluations"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    type = db.Column("type", db.Enum(EvaluationTypeEnum), nullable=False)
    year = db.Column("year", db.Integer, nullable=False)
    period = db.Column("period", db.Enum(PeriodEnum), nullable=False)
    evaluation_key_id = db.Column(
        "evaluation_key_id",
        db.Integer,
        db.ForeignKey("evaluation_keys.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    download_link = db.Column("download_link", db.Unicode(), nullable=False)
    subject_id = db.Column(
        "subject_id", db.Integer, db.ForeignKey("subjects.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    created_at = db.Column("created_at", db.DateTime(), server_default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(), server_default=db.func.now(), onupdate=db.func.now())

    evaluation_key = db.relationship(EvaluationKey, backref="evaluation")
    subject = db.relationship(Subject, backref="evaluation")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (
            f"<Evaluation: "
            f"id: {self.id}, "
            f"type: {self.type}, "
            f"year: {self.year}, "
            f"period: {self.period}, "
            f"evaluation_key_id: {self.evaluation_key_id}, "
            f"download_link: {self.download_link}, "
            f"subject_id: {self.subject_id}"
            f">"
        )

    def __str__(self):
        return f"{self.subject.name}_{self.year}.{self.period}_{self.type}"
