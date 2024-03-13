from model.media.root import MediaComponent
from pydantic import AnyUrl

class Narration(MediaComponent):
    audio_url: AnyUrl
    type = "narration"
