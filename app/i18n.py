from flask_babelplus import Domain, get_locale
from babel.support import Translations
from flask import Flask, current_app

from .data.babel import I18nMessage
from .utils.translating import t, tn


class DBMergedTranslations(Translations):
    def __init__(self, wrapped: Translations, domain: str, locale: str):
        super().__init__()
        self._wrapped = wrapped
        self._domain = domain
        self._locale = locale

    def _db_get(self, msgid):
        row = (I18nMessage.query
               .filter_by(domain=self._domain, locale=self._locale, key=msgid)
               .first())
        return row.text if row else None

    def gettext(self, message):
        return self._db_get(message) or self._wrapped.gettext(message)

    def ngettext(self, singular, plural, n):
        key = plural if (n != 1) else singular
        hit = self._db_get(key)
        return hit if hit else self._wrapped.ngettext(singular, plural, n)


class DBDomain(Domain):
    def get_translations(self):
        wrapped = super().get_translations()
        locale = str(get_locale() or current_app.config.get("BABEL_DEFAULT_LOCALE", "en"))
        domain = self.domain
        return DBMergedTranslations(wrapped, domain=domain, locale=locale)


def init_i18n(app: Flask):
    app.jinja_env.globals.update(
        _=t,
        ngettext=tn
    )
