from fastapi import FastAPI
from .routers import memes


app = FastAPI()
app.include_router(memes.router)


@app.get('/')
async def read_root():
    return {'message': 'Welcome to Meme API'}
