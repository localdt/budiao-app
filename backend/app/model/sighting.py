# Modelos SQLAlchemy
from __future__ import annotations
from sqlalchemy import Column, Integer, String
from ..utils.config import db
from typing import List
from ..model.file import File
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

class Sighting(db):
    __tablename__ = "sightings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    longitude = Column(Float)
    latitude = Column(Float)
    files = relationship("File")