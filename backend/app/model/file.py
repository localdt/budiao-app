# Modelos SQLAlchemy
from __future__ import annotations
from sqlalchemy import Column, Integer, String
from ..utils.config import db

from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship

class File(db):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    path = Column(String, index=True)
    
    sighting_id = Column(Integer, ForeignKey("sightings.id"))
    sightings = relationship("Sighting", back_populates="files")
