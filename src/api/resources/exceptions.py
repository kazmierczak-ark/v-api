from uuid import uuid4

from flask import current_app

from api.business_logic.models.common import BadRequestError, Unauthorized


def _render_bad_request(exception):
    error_id = str(uuid4())
    current_app.logger.error(f"{error_id}: {str(exception)}")
    return {"id": error_id, "title": "Bad Request", "detail": str(exception), "status": 400}, 400


def _render_unauthorized(exception):
    error_id = str(uuid4())
    current_app.logger.error(f"{error_id}: {str(exception)}")
    return {"id": error_id, "title": "Unauthorized", "detail": "Incorrect / Expired authentication header",
            "status": 401}, 401


def _render_unknown_error(exception):
    error_id = str(uuid4())
    current_app.logger.error(f"{error_id}: {str(exception)}")
    return {"id": error_id, "title": "Internal Server Error", "status": 500}, 500


def set_error_handlers(app):
    app.add_error_handler(Unauthorized, _render_unauthorized)
    app.add_error_handler(BadRequestError, _render_bad_request)

    app.add_error_handler(Exception, _render_unknown_error)
