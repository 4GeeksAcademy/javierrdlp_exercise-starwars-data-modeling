import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique = True)
    password = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    subscription_date = Column(String(50)) 

class FavoriteCharacters(Base):
    __tablename__= 'favorite_characters'
    id = Column(Integer, primary_key=True)    
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)    

class Characters(Base):
    __tablename__= 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique = True)
    gender = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)

    planet_id = Column(Integer, ForeignKey('planets.id'))
    starship_id = Column(Integer, ForeignKey('starships.id'))

    planet = relationship('Planets', back_populates='characters')
    starship = relationship('Starships', back_populates='characters')

class Planets(Base):
    __tablename__= 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique = True)
    climate = Column(String(250), nullable=False)    
    population = Column(Integer)

    characters = relationship('Characters', back_populates='planet')
    
    
class Starships(Base):
    __tablename__= 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique = True)
    passengers = Column(Integer)    
    lenght = Column(Integer)

    characters = relationship('Characters', back_populates='starship')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
