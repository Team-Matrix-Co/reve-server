from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import auth, sale, aggregator, recommender

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Change this to specific domains that can make a request on the API
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return "Reve API"


# API Routes
app.include_router(auth.router)
app.include_router(sale.router)
app.include_router(aggregator.router)
app.include_router(recommender.router)
