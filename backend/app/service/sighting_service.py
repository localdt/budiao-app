 # Funções CRUD
from sqlalchemy.orm import Session
from ..model.sighting import Sighting
from ..model.file import File 
from ..schema.sighting_schema import SightingCreate, FileCreate, FileUpdate
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncSession

class SightingService:

    async def get_sighting_by_id(db: AsyncSession, sighting_id: int):
        result = await db.execute(select(Sighting).filter(Sighting.id == sighting_id))
        return result.scalars().first()

    async def get_sightings(db: AsyncSession, skip: int = 0, limit: int = 10):
        result = await db.execute(select(Sighting).offset(skip).limit(limit))
        return result.scalars().all()

    async def create_sighting(db: AsyncSession, sighting: SightingCreate):
        db_sighting = Sighting(latitude=sighting.latitude, longitude=sighting.longitude, status=sighting.status)
        db.add(db_sighting)
        await db.commit()
        await db.refresh(db_sighting)
        return db_sighting

    async def create_sighting_file(db: AsyncSession, file: FileCreate):
        db_file = File(name=file.name,path=file.path,status=file.status,sighting_id=file.sighting_id)
        db.add(db_file)
        await db.commit()
        await db.refresh(db_file)
        return db_file
    
    async def get_sightings_files(db: AsyncSession, skip: int = 0, limit: int = 10):
        result = await db.execute(select(File).offset(skip).limit(limit))
        return result.scalars().all()
    
    async def get_sightings_files_by_sighting_id(db: AsyncSession, sighting_id: int):
        result = await db.execute(select(File).filter(File.sighting_id == sighting_id))
        return result.scalars().all()
    
    async def get_file_by_id(db: AsyncSession, file_id: int):
        result = await db.execute(select(File).filter(File.id == file_id))
        return result.scalars().first()
    
    async def update_sighting_file(db: AsyncSession, sighting_file_id: int, file: FileUpdate):
        result = await db.execute(select(File).filter(File.id == sighting_file_id))
        db_sighting_file = result.scalars().first() 
        if db_sighting_file:
            db_sighting_file.status = file.status
            db_sighting_file.ml_class_result = file.ml_class_result
            await db.commit()
            await db.refresh(db_sighting_file)
            return db_sighting_file
        return None