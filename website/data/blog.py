from . import cloudinary
from .user import User
from shared.data import DB, commit
from sqlalchemy.ext.hybrid import hybrid_property


class Blog(DB.Model):
    __tablename__ = 'blog'
    id = DB.Column(DB.Integer, primary_key=True)

    headline = DB.Column(DB.String(64), nullable=False)
    image_id = DB.Column(DB.String(64), nullable=False)
    summary = DB.Column(DB.Text, nullable=False)
    content = DB.Column(DB.Text, nullable=False)

    author = DB.Column(DB.String(96), nullable=False)
    timestamp = DB.Column(DB.DateTime, server_default=DB.func.current_timestamp())
    edited = DB.Column(DB.Boolean, default=False)

    comments = DB.relationship('Comment', backref='blog', cascade='all, delete-orphan')

    @hybrid_property
    def image_url(self) -> str | None:
        return cloudinary.retrieve_asset_url(self.image_id)

    @hybrid_property
    def info(self) -> str:
        user = User.query.filter_by(username=self.author).first()
        author = f"{user.first_name} {user.last_name if not user.hide_last_name else ''}".strip()
        timestamp = self.timestamp.strftime("%d.%m.%Y %H:%M")
        edited = ' (bearbeitet)' if self.edited else ''
        return f"{author}, {timestamp}{edited}"

    def __init__(self, headline: str, image_id: str, summary: str, content: str, author: str):
        self.headline = headline
        self.image_id = image_id
        self.summary = summary
        self.content = content
        self.author = author

    def update_data(self, new_headline: str | None, new_summary: str | None, new_content: str | None) -> None:
        if new_headline:
            self.headline = new_headline
        if new_summary:
            self.summary = new_summary
        if new_content:
            self.content = new_content
        self.edited = True
        commit()
