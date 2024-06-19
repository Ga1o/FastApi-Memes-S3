import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to Meme API'}


@pytest.mark.asyncio
async def test_read_memes():
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get('/memes')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'title' in data[0]
    assert 'description' in data[0]
    assert 'image_url' in data[0]


@pytest.mark.asyncio
async def test_read_meme():
    meme_id = 1
    async with AsyncClient(app=app, base_url='http://test') as ac:
        response = await ac.get(f'/memes/{meme_id}')
    assert response.status_code == 200
    data = response.json()
    assert 'title' in data
    assert 'description' in data
    assert 'image_url' in data
