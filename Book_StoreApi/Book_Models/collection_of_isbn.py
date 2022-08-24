from Book_StoreApi.Book_Models.baseObj import BaseObj


class CollectionOfIsbn(BaseObj):
    def __init__(self, isbn: str):
        super(BaseObj, self).__init__()
        if not str(isbn).isdigit():
            raise TypeError("isbn must be string")
        self._isbn = isbn

    @property
    def isbn(self):
        """Gets the isbn of this Model.
        :return: The isbn of this Model.
        :rtype: str
        """
        return self._isbn
