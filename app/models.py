# from geoalchemy2 import Geometry
import uuid

from sqlalchemy.dialects.postgresql import JSON
from app import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()), unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    auth_user_id = db.Column(db.String)
    auth_user = db.relationship('Users', backref=('auth.users'), primaryjoin='foreign(Users.auth_user_id) == remote(Users.id)')

class Sectors(db.Model):
    __tablename__ = 'sectors'
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()), unique=True)
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
    __tablename__ = 'climb_routes'
    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()), unique=True)
    name = db.Column(db.String)
    grade = db.Column(JSON)
    sector_id = db.Column(db.String, db.ForeignKey('sectors.id'), nullable=False)

    sector = db.relationship('Sectors', backref=db.backref('climb_routes', lazy=True))
    
    def __repr__(self):
        return f"ClimbRoute(name='{self.name}', sector='{self.sector.name}')"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'sector_name': self.sector.name,
            'sector_city': self.sector.city
        }
