import pytest
import logging
from PetShopApi.Pet_Models.user import User
from PetShopApi.Pet_Models.pet import Pet
from PetShopApi.Pet_Models.order import *
from PetShopApi.Pet_Models.tag import Tag
from PetShopApi.Pet_Models.petStatus import petStatus
from PetShopApi.Pet_Models.category import Category
from PetShopApi.PetStoreApi import petstore_api as Api
import json

LOGGER = logging.getLogger(__name__)


@pytest.fixture
def url(pytestconfig):
    url = pytestconfig.getoption("url")
    return url


@pytest.fixture
def pet_Api(url):
    return Api.PetApi(url)


@pytest.fixture
def store_Api(url):
    return Api.StoreApi(url)


@pytest.fixture
def user_Api(url):
    return Api.UserApi(url)


@pytest.fixture(scope="session")
def Pet_fix() -> Pet:
    cat = {
        "id": 1250,
        "name": "Danny",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    return Pet(**cat)


@pytest.fixture(scope="session")
def test_status() -> petStatus:
    status = petStatus.available.value
    return status


def test_put_pet(Pet_fix, pet_Api):
    LOGGER.info("Start tests on PetApi")
    res_status, res_put_pet = pet_Api.post_pet(Pet_fix.to_json())
    assert res_status == 200 and res_put_pet.id == Pet_fix.id
    Pet_fix2 = Pet_fix
    Pet_fix2.name = "Yossy"
    res_status, pet_res = pet_Api.put_pet(Pet_fix2.to_json())
    assert res_status == 200 and pet_res.name == Pet_fix2.name


def test_post_pet(Pet_fix, pet_Api):
    res_status, res_post_pet = pet_Api.post_pet(Pet_fix.to_json())
    assert res_status == 200 and res_post_pet.id == Pet_fix.id


def test_find_by_status(test_status, Pet_fix, pet_Api):
    Pet_fix.status = test_status
    res_code, res_post_pet = pet_Api.post_pet(Pet_fix.to_json())
    assert res_code == 200 and res_post_pet.id == Pet_fix.id
    res_code, res_list_pet = pet_Api.findByStatus(test_status)
    assert res_code == 200
    for pets in res_list_pet:
        assert test_status == pets.status


def test_find_by_tag(Pet_fix, pet_Api):
    res_status, res_put_pet = pet_Api.post_pet(Pet_fix.to_json())
    assert res_status == 200 and res_put_pet.id == Pet_fix.id
    res_get_tags, res_list_pet = pet_Api.findByTags("tag1")
    assert res_get_tags == 200
    for tags in res_list_pet:
        assert Pet_fix.tags[0] == tags.tags[0]


def test_get_pet_by_id(Pet_fix, pet_Api):
    res_status, res_post_pet = pet_Api.post_pet(Pet_fix.to_json())
    assert res_status == 200 and res_post_pet.id == Pet_fix.id
    res_code, res_get_id = pet_Api.get_pet(Pet_fix.id)
    assert res_code == 200 and res_get_id.id == Pet_fix.id


def test_update_name_or_status_by_id(test_status, Pet_fix, pet_Api):
    res_status, res_post_pet = pet_Api.post_pet(Pet_fix.to_json())
    assert res_status == 200 and res_post_pet.id == Pet_fix.id
    res_status, res_post_pet = pet_Api.put_post_pet(id=Pet_fix.id, name="Danny", status=test_status)
    Pet_fix2 = Pet_fix
    Pet_fix2.name = "Danny"
    Pet_fix2.status = "available"
    assert res_status == 200 and res_post_pet.id == Pet_fix2.id and res_post_pet.name == \
           Pet_fix2.name and res_post_pet.status == Pet_fix2.status


def test_delete_by_id(Pet_fix, pet_Api):
    res_status, res_post_pet = pet_Api.post_pet(Pet_fix.to_json())
    assert res_status == 200 and res_post_pet.id == Pet_fix.id
    res_code, res_get_id = pet_Api.get_pet(Pet_fix.id)
    assert res_code == 200 and res_get_id.id == Pet_fix.id
    res_code, res_text = pet_Api.delete_pet(Pet_fix.id)
    assert res_code == 200 and res_text == "Pet deleted"
    res_code, res_get_id = pet_Api.get_pet(Pet_fix.id)
    assert res_code == 404 and res_get_id == "Pet not found"
    LOGGER.info("Finish tests on PetApi")


def test_upload_image(Pet_fix, pet_Api):
    res_status, res_post_pet = pet_Api.post_pet(Pet_fix.to_json())
    assert res_status == 200 and res_post_pet.id == Pet_fix.id
    image = '186462.jpg'
    res_img, pet_img = pet_Api.post_pet_uplaodImage(id=Pet_fix.id, photo=image)
    assert res_img == 200 and pet_img == Pet_fix.photo_Urls


@pytest.fixture(scope="session")
def order_fix():
    order = {
        "id": 1200,
        "petId": 1250,
        "quantity": 7,
        "status": "approved",
        "complete": True
    }
    return Order(**order)


def test_get_inventory(order_fix: Order, store_Api):
    res1_code, res1_order = store_Api.get_inventory()
    LOGGER.info(res1_order)
    assert res1_code == 200
    order = order_fix
    res2_code, res2_order = store_Api.post_order(order.to_json())
    assert res2_code == 200 and order_fix.id == res2_order.id
    res3_code, res3_order = store_Api.get_inventory()
    assert res3_code == 200 and res3_order["approved"] != res1_order["approved"]


def test_post_order(order_fix: Order, store_Api):
    res1_code, res_order = store_Api.post_order(order_fix.to_json())
    assert res1_code == 200 and order_fix.id == res_order.id
    res2_code, res2_order = store_Api.get_order(order_fix.id)
    assert res2_code == 200 and order_fix.id == res2_order.id


def test_get_order_by_id(order_fix: Order, store_Api):
    res1_code, res_order = store_Api.post_order(order_fix.to_json())
    assert res1_code == 200 and order_fix.id == res_order.id
    res2_code, res2_order = store_Api.get_order(order_fix.id)
    assert res2_code == 200 and order_fix.id == res2_order.id


def test_delete_order(order_fix: Order, store_Api):
    res1_code, res_order = store_Api.post_order(order_fix.to_json())
    assert res1_code == 200 and order_fix.id == res_order.id

    res1_code, res1_order = store_Api.get_order(order_fix.id)
    assert res1_code == 200 and order_fix.id == res1_order.id

    res3_code, res_text = store_Api.delete_order(order_fix.id)
    res4_code, res4_order = store_Api.get_order(order_fix.id)

    assert res3_code == 200 and res4_code == 404


@pytest.fixture(scope="session")
def user_fix1() -> User:
    user = User(id=1250, username="user1250", userStatus=1, password="123456")
    return user


@pytest.fixture(scope="session")
def user_fix2() -> User:
    user = User(id=1251, username="user1251", userStatus=1, password="123456")
    return user


@pytest.fixture(scope="session")
def user_fix3() -> User:
    user = User(id=1252, username="user1250", userStatus=1, password="123456")
    return user


def test_post_user(user_fix1: User, user_Api):
    res1_code,res1_user = user_Api.post_user(data=user_fix1.to_json())
    assert res1_code == 200 and user_fix1.id == res1_user.id


def test_login(user_fix1: User, user_Api):
    res1_code, res1_user = user_Api.get_login(username=user_fix1.username, password=user_fix1.password)
    LOGGER.info(res1_user)
    assert res1_code == 200


def test_get_user(user_fix1: User, user_Api):
    res1_code, res_user = user_Api.get_username(username=user_fix1.to_json()["username"])
    assert res1_code == 200 and user_fix1.username == res_user.username


def test_post_user_with_list(user_fix1: User, user_fix2: User, user_Api):
    temp_users_list = [user_fix1.to_json(), user_fix2.to_json()]
    data = json.dumps(temp_users_list)
    res_code,res_user_list = user_Api.post_users_with_list(data=data)
    assert res_code == 200 and data == res_user_list


def test_logout(user_Api):
    res1 = user_Api.get_logout()
    LOGGER.info(res1.text)
    assert res1.status_code == 200


def test_put_username(user_fix1:User,user_fix3: User, user_Api):
    res1_code,res1_user = user_Api.post_user(data=user_fix1.to_json())
    assert res1_code == 200 and user_fix1.id == res1_user.id
    username = user_fix3.username
    user_fix3.username = "Danny1250"
    res2_code,res2_user = user_Api.put_username(username=username, data=user_fix3.to_json())
    assert res2_code == 200 and user_fix3.username == res2_user.username


def test_delete_username(user_fix3: User, user_Api):
    res1 = user_Api.delete_username(username=user_fix3.username)
    assert res1.status_code == 200
    res1_code, res_user = user_Api.get_username(username=user_fix3.username)
    assert res1_code == 404
