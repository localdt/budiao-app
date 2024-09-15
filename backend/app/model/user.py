# Modelos SQLAlchemy
from sqlalchemy import Column, Integer, String
from ..utils.config import db

class User(db):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)