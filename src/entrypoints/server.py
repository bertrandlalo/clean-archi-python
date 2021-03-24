from typing import Tuple
from flask import Flask, jsonify, request
from flask_cors import CORS

from domain.ports.user_repository import AbstractUserRepository, InMemoryUserRepository
from domain.ports.uuid import RealUuid
from domain.use_cases.create_new_user import CreateNewUser


# configuration
DEBUG = True


class Config:
    user_repository: AbstractUserRepository

    def __init__(self):
        self.user_repository = InMemoryUserRepository()

    def get_use_cases(self) -> CreateNewUser:
        return CreateNewUser(user_repository=self.user_repository, uuid=RealUuid())


def make_app(config):
    create_new_user = config.get_use_cases()
    # instantiate the app
    app = Flask(__name__)
    # app.config.from_object(__name__)

    # enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # sanity check route
    @app.route("/ping", methods=["GET"])
    def ping_pong():
        return jsonify("pong!")

    @app.route("/user", methods=["POST"])
    def post_new_user():
        payload = request.get_json()
        create_new_user.execute(**payload)
        return jsonify("ok")

    return app


if __name__ == "__main__":
    config = Config()
    app = make_app(config)
    app.run()