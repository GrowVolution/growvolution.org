from . import enabled

if enabled("EXT_BABEL"):
    from flask_babelplus import gettext as t, ngettext as tn
else:
    def t(s: str) -> str:
        return s
    def tn(s: str, p: str, n: int) -> str:
        return p if (n != 1) else s
