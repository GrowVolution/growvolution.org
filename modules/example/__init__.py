from flask import Blueprint, Flask

from app.utils import enabled
from .data import init_models

NAME = "example"
bp = Blueprint(NAME, __name__, template_folder="templates", static_folder="static")


@bp.context_processor
def context_processor():
    return dict(
        NAME=NAME
    )


def register_module(app: Flask, home: bool):
    from .routes import init_routes
    init_routes(bp)

    if home:
        bp.static_url_path = f"/{NAME}/static"
    else:
        bp.url_prefix = f"/{NAME}"

    app.register_blueprint(bp)

    if enabled("EXT_SQLALCHEMY"):
        init_models()
