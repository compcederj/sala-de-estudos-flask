import os.path

from connexion import FlaskApp
from flask import Flask, redirect
import json

import click
import dynaconf
from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin
)
from oauthlib.oauth2 import WebApplicationClient
import requests

from sala_de_estudos_flask.ext import config
from sala_de_estudos_flask.ext.api import add_apis

GOOGLE_CLIENT_ID = dynaconf.settings('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = dynaconf.settings('GOOGLE_CLIENT_SECRET')
GOOGLE_DISCOVERY_URL = dynaconf.settings('GOOGLE_DISCOVERY_URL')


class User(UserMixin):
    users = []

    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        for user in User.users:
            if user.id == user_id:
                return user

    @staticmethod
    def create(id_, name, email, profile_pic):
        user = User(id_, name, email, profile_pic)
        User.users.append(user)
        return user

    @staticmethod
    def get_or_create(user_id, name, email, profile_pic):
        return User.get(user_id) or User.create(user_id, name, email, profile_pic)


def create_app() -> Flask:
    basedir = os.path.abspath(os.path.dirname(__file__))
    connexion_app = FlaskApp(__name__, specification_dir=basedir)

    app = connexion_app.app
    config.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    client = WebApplicationClient(GOOGLE_CLIENT_ID)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    add_apis(connexion_app)

    @app.route("/")
    def home():
        # return redirect("http://saladeestudos.online")
        if current_user.is_authenticated:
            return (
                "<p>Hello, {}! You're logged in! Email: {}</p>"
                "<div><p>Google Profile Picture:</p>"
                '<img src="{}" alt="Google profile pic"></img></div>'
                '<a class="button" href="/logout">Logout</a>'.format(
                    current_user.name, current_user.email, current_user.profile_pic
                )
            )
        else:
            return '<a class="button" href="/login">Google Login</a>'

    def get_google_provider_config():
        return requests.get(GOOGLE_DISCOVERY_URL).json()

    @app.route("/login")
    def login():
        google_provider_config = get_google_provider_config()
        authorization_endpoint = google_provider_config.get("authorization_endpoint")
        request_uri = client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri=request.base_url + "/callback",
            scope=["openid", "email", "profile"],
        )
        return redirect(request_uri)

    @app.route("/login/callback")
    def callback():
        code = request.args.get("code")
        google_provider_config = get_google_provider_config()

        token_endpoint = google_provider_config.get("token_endpoint")
        token_url, headers, body = client.prepare_token_request(
            token_endpoint,
            authorization_response=request.url,
            redirect_url=request.base_url,
            code=code
        )
        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
        )
        client.parse_request_body_response(json.dumps(token_response.json()))
        userinfo_endpoint = google_provider_config.get("userinfo_endpoint")
        uri, headers, body = client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)

        userinfo = userinfo_response.json()
        if userinfo.get("email_verified"):
            click.echo(userinfo)
            unique_id = userinfo.get("sub")
            users_name = userinfo.get("given_name")
            users_email = userinfo.get("email")
            picture = userinfo.get("picture")
        else:
            return "User email not available or not verified by Google", 400

        user = User.get_or_create(unique_id, users_name, users_email, picture)

        login_user(user)

        return redirect(url_for("home"))

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("home"))

    return app
