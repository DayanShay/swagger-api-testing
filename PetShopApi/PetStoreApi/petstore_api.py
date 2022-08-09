import requests
from PetShopApi.Pet_Models.pet import Pet
from PetShopApi.Pet_Models.order import *
from PetShopApi.Pet_Models.tag import Tag
import json


class PetApi:
    def __init__(self, url: str):
        self._url = f"{url}/pet"
        self._headers = {"accept": "application/json"}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def put_pet(self, data: json):
        res = self._session.put(url=f"{self._url}", data=data, headers=self._headers)
        return res

    def post_pet(self, data: json):
        res = self._session.post(url=f"{self._url}", data=data, headers=self._headers)
        return res

    def findByStatus(self, status: json):
        res = self._session.get(url=f"{self._url}/findByStatus?status={status}", headers=self._headers)
        return res

    def findByTags(self, tags: json):
        res = self._session.get(url=f"{self._url}/findByTags?tags={tags}", headers=self._headers)
        return res

    def get_pet(self, id: int):
        res = self._session.get(url=f"{self._url}/{id}", headers=self._headers)
        return res

    def put_post_pet(self, id: int, name: str, status: str):
        res = self._session.post(url=f"{self._url}/{id}?name={name}&status={status}", headers=self._headers)
        return res

    def delete_pet(self, id: int):
        res = self._session.delete(url=f"{self._url}/{id}", headers=self._headers)
        return res

    def post_pet_uplaodImage(self, id: int, photo: str, additionalMetadata: str = 'null'):
        res = self._session.post(url=f"{self._url}/{id}/uploadImage?additionalMetadata={additionalMetadata}",
                                 data=photo, headers=self._headers)
        return res


class StoreApi:
    def __init__(self, url: str):
        self._url = f"{url}/store/"
        self._headers = {"accept": "application/json"}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def get_inventory(self) -> requests:
        res = self._session.get(url=f"{self._url}inventory", headers=self._headers)
        return res

    def post_order(self, data: json) -> requests:
        res = self._session.post(url=f"{self._url}order", json=data, headers=self._headers)
        return res

    def get_order(self, id: int) -> requests:
        res = self._session.get(url=f"{self._url}order/{id}", headers=self._headers)
        return res

    def delete_order(self, id: int) -> requests:
        res = self._session.delete(url=f"{self._url}order/{id}", headers=self._headers)
        return res


class UserApi:
    def __init__(self, url: str):
        self._url = f"{url}/user"
        self._headers = {"accept": "application/json"}
        self._session = requests.session()
        self._session.headers.update(self._headers)

    def post_user(self, data: json) -> requests:
        res = self._session.post(url=f"{self._url}", data=data, headers=self._headers)
        return res

    def post_users_with_list(self, data: json) -> requests:
        res = self._session.post(url=f"{self._url}/createWithList", data=data, headers=self._headers)
        return res

    def get_login(self, username:str, password:str) -> requests:
        res = self._session.get(url=f"{self._url}/login?username={username}&password={password}", headers=self._headers)
        return res

    def get_logout(self) -> requests:
        res = self._session.get(url=f"{self._url}/logout", headers=self._headers)
        return res

    def get_username(self, username: str) -> requests:
        res = self._session.get(url=f"{self._url}/{username}", headers=self._headers)
        return res

    def put_username(self, username: str, data: json) -> requests:
        res = self._session.put(url=f"{self._url}/{username}", data=data, headers=self._headers)
        return res

    def delete_username(self, username: str) -> requests:
        res = self._session.delete(url=f"{self._url}/{username}", headers=self._headers)
        return res
