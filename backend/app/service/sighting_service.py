 # Funções CRUD
from sqlalchemy.orm import Session
from ..model.sighting import Sighting
from ..schema.sighting_schema import SightingCreate
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.asyncio import AsyncSession

class SightingService:

    async def get_sighting_by_id(db: AsyncSession, sighting_id: int):
        result = await db.execute(select(Sighting).filter(Sighting.id == sighting_id))
        return result.scalars().first()

    async def get_sightings(db: AsyncSession, skip: int = 0, limit: int = 10):
        result = await db.execute(select(Sighting).offset(skip).limit(limit))
        return result.scalars().all()

    async def create_sighting(db: AsyncSession, sighting: SightingCreate):
        db_sighting = Sighting(latitude=sighting.latitude, longitude=sighting.longitude)
        db.add(db_sighting)
        await db.commit()
        await db.refresh(db_sighting)
        return db_sighting
