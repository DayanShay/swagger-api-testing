import pytest
from BookStoreApi.BookStore_Api.BookstoreApi import BookStoreApi
from BookStoreApi.BookStore_Api.BookstoreApi import AccountApi
from BookStoreApi.Book_Models.bookModal import BookModel
from BookStoreApi.Book_Models.replace_isbn import ReplaceIsbn
from BookStoreApi.Book_Models.string_object import StringObject
from BookStoreApi.Book_Models.getUserResult import UserResult
from BookStoreApi.Book_Models.add_list_of_books import AddListOfBooks
from BookStoreApi.Book_Models.collection_of_isbn import CollectionOfIsbn
import logging
import requests

LOGGER = logging.getLogger(__name__)

user_res_json = {
    "userId": "e097ff54-6b4e-4d13-b384-72dfe23c6391",
    "username": "Yossi1250",
    "books": []
}
user_res = UserResult(**user_res_json)


@pytest.fixture(scope="module")
def bearer_auth_session(user_fix):
    headers = {'accept': 'application/json'}
    res = requests.post('https://bookstore.toolsqa.com/Account/v1/GenerateToken', data=user_fix, headers=headers)
    my_token = res.json()["token"]
    session = requests.session()
    session.headers.update(headers)
    session.headers.update({'Authorization': f'Bearer {my_token}'})
    session.headers.update(headers)
    return session


@pytest.fixture(scope="module")
def url(pytestconfig):
    url = pytestconfig.getoption("url")
    return url


@pytest.fixture(scope="module")
def bookStoreApi(url, bearer_auth_session):
    return BookStoreApi(url, bearer_auth_session)


@pytest.fixture(scope="module")
def accountApi(url, bearer_auth_session):
    return AccountApi(url, bearer_auth_session)


@pytest.fixture(scope="module")
def user_fix():
    user = {
        "userName": "Yossi1250",
        "password": "Aa123456!"
    }
    return user


def test_post_account(user_fix, accountApi):
    code, outcome = accountApi.post_account(data=user_fix)
    LOGGER.info(outcome)
    assert code == 406 and "User exists!" in outcome


def test_authorized_user(user_fix, accountApi):
    code, outcome = accountApi.authorized_account(data=user_fix)
    LOGGER.info(outcome)
    assert code == 200 and outcome == True


def test_get_by_id(user_fix, accountApi):
    code, outcome = accountApi.get_user_by_id(userId=user_res.userId)
    LOGGER.info(outcome)
    assert code == 200


@pytest.fixture(scope="module")
def book_fix():
    book = BookModel(isbn="1250", title="Dayan King", pages=125)
    return book


def book_fix2():
    book = BookModel(isbn="1251", title="Dayan King2", pages=125)
    return book


@pytest.fixture(scope="module")
def book_list_fix(book_fix, book_fix2):
    isbn_collection = [CollectionOfIsbn(book_fix.isbn), CollectionOfIsbn(book_fix2.isbn)]
    books_list = AddListOfBooks(userId=user_res.userId, collectionOfIsbns=isbn_collection)
    return books_list


@pytest.fixture(scope="module")
def store_user_fix():
    store_user_json = {
        "userId": "e097ff54-6b4e-4d13-b384-72dfe23c6391",
        "isbn": "1250"
    }
    rep_sbn = ReplaceIsbn(**store_user_json)
    return rep_sbn


def test_get_books(bookStoreApi):
    code1, outcome1 = bookStoreApi.get_books()
    list1 = [BookModel(**a) for a in outcome1["books"]]
    LOGGER.info(f"test get books {list1[0:1:1]}")
    assert code1 == 200


def test_post_books(book_list_fix, bookStoreApi):
    code, outcome = bookStoreApi.post_books(data=book_list_fix.to_json())
    LOGGER.info(outcome)
    assert code == 201 and book_list_fix.to_json()["collectionOfIsbns"] == outcome["books"]


def test_delete_books(bookStoreApi):
    code, outcome = bookStoreApi.delete_books(userId=user_res.to_json()["userId"])
    LOGGER.info(outcome)
    assert code == 204


def test_get_book(book_fix, bookStoreApi):
    code, outcome = bookStoreApi.get_book(isbn=book_fix.isbn)
    book_test = []
    for a in outcome["books"]:
        book_test.append(BookModel(**a))
    print(book_test)
    LOGGER.info(outcome)
    assert code == 200 and len(book_test) > 0


def test_delete_book(book_fix, bookStoreApi):
    str_obj = StringObject(isbn=book_fix.isbn, user_id=user_res.userId)
    code, outcome = bookStoreApi.delete_book(data=str_obj.to_json())
    LOGGER.info(outcome)
    assert code == 204


def test_put_books(store_user_fix, bookStoreApi):
    code, outcome = bookStoreApi.put_books(isbn=store_user_fix.isbn, data=store_user_fix.to_json())
    LOGGER.info(outcome)
    assert code == 200


def test_delete_user(user_fix, accountApi):
    code1, outcome1 = accountApi.delete_user(userId=user_res.userId)
    LOGGER.info(outcome1)
    assert code1 == 200
    code2, outcome2 = accountApi.get_user_by_id(userId=user_res.userId)
    LOGGER.info(outcome2)
    assert code2 == 200
