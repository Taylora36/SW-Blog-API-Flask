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
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))

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
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))



class Person(db.Model):
    __tablename__ = 'person'
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
    favorites_id = db.Column(db.Integer, db.ForeignKey("favorites.id"))


    #These are things that people are related to (other than people)
    starships = db.relationship("Starships")

    #This is just letting us know that things have changed.
    created = db.Column(db.DateTime, default=datetime.now)
    edited = db.Column(db.DateTime, default=None, onupdate=datetime.now)



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

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    person = db.relationship("Person")
    planets = db.relationship("Planets")
    vehicles = db.relationship("Vehicles")
    starships = db.relationship("Starships")
    user = db.relationship("User")

