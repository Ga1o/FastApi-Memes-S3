from pydantic import BaseModel


class MemeBase(BaseModel):
    title: str
    description: str
    image_url: str


class MemeCreate(MemeBase):
    pass


class MemeUpdate(MemeBase):
    pass


class Meme(MemeBase):
    id: int
