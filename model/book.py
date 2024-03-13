from pydantic import BaseModel
from typing import Union

class TableOfContent(BaseModel):
    __root__: list[dict[str, Union[str, str]]]


class BookMetaData(BaseModel):
    id: str
    title: str
    author: str


class Book(BaseModel):
    metadata: BookMetaData
    toc: TableOfContent


if __name__ == "__main__":
    dict_bookmeta = {
        "id": "AAAA",
        "title": "book1",
        "author": "author1"
    }

    dict_toc = [
        {
            "chapter_id": "asd1",
            "chapter_name": "chapter1",
            "episode_id": "qwe",
            "episode_name": "episode1"
        },
        {
            "chapter_id": "asd1",
            "chapter_name": "chapter1",
            "episode_id": "rty",
            "episode_name": "episode2"
        },
        {
            "chapter_id": "asd2",
            "chapter_name": "chapter2",
            "episode_id": "zxc",
            "episode_name": "episode3"
        }
    ]

    # convert df into BookMetaData's toc
    book_meta_data = Book(
        metadata=dict_bookmeta,
        toc=dict_toc
    )

    print(book_meta_data.json())