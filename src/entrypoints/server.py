from dataclasses import asdict
from pathlib import Path
from flask import Flask, jsonify, request
from flask_cors import CORS
from adapters.csv_topic_repository import CsvTopicRepository
from adapters.csv_user_repository import CsvUserRepository
from domain.models import commands
from entrypoints.config.config import Config, get_api_host, get_api_port


def make_app(config: Config):
    create_new_user, get_all_users, create_new_topic = config.get_use_cases()

    # instantiate the app
    app = Flask(__name__)
    # if config.has_middleware:
    #     app.wsgi_app = config.wsgi_middleware(wsgi_app=app.wsgi_app)

    # enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # sanity check route
    @app.route("/ping", methods=["GET"])
    def on_get_ping():
        return jsonify("pong!")

    @app.route("/user", methods=["POST"])
    def on_post_new_user():
        result = config.bus.publish_command(commands.CreateNewUser(**request.form))
        # result = create_new_user.execute(**request.form)
        return jsonify(asdict(result)) if result else "nok"
        # try:
        #     create_new_user.execute(**request.form)
        # except UserNameAlreadyExists:
        #     return jsonify("user already exists!")
        # return jsonify("ok!")

    @app.route("/users", methods=["GET"])
    def on_get_all_users():
        users = get_all_users.execute()
        return jsonify(users)

    return app


if __name__ == "__main__":
    config = Config(
        user_repository=CsvUserRepository(csv_path=Path("data") / "user_repo"),
        topic_repository=CsvTopicRepository(csv_path=Path("data") / "topic_repo"),
    )
    app = make_app(config)
    app.run(host=get_api_host(), port=get_api_port())
