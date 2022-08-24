import json
import pytest
from Book_StoreApi.Bookstore_Api.BookstoreApi import Book_Store_Api
from Book_StoreApi.Bookstore_Api.BookstoreApi import AccountApi
from Book_StoreApi.Book_Models.replace_isbn import ReplaceIsbn
from Book_StoreApi.Book_Models.string_object import StringObject
from Book_StoreApi.Book_Models.getUserResult import UserResult
from Book_StoreApi.Book_Models.add_list_of_books import AddListOfBooks
from Book_StoreApi.Book_Models.collection_of_isbn import CollectionOfIsbn
import logging
import requests

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def bearer_auth_session(user_fix):
    headers = {'accept': 'application/json'}
    res = requests.post('https://bookstore.toolsqa.com/Account/v1/GenerateToken', data=user_fix, headers=headers)
    LOGGER.info(res.json())
    my_token = res.json()["token"]
    session = requests.session()
    session.headers.update({'Authorization': f'Bearer {my_token}'})
    session.headers.update(headers)
    return session


@pytest.fixture(scope="module")
def url(pytestconfig):
    url = pytestconfig.getoption("url")
    return url


@pytest.fixture(scope="module")
def bookStoreApi(url, bearer_auth_session):
    return Book_Store_Api(url, bearer_auth_session)


@pytest.fixture(scope="module")
def accountApi(url, bearer_auth_session):
    return AccountApi(url, bearer_auth_session)


@pytest.fixture(scope="module")
def user_fix():
    user = {
        "userName": "Yoss8ii1274",
        "password": "Aa123456!"
    }
    return user


@pytest.fixture(scope="module")
def get_data_from_json():
    with open("data.json", "r") as f:
        res_json_data = UserResult(**json.load(f))
    return res_json_data


@pytest.fixture(scope="module")
def post_account(user_fix, accountApi):
    code, outcome = accountApi.post_account(data=user_fix)
    LOGGER.info(outcome)
    if code == 201 and outcome.username == user_fix["userName"]:
        res_json = json.dumps(outcome.to_json(), indent=3)
        with open("data.json", "w") as f:
            f.write(res_json)
        return outcome


def test_authorized_user(user_fix, accountApi):
    code, outcome = accountApi.authorized_account(data=user_fix)
    LOGGER.info(outcome)
    assert code == 200 and outcome


def test_invalid_post_account(user_fix, accountApi):
    code, outcome = accountApi.post_account(data=user_fix)
    LOGGER.info(outcome)
    assert code == 406 and "User exists!" in outcome


def test_get_by_id(get_data_from_json, accountApi):
    code, outcome = accountApi.get_user_by_id(userId=get_data_from_json.userId)
    LOGGER.info(outcome)
    assert code == 200 and outcome.userId == get_data_from_json.userId


@pytest.fixture(scope="module")
def book_fix():
    book = {"isbn": "9781449325862"}
    return CollectionOfIsbn(**book)


@pytest.fixture(scope="module")
def book_fix2():
    book = {"isbn": "9781449331818"}
    return CollectionOfIsbn(**book)


@pytest.fixture(scope="module")
def book_list_fix(book_fix, book_fix2, get_data_from_json):
    isbn_collection = [book_fix, book_fix2]
    books_list = AddListOfBooks(userId=get_data_from_json.userId, collectionOfIsbns=isbn_collection)
    return books_list


@pytest.fixture(scope="module")
def store_user_fix():
    store_user_json = {
        "userId": "e7fa32a6-ce2c-43bd-a106-7c5031e3141e",
        "isbn": "9781449331818"
    }
    rep_sbn = ReplaceIsbn(**store_user_json)
    return rep_sbn


def test_get_books(bookStoreApi):
    code1, outcome = bookStoreApi.get_books()
    assert code1 == 200 and len(outcome) != 0


def test_post_books(book_list_fix, bookStoreApi):
    code, outcome = bookStoreApi.post_books(data=book_list_fix.to_json())
    LOGGER.info(outcome)
    assert code == 201 and book_list_fix == outcome


def test_delete_books(get_data_from_json, bookStoreApi):
    code, outcome = bookStoreApi.delete_books(userId=get_data_from_json.userId)
    LOGGER.info(outcome)
    assert code == 204


def test_get_book(book_fix, bookStoreApi):
    code, outcome = bookStoreApi.get_book(isbn=book_fix.isbn)
    assert code == 200 and outcome.isbn == book_fix.isbn


def test_delete_book(book_fix, bookStoreApi, get_data_from_json):
    str_obj = StringObject(isbn=book_fix.isbn, user_id=get_data_from_json.userId)
    code, outcome = bookStoreApi.delete_book(data=str_obj.to_json())
    LOGGER.info(outcome)
    assert code == 204


def test_put_books(book_fix2, store_user_fix, bookStoreApi):
    code, outcome = bookStoreApi.put_books(isbn=book_fix2.isbn, data=store_user_fix.to_json())
    LOGGER.info(outcome)
    assert code == 200


def test_delete_user(get_data_from_json, accountApi):
    code1, outcome1 = accountApi.delete_user(userId=get_data_from_json.userId)
    LOGGER.info(outcome1)
    assert code1 == 204
    code, outcome = accountApi.get_user_by_id(userId=get_data_from_json.userId)
    LOGGER.info(outcome)
    assert code == 401 and "User not found!" in outcome
