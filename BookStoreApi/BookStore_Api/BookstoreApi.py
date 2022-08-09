import json
import requests


class AccountApi:
    def __init__(self, url: str, session : requests):
        self._url = f"{url}Account/v1/"
        self._headers = {"accept": "application/json"}
        self._session = session
        self._session.headers.update(self._headers)

    def authorized_account(self, data: json) -> tuple[int, str | type(json)]:
        res1 = self._session.post(url=f"{self._url}Authorized", data=data, headers=self._headers)
        if res1.status_code == 200:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def post_GenerateToken(self, data: json) -> tuple[int, str | type(json)]:
        res1 = self._session.post(url=f"{self._url}GenerateToken", data=data, headers=self._headers)
        print(res1.json())
        my_token = res1.json()["token"]
        self._session.headers.update(self._headers)
        self._session.headers.update({'Authorization': f'Bearer {my_token}'})
        return res1

    def post_account(self, data: json) -> tuple[int, str | type(json)]:
        res1 = self._session.post(url=f"{self._url}User", data=data, headers=self._headers)
        if res1.status_code == 200:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def delete_user(self, userId: str) -> tuple[int, str | type(json)]:
        res1 = self._session.delete(url=f"{self._url}User/{userId}", headers=self._headers)
        if res1.status_code == 200:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def get_user_by_id(self, userId: str) -> tuple[int, str | type(json)]:
        res1 = self._session.get(url=f"{self._url}User/{userId}", headers=self._headers)
        if res1.status_code == 200:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text


class BookStoreApi:
    def __init__(self, url: str, session):
        self._url = f"{url}BookStore/v1/Books"
        self._headers = {"accept": "application/json"}
        self._session = session
        self._session.headers.update(self._headers)

    def get_books(self) -> tuple[int, str | type(json)]:
        res1 = self._session.get(url=f"{self._url}")
        if res1.status_code == 200:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def post_books(self, data) -> tuple[int, str | type(json)]:
        res1 = self._session.post(url=f"{self._url}", data=data)
        if res1.status_code == 201:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def delete_books(self, userId) -> tuple[int, str | type(json)]:
        res1 = self._session.delete(url=f"{self._url}?UserId={userId}")
        if res1.status_code == 204:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def get_book(self, isbn) -> tuple[int, str | type(json)]:
        res1 = self._session.get(url=f"{self._url}?ISBN={isbn}")
        if res1.status_code == 200:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def delete_book(self, data) -> tuple[int, str | type(json)]:
        res1 = self._session.delete(url=f"{self._url}", data=data)
        if res1.status_code == 204:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text

    def put_books(self, data, isbn) -> tuple[int, str | type(json)]:
        res1 = self._session.put(url=f"{self._url}/{isbn}", data=data)
        if res1.status_code == 200:
            return res1.status_code, res1.json()
        return res1.status_code, res1.text
