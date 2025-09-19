from app.extensions import db


class YourModel(db.Model):
    __tablename__ = 'your_table'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=db.func.now())

    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<YourModel %r>' % self.name
