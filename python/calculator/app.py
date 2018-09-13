from api import ApiFlask
from blueprint import bp
from exception import ApiException


def create_app():
    app = ApiFlask(__name__)
    app.register_blueprint(bp)
    app.register_error_handler(ApiException, lambda err: err.to_response())
    return app


calculator = create_app()