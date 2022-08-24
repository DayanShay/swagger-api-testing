from Book_StoreApi.Book_Models.baseObj import BaseObj


class StringObject(BaseObj):
    def __init__(self, isbn: str, user_id: str):
        super(BaseObj, self).__init__()
        self._isbn = None
        self._userId = None

        if isbn is not None:
            if not isinstance(isbn, str):
                raise TypeError("isbn must be string")
            self._isbn = isbn

        if user_id is not None:
            if not isinstance(user_id, str):
                raise TypeError(" userId must be string")
            self._userId = user_id
