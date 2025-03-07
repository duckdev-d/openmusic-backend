from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import api
from app.core.db import set_db
from app.core.db import drop_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    set_db()
    yield
    drop_db()


app = FastAPI(lifespan=lifespan)

app.include_router(api)
