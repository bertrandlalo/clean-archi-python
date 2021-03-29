from pathlib import Path
from typing import Tuple
from flask import Flask, jsonify, request
from flask_cors import CORS

from domain.ports.user_repository import AbstractUserRepository
from domain.ports.uuid import RealUuid
from domain.use_cases.create_new_user import CreateNewUser
from domain.use_cases.get_all_users import GetAllUsers
from adapters.csv_user_repository import CsvUserRepository
from helpers.csv import reset_file_from_path

# configuration
DEBUG = True


class Config:
    user_repository: AbstractUserRepository

    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    def get_use_cases(self) -> Tuple[CreateNewUser, GetAllUsers]:
        return (
            CreateNewUser(user_repository=self.user_repository, uuid=RealUuid()),
            GetAllUsers(user_repository=self.user_repository),
        )


def make_app(config):
    create_new_user, get_all_users = config.get_use_cases()
    # instantiate the app
    app = Flask(__name__)
    # app.config.from_object(__name__)

    # enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # sanity check route
    @app.route("/ping", methods=["GET"])
    def on_get_ping():
        return jsonify("pong!")

    @app.route("/user", methods=["POST"])
    def on_post_new_user():
        create_new_user.execute(**request.form)
        return jsonify("ok!")

    @app.route("/users", methods=["GET"])
    def on_get_all_users():
        users = get_all_users.execute()
        return jsonify(users)

    @app.route("/user", methods=["POST"])
    def add_new_user():
        # TODO : add_new_user.execute(...)
        pass

    return app


if __name__ == "__main__":
    csv_path = Path("data") / "user_repo.csv"
    user_repository = CsvUserRepository(csv_path=csv_path)
    reset_file_from_path(csv_path)
    config = Config(user_repository)
    app = make_app(config)
    app.run()