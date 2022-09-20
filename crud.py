from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func

import schemas
import models


async def get_piecesreelles(db: AsyncSession) -> list[models.PieceReelle]:
    result = await db.execute(select(models.PieceReelle))
    return result.scalars().all()


async def ajout_piece(db: AsyncSession, piece: schemas.PiecesReelles):
    db.add(models.PieceReelle(**piece.dict()))
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise ValueError("Erreur")


async def get_kits(db: AsyncSession) -> list[models.Kit]:
    result = await db.execute(select(models.Kit))
    return result.scalars().all()


async def get_kit_by_id(db: AsyncSession, id_kit: int) -> models.Kit | None:
    result = await db.execute(select(models.Kit).where(models.Kit.id == id_kit))
    return result.scalars().first()


async def add_kit(db: AsyncSession, kit: schemas.KitBase) -> models.Kit:
    recherche_id = await db.execute(
        select(func.max(models.Kit.id)).select_from(models.Kit)
    )
    id_max = recherche_id.scalars().first()
    if id_max is not None:
        id = id_max + 1
    else:
        id = 1
    kit_db = models.Kit(id=id, nb_pieces=0, **kit.dict())
    db.add(kit_db)
    try:
        await db.commit()
        return kit_db
    except IntegrityError:
        await db.rollback()
        raise ValueError("Erreur")


async def edit_kit(db: AsyncSession, kit: schemas.KitBase, id_kit: int):
    await db.execute(
        update(models.Kit).where(models.Kit.id == id_kit).values(**kit.dict())
    )
    await db.commit()

async def get_kit_pieces(db: AsyncSession, id_kit: int) -> list[models.PieceConception]:
    result = await db.execute(select(models.piece_conception).where(models.PieceConception.id_kit==id_kit))
    return result.scalars().all()