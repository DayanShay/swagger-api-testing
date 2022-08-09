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
            if not isinstance(collectionOfIsbns, list):
                raise TypeError("collectionOfIsbns must be list")
            for isnb in collectionOfIsbns:
                if not isinstance(isnb, CollectionOfIsbn):
                    raise TypeError("one or more values inside collectionOfIsbns is not instance of CollectionOfIsbn!")
            self._collectionOfIsbns = collectionOfIsbns
