from ..extensions import db


class I18nMessage(db.Model):
    __tablename__ = "i18n_messages"
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(64), nullable=False, default="messages")
    locale = db.Column(db.String(16), nullable=False)
    key = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)

    __table_args__ = (db.UniqueConstraint("domain", "locale", "key"),)
