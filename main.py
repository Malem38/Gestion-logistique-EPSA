from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

import crud, models, schemas
from database import SessionLocal, engine

from enum import Enum


class Tags(str, Enum):
    pieces = "Pieces"
    kits = "Kits"


app = FastAPI()

app.mount("/client", StaticFiles(directory="client"), name="client")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.get("/")
async def root():
    return RedirectResponse("client/index.html")


@app.get(
    "/piecesreelles",
    response_model=list[schemas.PiecesComplet],
    status_code=200,
    tags=[Tags.pieces],
)
async def get_piecesreelles(db: AsyncSession = Depends(get_db)):
    result = await crud.get_piecesreelles(db)
    return result


@app.post("/ajoutpiece", status_code=201, tags=[Tags.pieces])
async def ajout_piece(piece: schemas.PiecesReelles, db: AsyncSession = Depends(get_db)):
    piece_db = schemas.PiecesComplet(nombre_commande=0, nombre_reel=0, **piece.dict())
    await crud.ajout_piece(db, piece_db)


@app.get(
    "/kits", response_model=list[schemas.KitComplet], status_code=200, tags=[Tags.kits]
)
async def get_kits(db: AsyncSession = Depends(get_db)):
    result = await crud.get_kits(db)
    return result


@app.get(
    "/kits/{id_kit}",
    response_model=schemas.KitComplet,
    status_code=200,
    tags=[Tags.kits],
)
async def get_kit_by_id(id_kit: int, db: AsyncSession = Depends(get_db)):
    result = await crud.get_kit_by_id(db, id_kit)
    return result
