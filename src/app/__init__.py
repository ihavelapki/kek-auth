from flask import Flask


def create_flask_app(config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config)

    flask_app.app_context().push()

    from .routes.auth import auth_bp
    flask_app.register_blueprint(auth_bp)

    return flask_app
