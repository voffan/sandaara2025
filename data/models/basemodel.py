from data.database import db


class BaseModel(db.Model):
    __abstract__ = True  # mark this as an abstract base class
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)