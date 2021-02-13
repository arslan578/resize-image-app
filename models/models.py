from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ResizeImagesCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.TEXT)
    count = db.Column(db.Integer, default=0)
