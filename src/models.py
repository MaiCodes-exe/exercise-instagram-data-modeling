import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)



class User():
    _tablename__="User"
    id= Column(Integer, primary_key=True)
    name= Column(String(200))
    bio= Column(String(180))

class Post():
    _tablename__="Post"
    id= Column(Integer, primary_key=True)
    caption= Column(String(180))
    likes= column(Integer)

class LikedPosts():
    _tablename__="LikedPosts"
    id= Column(Integer, primary_key=True)

class Comments():
    _tablename__="Comments"
    id= Column(Integer, primary_key=True)



    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e