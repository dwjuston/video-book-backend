from model.media.root import MediaComponent
from pydantic import AnyUrl


class Image(MediaComponent):
    image_url: AnyUrl
    type = "image"
