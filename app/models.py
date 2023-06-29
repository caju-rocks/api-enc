# from geoalchemy2 import Geometry

from sqlalchemy.dialects.postgresql import JSON
from app import db

class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    city = db.Column(db.String)
    state = db.Column(db.String)
    description = db.Column(db.Text)
    how_to_get_there = db.Column(db.Text)
    # geolocation = db.Column(Geometry('POINT', srid=4326))
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))

    def __init__(self, name, city, state, description, how_to_get_there):
        self.name = name
        self.city = city
        self.state = state
        self.description = description
        self.how_to_get_there = how_to_get_there

    def __repr__(self):
        return f"Sector(name='{self.name}', city='{self.city}', state='{self.state}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'description': self.description,
            'how_to_get_there': self.how_to_get_there
        }    

class ClimbRoutes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    grade = db.Column(JSON)
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'), nullable=False)

    sector = db.relationship('Sector', backref=db.backref('climb_routes', lazy=True))
    
    def __repr__(self):
        return f"ClimbRoute(name='{self.name}', sector='{self.sector.name}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sector_name': self.sector.name,
            'sector_city': self.sector.city
        }
