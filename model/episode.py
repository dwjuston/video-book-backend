from __future__ import annotations

from pydantic import BaseModel
from model.media.root import MediaComponent
from model.media.type import MediaComponentType
from typing import Union

class EpisodeMetaData(BaseModel):
    start_time: int
    end_time: int
    description: str


class Episode(BaseModel):
    episode_id: str
    metadata: dict[str, EpisodeMetaData]
    data: dict[str, Union[list[MediaComponent], MediaComponent]]


if __name__ == "__main__":
    media_component_1 = MediaComponent(id="asd", type="image")
    media_metadata_1 = EpisodeMetaData(start_time=0, end_time=10, description="First image")
    media_component_2 = MediaComponent(id="qwe", type="text")
    media_metadata_2 = EpisodeMetaData(start_time=10, end_time=20, description="First text")
    episode = Episode(episode_id="123",
                      metadata={
                          media_component_1.id: media_metadata_1,
                          media_component_2.id: media_metadata_2},
                      data={
                          MediaComponentType.Image.name: [media_component_1],
                          MediaComponentType.Text.name: media_component_2})

    print(episode.json())