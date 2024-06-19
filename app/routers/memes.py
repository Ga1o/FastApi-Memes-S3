from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .. import crud, schemas
from ..models import get_db


router = APIRouter()


@router.get('/memes', response_model=List[schemas.Meme])
async def read_memes(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    memes = await crud.get_memes(db, skip=skip, limit=limit)
    return memes


@router.get('/memes/{meme_id}', response_model=schemas.Meme)
async def read_meme(meme_id: int, db: AsyncSession = Depends(get_db)):
    db_meme = await crud.get_meme(db, meme_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail='Meme not found')
    return db_meme


@router.post('/memes', response_model=schemas.Meme)
async def create_meme(meme: schemas.MemeCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_meme(db=db, meme=meme)


@router.put('/memes/{meme_id}', response_model=schemas.Meme)
async def update_meme(meme_id: int, meme: schemas.MemeUpdate, db: AsyncSession = Depends(get_db)):
    db_meme = await crud.update_meme(db=db, meme_id=meme_id, meme=meme)
    if db_meme is None:
        raise HTTPException(status_code=404, detail='Meme not found')
    return db_meme


@router.delete('/memes/{meme_id}', response_model=schemas.Meme)
async def delete_meme(meme_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud.delete_meme(db=db, meme_id=meme_id)
    if not success:
        raise HTTPException(status_code=404, detail='Meme not found')
    return {'message': 'Meme deleted'}
