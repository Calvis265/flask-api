from models import db
from .hero import Hero   

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete')
