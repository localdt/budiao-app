# Ponto de entrada da aplicação
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import async_engine, Base
from .controller import users

app = FastAPI(
        title= "Budiao App",
        description= "Login Page",
        version= "1"
)

# Allow CORS for frontend
origins = [
    "http://localhost",
    "http://localhost:8000",
    # Add your front-end domain here
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
        await conn.run_sync(Base.metadata.create_all)
    
app.include_router(users.router)
