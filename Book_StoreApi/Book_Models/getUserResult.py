from Book_StoreApi.Book_Models.baseObj import BaseObj


class UserResult(BaseObj):
    def __init__(self, username: str, books: [str],userID = None, userId= None):
        super(BaseObj, self).__init__()
        if userID and not userId:
            self._userId = userID
        else:
            self._userId = userId
        self._username = username
        self._books = books

    @property
    def userId(self) -> str:
        return self._userId

    @property
    def username(self) -> str:
        return self._username

    @property
    def books(self) -> [str]:
        return self._books
