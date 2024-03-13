from model.media.root import MediaComponent
from pydantic import AnyUrl


class BackgroundMusic(MediaComponent):
    music_url: AnyUrl
    type = "bgm"
