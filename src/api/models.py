from flask_sqlalchemy import SQLAlchemy
import os
import sys
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    person_favorites = db.relationship('FavoritePerson', backref='User', lazy=True)
    planet_favorites = db.relationship('FavoritePlanet', backref='User', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(64))
    gravity = db.Column(db.String(64))
    terrain = db.Column(db.String(64))
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)
    films = ""
    created = db.Column(db.DateTime, default=datetime.now)
    edited = db.Column(db.DateTime, default=None, onupdate=datetime.now)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    planet_favorites = db.relationship('FavoritePlanet', backref='Planets', lazy=True)



class Person(db.Model):
    # __tablename__ = 'person'
    # Here we define columns for the table person
    id = db.Column(db.Integer, primary_key=True)
    #These are all the properties of people in the SW universe
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.Integer)
    is_bby = db.Column(db.Boolean)
    eye_color = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    hair_color = db.Column(db.String(64))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    skin_color = db.Column(db.String(64))
    vehicles = db.relationship("Vehicles")
    planets = db.relationship("Planets")
    person_favorites = db.relationship('FavoritePerson', backref='Person', lazy=True)


    #These are things that people are related to (other than people)
    starships = db.relationship("Starships")

    #This is just letting us know that things have changed.
    created = db.Column(db.DateTime, default=datetime.now)
    edited = db.Column(db.DateTime, default=None, onupdate=datetime.now)

    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "is_bby": self.is_bby,
            "vehicles": self.vehicles,
            "starships": self.starships,
            "planets": self.planets,
            "favorites_id": self.favorites_id           

            # do not serialize the password, its a security breach
        }


class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    model = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(64))
    vehicle_class = db.Column(db.String(64))
    pilots = db.Column(db.Integer, db.ForeignKey("person.id"))
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))
    created = db.Column(db.DateTime, default=datetime.now)
    edited = db.Column(db.DateTime, default=None, onupdate=datetime.now)

class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    model = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(64))
    hyperdrive_rating = db.Column(db.Integer)
    MGLT = db.Column(db.Integer)
    starship_class = db.Column(db.String(64))
    created = db.Column(db.DateTime, default=datetime.now)
    edited = db.Column(db.DateTime, default=None, onupdate=datetime.now)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))

class FavoritePerson(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __repr__(self):
        return '<FavoritePerson %r>' % self.user_id

    def serialize(self):
        user = User.query.get(self.user_id)
        return {
            "user": user.username,
            "person_id": self.person_id,
        }

class FavoritePlanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))        

    def __repr__(self):
        return '<FavoritePlanet %r>' % self.user_id

    def serialize(self):
        user = User.query.get(self.user_id)
        return {
            "id": self.id,
            "user": user.username,
            "planet_id": self.planet_id,
        }
