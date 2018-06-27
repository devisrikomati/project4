import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

"""User information id, name ,email, 
   picture are stored in database
   Here id should be unique and name, 
   email not null values"""
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

"""Information about shoppingmall"""
class Shoppingmall(Base):
    __tablename__ = 'shoppingmall'
""" Taken class method to insert the data of shoppingmall"""
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

"""Information about clothes"""
class Cloth(Base):
    __tablename__ = 'cloth_details'
""" Taken class method"""
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    type = Column(String(250))
    shoppingmall_id = Column(Integer, ForeignKey('shoppingmall.id'))
    shoppingmall = relationship(Shoppingmall)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format
           Here serialize the data based on user_id and shoppingmall_id"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'price': self.price,
            'type': self.type,
            'shoppingmall_id': self.shoppingmall_id,
            'user_id':self.user_id
        }

"""database named as dresses"""
engine = create_engine('sqlite:///dresses.db')


Base.metadata.create_all(engine)
