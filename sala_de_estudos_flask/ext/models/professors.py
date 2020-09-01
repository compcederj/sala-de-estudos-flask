from datetime import datetime

from sala_de_estudos_flask.ext.db import db


class Professor(db.Model):
    __tablename__ = "professors"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.Unicode(70), nullable=False)
    email = db.Column("email", db.Unicode(100))
    site = db.Column("site", db.Unicode())
    created_at = db.Column("created_at", db.DateTime(), server_default=db.func.now())
    updated_at = db.Column("updated_at", db.DateTime(), server_default=db.func.now(), onupdate=db.func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"<Professor: "
                f"id: {self.id}, "
                f"name: {self.name}, "
                f"email: {self.email}, "
                f"site: {self.site}"
                f">")
