"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint

from api.models import db, User, Person, Planets, Vehicles, Starships, FavoritePlanet, FavoritePerson
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def Index():
    response_body = {
        "message": "Welcome to the Star Wars REST API"
    }

@api.route('/people', methods=['GET'])
def get_people():
    req_people = Person.query.all()
    peoples = [people.serialize() for people in req_people]
    return jsonify(peoples), 200

@api.route('/people/<int:people_id>', methods=['GET'])
def get_person():
    person = People.query.filter_by(id=people_id).first()
    return jsonify(person.serialize())

@api.route('/planets', methods=['GET'])
def get_planets():
    req_planets = Planets.query.all()
    return jsonify(planets = [planets.serialize() for planet in req_planets]), 200

@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet():
    planet = Planets.query.filter_by(id=planets_id).first()
    return jsonify(planet.serialize())

@api.route('/starships', methods=['GET'])
def get_starships():
    req_starships = Starships.query.all()
    return jsonify(starships = [starships.serialize() for starship in req_starships]), 200

@api.route('/starships/<int:starship_id>', methods=['GET'])
def get_starship():
    starship = Starships.query.filter_by(id=starships_id).first()
    return jsonify(starship.serialize())

@api.route('/vehicles', methods=['GET'])
def get_vehicles():
    req_vehicles = Vehicles.query.all()
    return jsonify(vehicles = [vehicles.serialize() for vehicle in req_vehicles]), 200

@api.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def get_vehicle():
    vehicle = Vehicles.query.filter_by(id=vehicles_id).first()
    return jsonify(vehicle.serialize())

@api.route('/user/favorites', methods=['GET'])
def get_user_favorites():
    favoriteplanet = FavoritePlanet.query.all()
    favoriteperson = FavoritePerson.query.all()
    all_favorite_person = [favPerson.serialize() for favPerson in favoriteperson]
    all_favorite_planet = [favPlanet.serialize() for favPlanet in favoriteplanet]
    return jsonify(all_favorite_planet+all_favorite_person), 200

@api.route('/favorite/planet/<int:planet_id>', methods=["POST"])
def add_favorite_planet(planet_id):
    request_body = request.get_json()
    user_id = request_body["user_id"]
    new_favorite = FavoritePlanet(user_id = user_id, planets_id = planet_id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify("Favorite planet has been added."), 200

@api.route('/favorite/person/<int:person_id>', methods=["POST"])
def add_favorite_person(person_id):
    request_body = request.get_json()
    user_id = request_body["user_id"]
    new_favorite = FavoritePerson(user_id = user_id, person_id = person_id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify("Favorite person has been added."), 200

@api.route('/favorite/planet/<int:planet_id>', methods=["DELETE"])
def delete_favorite_planet(planet_id):
    request_body = request.get_json()
    user_id = request_body["user_id"]
    my_favorite = FavoritePlanet.query.filter_by(user_id = user_id, planets_id = planet_id).first()
    if my_favorite is not None:
        db.session.delete(my_favorite)
        db.session.commit()
        return jsonify("Favorite planet has been deleted."), 200
    return jsonify("Favorite planet not found."), 400

@api.route('/favorite/person/<int:person_id>', methods=["DELETE"])
def delete_favorite_person(person_id):
    request_body = request.get_json()
    user_id = request_body["user_id"]
    my_favorite = FavoritePerson.query.filter_by(user_id = user_id, person_id = person_id).first()
    if my_favorite is not None:
        db.session.delete(my_favorite)
        db.session.commit()
        return jsonify("Favorite person has been deleted."), 200
    return jsonify("Favorite person not found."), 400