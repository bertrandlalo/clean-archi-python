from pathlib import Path
from flask import Flask, jsonify
from flask_cors import CORS

from src.domain.ports.user_repository import AbstractUserRepository
from src.adapters.csv_user_repository import CsvUserRepository

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

    return app


if __name__ == "__main__":
    config = Config()
    app = make_app()
    app.run()