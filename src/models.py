import os
import sys
import sqlalchemy
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



class User(Base):
    __tablename__= "user"
    id= Column(Integer, primary_key=True)
    name= Column(String(20))
    password = Column(String(50))  
    bio= Column(String(180))

class Posts(Base):
    __tablename__= "posts"
    id= Column(Integer, primary_key=True)
    caption= Column(String(180))
    likes= Column(Integer)

class LikedPosts(Base):
    __tablename__= "likedposts"
    id= Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    posts_id= Column(Integer, ForeignKey('posts.id'))
    LikedPosts = relationship(user_id)

class Comments(Base):
    __tablename__= "comments"
    id= Column(Integer, primary_key=True)
    comment= Column(String(200))
    user_id= Column(Integer, ForeignKey('user.id'))
    posts_id= Column(Integer, ForeignKey('posts.id'))
    Comments = relationship(posts_id)


    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e