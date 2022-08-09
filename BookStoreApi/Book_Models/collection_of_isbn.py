from BookStoreApi.Book_Models.baseObj import BaseObj


class CollectionOfIsbn(BaseObj):
    def __init__(self, isbn: str):
        super(BaseObj, self).__init__()
        if not isinstance(isbn, str):
            raise TypeError("isbn must be string")
        self._isbn = isbn
