
# Ponto de entrada da aplicação
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .utils.config import async_engine, db
from .router import sighting, user, authentication

app = FastAPI(
        title= "Budiao App",
        description= "API - Budiao App system",
        version= "1"
)

# Allow CORS for frontend
origins = [
    "http://localhost",
    "http://localhost:8000",
    # Add your front-end domain here
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure the tables are created before the app starts
@app.on_event("startup")
async def startup():
    async with async_engine.begin() as conn:
        #await conn.run_sync(db.metadata.drop_all) # delete all tables
        await conn.run_sync(db.metadata.create_all)
    
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(sighting.router)