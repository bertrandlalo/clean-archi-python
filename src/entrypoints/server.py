from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True


class Config:
    pass


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

    return app


if __name__ == "__main__":
    config = Config()
    app = make_app(config)
    app.run()