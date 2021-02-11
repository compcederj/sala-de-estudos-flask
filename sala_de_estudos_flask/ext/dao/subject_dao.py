from typing import Dict, List, Union

from sala_de_estudos_flask.ext.db import db
from sala_de_estudos_flask.ext.models.subjects import Subject


class SubjectsDAO:

    @staticmethod
    def list_all() -> List[Dict[str, Union[int, str]]]:
        subjects = db.session.query(Subject.id, Subject.code, Subject.name, Subject.material_design_icon).all()
        subjects = [
            {
                "id": subject[0],
                "code": subject[1],
                "name": subject[2],
                "material_design_icon": subject[3]
            }
            for subject in subjects
        ]
        return subjects

    @staticmethod
    def get_by_id(id_) -> Subject:
        subject = db.session.query(Subject).filter(Subject.id == id_).first()
        return subject

    @staticmethod
    def get_whatsapp_link_by_id(id_) -> str:
        whatsapp_link = db.session.query(Subject.whatsapp_link).filter(Subject.id == id_).first()
        if whatsapp_link:
            return whatsapp_link[0]
        return ""
