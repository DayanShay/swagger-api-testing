from BookStoreApi.Book_Models.baseObj import BaseObj


class ReplaceIsbn(BaseObj):
    def __init__(self, userId: str, isbn: str):
        self._userId = None
        self._isbn = None

        if userId is not None:
            if not isinstance(userId, str):
                raise TypeError("user id must be string")
            self._userId = userId

        if isbn is not None:
            if not isinstance(isbn, str):
                raise TypeError("isbn must be string")
            self._isbn = isbn

    @property
    def isbn(self):
        """Gets the isbn of this Model.
        :return: The isbn of this Model.
        :rtype: str
        """
        return self._isbn