from BookStoreApi.Book_Models.baseObj import BaseObj
from BookStoreApi.Book_Models.collection_of_isbn import CollectionOfIsbn


class AddListOfBooks(BaseObj):
    def __init__(self, userId: str, collectionOfIsbns: list):
        super(BaseObj, self).__init__()
        self._collectionOfIsbns = None
        if userId is not None:
            if not isinstance(userId, str):
                raise TypeError("user id must be string")
            self._userId = userId

        if collectionOfIsbns is not None:
            isbn_list = []
            for isnb in collectionOfIsbns:
                isbn_list.append(isnb)
            self._collectionOfIsbns = isbn_list
