from pydantic import BaseModel

# Message class defined in Pydantic
class Book(BaseModel):
    bookName: str
    genre: str
    authorName: str

    def get_book_name(self):
        return self.bookName

    def get_author_name(self):
        return self.authorName

