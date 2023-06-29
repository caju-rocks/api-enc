from flask import render_template, flash, redirect, url_for, request, jsonify
from sqlalchemy.exc import IntegrityError

from app import app, db
from app.models import Sector, ClimbRoutes


@app.route('/')
def index():
    return str(200)

@app.route('/sectors', methods=['POST'])
def create_sector():
    data = request.get_json()
    sector = Sector(
        name=data['name'], 
        city=data['city'], 
        state=data['state'], 
        description=data['description'],
        how_to_get_there=data['how_to_get_there'])
    db.session.add(sector)
    try:
        db.session.commit()
        return jsonify(sector.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'sector with same name already exists'}), 200


@app.route('/sectors', methods=['GET'])
def get_sector():
    sectors = Sector.query.all()
    return jsonify([sector.to_dict() for sector in sectors])

@app.route('/sectors/<int:sector_id>', methods=['PUT'])
def update_sector(sector_id):
    sector = Sector.query.get(sector_id)
    if sector:
        data = request.get_json()
        sector.name = data['name']
        sector.city = data['city']
        sector.state = data['state']
        sector.description = data['description']
        sector.how_to_get_there = data['how_to_get_there']
        db.session.commit()
        return jsonify(sector.to_dict())
    else:
        return jsonify({'error': 'sector not found'}), 404

@app.route('/climb-routes', methods=['POST'])
def create_climb_routes():
    data = request.get_json()
    sector = Sector.query.get(data['sector_id'])
    if sector:
        climb_route = ClimbRoutes(
            name=data['name'],
            grade=data['grade'],
            sector=sector)
        db.session.add(climb_route)
        db.session.commit()

        return jsonify(climb_route.to_dict()), 201
    else:
        return jsonify({'error': 'sector not found'}), 404

@app.route('/climb-routes', methods=['GET'])
def get_climb_routes():
    climb_routes = ClimbRoutes.query.all()
    return jsonify([cr.to_dict() for cr in climb_routes])

