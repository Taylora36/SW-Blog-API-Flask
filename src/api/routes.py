"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint

from api.models import db, User, Person, Planets, Vehicles, Starships
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def Index():
    response_body = {
        "message": "Welcome to the Star Wars REST API"
    }

@api.route('https://swapi.dev/api/people', methods=['GET'])
def get_people():
    req_people = People.query.all()
    return jsonify(peoples = [people.serialize() for people in req_people]), 200

@api.route('https://swapi.dev/api/people/<int:people_id>', methods=['GET'])
def get_person():
    person = People.query.filter_by(id=people_id).first()
    return jsonify(person.serialize())

@api.route('https://swapi.dev/api/planets', methods=['GET'])
def get_planets():
    req_planets = Planets.query.all()
    return jsonify(planets = [planets.serialize() for planet in req_planets]), 200

@api.route('https://swapi.dev/api/planets/<int:planet_id>', methods=['GET'])
def get_planet():
    planet = Planets.query.filter_by(id=planets_id).first()
    return jsonify(planet.serialize())

@api.route('https://swapi.dev/api/starships', methods=['GET'])
def get_starships():
    req_starships = Starships.query.all()
    return jsonify(starships = [starships.serialize() for starship in req_starships]), 200

@api.route('https://swapi.dev/api/starships/<int:starship_id>', methods=['GET'])
def get_starship():
    starship = Starships.query.filter_by(id=starships_id).first()
    return jsonify(starship.serialize())

@api.route('https://swapi.dev/api/vehicles', methods=['GET'])
def get_vehicles():
    req_vehicles = Vehicles.query.all()
    return jsonify(vehicles = [vehicles.serialize() for vehicle in req_vehicles]), 200

@api.route('https://swapi.dev/api/vehicles/<int:vehicles_id>', methods=['GET'])
def get_vehicle():
    vehicle = Vehicles.query.filter_by(id=vehicles_id).first()
    return jsonify(vehicle.serialize())
