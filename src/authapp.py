import logging
from app import create_flask_app
from conf import FlaskConfig

flask_app = create_flask_app(FlaskConfig)

if __name__ == '__main__':
    flask_app.run(host="0.0.0.0", port=8000)
