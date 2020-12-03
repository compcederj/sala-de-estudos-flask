from abc import ABC

from flask import jsonify, request, redirect


class Controller(ABC):
    def __init__(self):
        pass

    @property
    def data(self):
        return request.get_json()

    @staticmethod
    def index():
        pass

    @staticmethod
    def make_error(status_code, status, description):
        response = jsonify({
            "http_status": status_code,
            "status": status,
            "code": status_code,
            "description": description
        })
        response.status_code = status_code
        return response

    @staticmethod
    def as_json(data, status_code=200):
        response = jsonify(data)
        response.status_code = status_code
        return response

    @staticmethod
    def redirect(whatsapp_link):
        return redirect(whatsapp_link)
