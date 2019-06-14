import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random
import string
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)


secret_key = "test"
Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)

    def hash_password(self, pw):
        self.password = pwd_context.encrypt(pw)

    def verify_password(self, pw):
        return pwd_context.verify(pw, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'id': self.id, 'name': self.name})


class Item(Base):
    __tablename__ = 'Items'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category = Column(String(40))

    owner = Column(String(100), ForeignKey('User.id'))
    User = relationship(User)

# send JSON objects in a serializable format
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'category': self.category,
            'owner': self.owner,
                }


@staticmethod
def verify_auth_token(token):
    s = Serializer(secret_key)
    try:
        data = s.loads(token)
    except SignatureExpired:
        # Valid Token, but expired
        return None
    except BadSignature:
        # Invalid Token
        return None
    user_id = data['id']
    return user_id


engine = create_engine('sqlite:///CatalogWithUsers.db')

Base.metadata.create_all(engine)
