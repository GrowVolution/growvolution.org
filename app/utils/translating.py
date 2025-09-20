from flask import current_app, has_app_context

from . import enabled


def _t(s: str) -> str:
    return s


def _tn(s: str, p: str, n: int) -> str:
    return p if (n != 1) else s


def _get_domain():
    return current_app.extensions["babel_domain"]


if enabled("EXT_BABEL"):
    def t(message, **variables):
        if not has_app_context():
            return _t(message)
        return _get_domain().get_translations().gettext(message, **variables)

    def tn(singular, plural, n, **variables):
        if not has_app_context():
            return _tn(singular, plural, n)
        return _get_domain().get_translations().ngettext(singular, plural, n, **variables)
else:
    t = _t
    tn = _tn
