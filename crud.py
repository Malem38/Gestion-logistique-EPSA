from requests import delete
from sqlalchemy import delete, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import schemas, models


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


async def get_kit_by_id(db: AsyncSession, id_kit: int) -> models.Kit:
    result = await db.execute(select(models.Kit).where(models.Kit.id == id_kit))
    return result.scalars().first()
