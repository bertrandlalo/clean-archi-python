from pathlib import Path
from flask import Flask, jsonify
from flask_cors import CORS

from domain.ports.user_repository import AbstractUserRepository
from adapters.csv_user_repository import CsvUserRepository

# configuration
DEBUG = True


class Config:
    user_repo: AbstractUserRepository

    def __init__(self) -> None:
        self.user_repo = CsvUserRepository(csv_path=Path("data") / "user_repo.csv")


def make_app(config):
    # instantiate the app
    app = Flask(__name__)
    # app.config.from_object(__name__)

    # enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # sanity check route
    @app.route("/ping", methods=["GET"])
    def ping_pong():
        return jsonify("pong!")

    # sanity check route
    @app.route("/users", methods=["GET"])
    def get_all_users():
        return jsonify(config.user_repo.users)

    @app.route("/user", methods=["POST"])
    def add_new_user():
        # TODO : add_new_user.execute(...)
        pass

    return app


if __name__ == "__main__":
    config = LocalConfig()
    app = make_app(config)
    app.run()