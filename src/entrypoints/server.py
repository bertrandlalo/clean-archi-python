from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
from domain.use_cases.create_new_user import CreateNewUser
from entrypoints.config import ndb_config


def make_app(config):
    # instantiate the app
    app = Flask(__name__)
    if config.has_middleware:
        app.wsgi_app = config.wsgi_middleware(wsgi_app=app.wsgi_app)

    # enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # sanity check route
    @app.route("/ping", methods=["GET"])
    def ping_pong():
        return jsonify("pong!")

    # sanity check route
    @app.route("/users", methods=["GET"])
    def get_all_users():
        return jsonify(users=config.user_repo.users)

    @app.route("/user", methods=["POST"])
    def add_new_user():
        # config.user_repo.add()
        json_data = request.get_json()
        print(json_data)

        CreateNewUser(user_repository=config.user_repo)
        return 'ok', 200

    return app


if __name__ == "__main__":
    app = make_app(ndb_config)
    app.run()
