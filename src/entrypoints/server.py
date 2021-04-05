from flask import Flask, jsonify, request
from flask_cors import CORS

from entrypoints.config.config import Config


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
        create_new_user.execute(**request.form)
        return jsonify("ok!")

    @app.route("/users", methods=["GET"])
    def on_get_all_users():
        users = get_all_users.execute()
        return jsonify(users)

    return app


if __name__ == "__main__":
    app = make_app(ndb_config)
    app.run()
