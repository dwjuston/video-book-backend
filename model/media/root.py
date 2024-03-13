from pydantic import BaseModel


class MediaComponent(BaseModel):
    id: str
    type: str