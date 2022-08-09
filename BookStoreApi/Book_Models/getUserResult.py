from BookStoreApi.Book_Models.baseObj import BaseObj


class UserResult(BaseObj):
    def __init__(self, userId: str, username: str, books: [str]):
        super(BaseObj, self).__init__()
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
