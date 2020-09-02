from flask import Flask
from flask_admin import Admin


admin = Admin()


def init_app(app: Flask):
    admin.name = app.config["ADMIN_NAME"]
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.url = "/admin"
