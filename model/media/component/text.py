from model.media.root import MediaComponent


class Text(MediaComponent):
    text: str
    type = "text"


if __name__ == '__main__':
    text = Text(id="asd", text="Hello, world!")
    print(text)
    print(text.json())