import json
import requests
from BookStoreApi.Book_Models.getUserResult import UserResult
from BookStoreApi.Book_Models.bookModal import BookModel
from BookStoreApi.Book_Models.replace_isbn import ReplaceIsbn


class AccountApi:
    def __init__(self, url: str, session: requests):
        """
        contractor
        :param url: str: the swagger https link
        :param session: requests : the session requests and the from the tests
        """
        self._url = f"{url}Account/v1/"
        self._headers = {"accept": "application/json"}
        self._session = session
        self._session.headers.update(self._headers)

    def authorized_account(self, data) -> tuple[int, str]:
        """
        this fun gets data : User as json and returns tuple(status_code , str or json
        :param data: json: user account : name and password
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.post(url=f"{self._url}Authorized", data=data, headers=self._headers)
        if res1.status_code == 200:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def post_GenerateToken(self, data: json) -> tuple[int, str]:
        """
        fun generate token by user.
        :param data: json: user account
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.post(url=f"{self._url}GenerateToken", data=data, headers=self._headers)
        print(res1.json())
        my_token = res1.json()["token"]
        self._session.headers.update({'Authorization': f'Bearer {my_token}'})
        self._session.headers.update(self._headers)
        return res1

    def post_account(self, data: json) -> UserResult:
        """
        this fun gets account as json and post it to swagger
        :param data:
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.post(url=f"{self._url}User", data=data, headers=self._headers)
        if res1.status_code == 201:
            return res1.status_code, UserResult(**res1.json())
        return res1.status_code, res1.text

    def delete_user(self, userId: str) -> tuple[int, str ]:
        """
        this fun gets userid and send delete req to swagger
        :param userId: str: the userid id you want to delete
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.delete(url=f"{self._url}User/{userId}", headers=self._headers)
        if res1.status_code == 200:
            return res1.status_code, res1.text
        return res1.status_code, res1.text

    def get_user_by_id(self, userId: str) -> UserResult:
        """
        this function gets userid and bring back the account
        :param userId: str: the user id you want to find
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.get(url=f"{self._url}User/{userId}", headers=self._headers)
        if res1.status_code == 200:
            return res1.status_code, UserResult(**res1.json())
        return res1.status_code, res1.text


class Book_Store_Api:
    def __init__(self, url: str, session):
        """
        contractor
        :param url: str: the swagger https link
        :param session: requests : the session requests and the from the tests

        """
        self._url = f"{url}BookStore/v1/Book"
        self._headers = {"accept": "application/json"}
        self._session = session
        self._session.headers.update(self._headers)

    def get_books(self) -> tuple[int, str]:
        """
        this fun use a get req to swagger and ask to get all books
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.get(url=f"{self._url}s", headers=self._headers)
        if res1.status_code == 200:
            books_list = []
            for book in res1.json()["books"]:
                books_list.append(BookModel(**book))
            return res1.status_code, books_list
        return res1.status_code, res1.text

    def post_books(self, data) -> tuple[int, str ]:
        """
        this fun get book as json and sent a post req to swagger
        :param data: json : Book to Post
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.post(url=f"{self._url}s", data=data, headers=self._headers)
        if res1.status_code == 201:
            return res1.status_code, ReplaceIsbn(**res1.json())
        return res1.status_code, res1.text

    def delete_books(self, userId) -> tuple[int, str ]:
        """
        this fun get userid  as json and sent delete req  of all books to swagger
        :param userId: json: the user
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.delete(url=f"{self._url}s?UserId={userId}", headers=self._headers)
        if res1.status_code == 204:
            return res1.status_code, res1.text
        return res1.status_code, res1.text

    def get_book(self, isbn: json) -> BookModel:
        """
        this fun get isbn of a book  as json and sent get req  to swagger
        :param isbn: json the book id you want ot find
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.get(url=f"{self._url}?ISBN={isbn}", headers=self._headers)
        if res1.status_code == 200:
            return res1.status_code, BookModel(**res1.json())
        return res1.status_code, res1.text

    def delete_book(self, data) -> tuple[int, str]:
        """
        this fun get user as json and sent delete req of all  his books to swagger
        :param data: json: book you want to delete from swagger
        :return: tuple[int, str | json] status_code and the outcome(text or json) of the response
        """
        res1 = self._session.delete(url=f"{self._url}", data=data, headers=self._headers)
        if res1.status_code == 204:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def put_books(self, data:json, isbn:str) -> tuple[int, str]:
        """
        this function gets user as data and isbn of a book and put it in user books list
        :param data: json user account
        :param isbn:str: the id of the book you want to put at the user
        :return:
        """
        res1 = self._session.put(url=f"{self._url}s/{isbn}", data=data, headers=self._headers)
        if res1.status_code == 200:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text
