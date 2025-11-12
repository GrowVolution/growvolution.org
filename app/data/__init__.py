from pathlib import Path
from importlib import import_module

_package = Path(__file__).parent


def init_models():
    for file in _package.rglob("*.py"):
        if file.stem == "__init__":
            continue
        import_module(f"app.data.{file.stem}")


def add_model(model):
    from ..extensions import db
    db.

