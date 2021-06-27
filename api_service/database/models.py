from api_service.database import db
from datetime import datetime


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(80), unique=True, nullable=False)
    media_type = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow,
                           nullable=False)
    update_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns
                if getattr(self, c.name) is not None}

    def __repr__(self):
        return f"{self.file_name}"
