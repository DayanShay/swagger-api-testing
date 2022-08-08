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
    cat = Pet(id=12, name='danny', category=Category(id=1,name='Cats'), tags=[Tag(id=0,name='tag1')])
    return cat

@pytest.fixture(scope="session")
def test_status() -> petStatus:
    status = petStatus.available.value
    return status

def test_put_pet(Pet_fix,pet_Api):
    LOGGER.info("Start tests on PetApi")
    res_put_pet = pet_Api.post_pet(Pet_fix.to_json())
    LOGGER.info(res_put_pet.text)
    assert res_put_pet.status_code == 200 and res_put_pet.json()["id"] == Pet_fix.to_json()["id"]
    Pet_fix2 = Pet_fix
    Pet_fix2.name = "Yossy"
    pet = pet_Api.put_pet(Pet_fix2.to_json())
    LOGGER.info(pet.text)
    assert pet.status_code == 200 and pet.json()["name"] == Pet_fix2.to_json()["name"]

def test_post_pet(Pet_fix,pet_Api):
    res_put_pet = pet_Api.post_pet(Pet_fix.to_json())
    LOGGER.info(res_put_pet.text)
    assert res_put_pet.status_code == 200 and res_put_pet.json()["id"] == Pet_fix.to_json()["id"]

def test_find_by_status(test_status,Pet_fix,pet_Api):
    Pet_fix.status = test_status
    res_put_pet = pet_Api.post_pet(Pet_fix.to_json())
    LOGGER.info(res_put_pet.text)
    assert res_put_pet.status_code == 200 and res_put_pet.json()["id"] == Pet_fix.to_json()["id"]
    test = pet_Api.findByStatus(test_status)
    LOGGER.info(test.text)
    assert test.status_code == 200 and res_put_pet.json() in test.json()
    for items in test.json():
         pet_test = Pet(**items)
         assert test_status == pet_test.status

def test_find_by_tag(Pet_fix,pet_Api):
    res_put_pet = pet_Api.post_pet(Pet_fix.to_json())
    LOGGER.info(f'{Pet_fix.to_json()} on test_find_by_status ')
    assert res_put_pet.status_code == 200 and res_put_pet.json()["id"] == Pet_fix.to_json()["id"]
    res_get_tags = pet_Api.findByTags("tag1")
    LOGGER.info(res_get_tags.text)
    assert res_get_tags.status_code == 200
    pet_list = []
    for pets in res_get_tags.json():
        pet_list.append(Pet(**pets))
    for tags in pet_list:
        assert Pet_fix.tags[0] == tags.tags[0]

def test_get_pet_by_id(Pet_fix,pet_Api):
    res_post_pet = pet_Api.post_pet(Pet_fix.to_json())
    LOGGER.info(res_post_pet.text)
    assert res_post_pet.status_code == 200 and res_post_pet.json()["id"] == Pet_fix.to_json()["id"]
    res_get_id = pet_Api.get_pet(Pet_fix.id)
    LOGGER.info(res_get_id.text)
    assert res_get_id.status_code == 200 and res_get_id.json()["id"] == res_post_pet.json()["id"]

def test_update_name_or_status_by_id(test_status,Pet_fix,pet_Api):
    res_put_pet = pet_Api.post_pet(Pet_fix.to_json())
    LOGGER.info(res_put_pet.text)
    assert res_put_pet.status_code == 200 and res_put_pet.json()["id"] == Pet_fix.to_json()["id"]
    test = pet_Api.put_post_pet(id=Pet_fix.id,name="Danny",status=test_status)
    Pet_fix2 = Pet_fix
    Pet_fix2.name = "Danny"
    Pet_fix2.status = "available"
    LOGGER.info(test.text)
    assert test.status_code == 200 and test.json()["id"] == Pet_fix2.to_json()["id"]and test.json()["name"] == Pet_fix2.to_json()["name"]and test.json()["status"] == Pet_fix2.to_json()["status"]

def test_delete_by_id(Pet_fix,pet_Api):
    res_put_pet = pet_Api.post_pet(Pet_fix.to_json())
    LOGGER.info(res_put_pet.text)
    assert res_put_pet.status_code == 200 and res_put_pet.json()["id"] == Pet_fix.to_json()["id"]
    pet = pet_Api.get_pet(Pet_fix.id)
    LOGGER.info(pet.text)
    assert pet.status_code == 200 and pet.json()["id"] == res_put_pet.json()["id"]
    test = pet_Api.delete_pet(Pet_fix.id)
    LOGGER.info(test.text)
    assert test.status_code == 200 and test.text == "Pet deleted"
    res = pet_Api.get_pet(Pet_fix.id)
    LOGGER.info(res.text)
    assert res.status_code == 404 and res.text == "Pet not found"
    LOGGER.info("Finish tests on PetApi")

def test_upload_image(Pet_fix,pet_Api):
    res_post_pet = pet_Api.post_pet(Pet_fix.to_json())
    LOGGER.info(res_post_pet.text)
    assert res_post_pet.status_code == 200 and res_post_pet.json()["id"] == Pet_fix.to_json()["id"]
    image = '186462.jpg'
    pet = pet_Api.post_pet_uplaodImage(id=Pet_fix.id,photo=image)
    LOGGER.info(pet.text)
    assert pet.status_code == 200 and pet.json()["photoUrls"] != Pet_fix.photo_Urls




@pytest.fixture(scope="session")
def order_fix() :
    order = Order(id=1200, petId=12, quantity=7)
    return order
@pytest.mark.Store
def test_get_inventory(order_fix,store_Api):
    res1 = store_Api.get_inventory()
    LOGGER.info(res1.text)
    assert res1.status_code == 200 and res1.json() is not None ,res1.text
    order = order_fix
    res2 = store_Api.post_order(order)
    res3 = store_Api.get_inventory()
    LOGGER.info(res2.text)
    LOGGER.info(res3.text)
    assert res2.status_code == 200 and res2.json() is not None and res3.json() != res1.json() ,res2.text

def test_post_order(order_fix,store_Api):
    res1 = store_Api.post_order(order_fix)
    LOGGER.info(res1.text)
    assert res1.status_code == 200 and order_fix.id == res1.json()["id"]
    res2 = store_Api.get_order(order_fix.id)
    LOGGER.info(res2.text)
    assert res2.status_code == 200 and order_fix.to_json() == Order(**res2.json()).to_json()

def test_get_order_by_id(order_fix,store_Api):
    res1 = store_Api.post_order(order_fix)
    LOGGER.info(res1.text)
    assert res1.status_code == 200 and order_fix.id == res1.json()["id"],res1.text
    res2 = store_Api.get_order(order_fix.id)
    LOGGER.info(res2.text)
    assert res2.status_code == 200 and order_fix.to_json() == Order(**res2.json()).to_json(),res2.text

def test_delete_order(order_fix,store_Api):
    res1 = store_Api.post_order(order_fix)
    LOGGER.info(res1.text)
    assert res1.status_code == 200 and order_fix.id == res1.json()["id"] ,res1.text
    res2 = store_Api.get_order(order_fix.id)
    LOGGER.info(res2.text)
    assert res2.status_code == 200 and order_fix.to_json() == Order(**res2.json()).to_json(),res2.text
    res3 = store_Api.delete_order(order_fix.id)
    res4 = store_Api.get_order(order_fix.id)
    LOGGER.info(res4.text)
    LOGGER.info(res3.text)
    assert res3.status_code == 200 and res4.status_code == 404, res4.text

@pytest.fixture(scope="session")
def user_fix1() -> User:
    user = User(id=1250,username="user1250",userStatus=1,password="123456")
    return user
@pytest.fixture(scope="session")
def user_fix2() -> User:
    user = User(id=1251,username="user1251",userStatus=1,password="123456")
    return user
@pytest.fixture(scope="session")
def user_fix3() -> User:
    user = User(id=1252,username="user1250",userStatus=1,password="123456")
    return user
def test_post_user(user_fix1,user_Api):
    res1 = user_Api.post_user(data=user_fix1.to_json())
    LOGGER.info(res1.text)
    assert res1.status_code == 200 and user_fix1.to_json()["username"] == res1.json()["username"],res1.text
def test_login(user_fix1,user_Api):
    res1 = user_Api.get_login(username= user_fix1.username,password=user_fix1.password)
    LOGGER.info(res1.text)
    assert res1.status_code == 200
def test_get_user(user_fix1,user_Api):
    res2 = user_Api.get_username(username=user_fix1.to_json()["username"])
    LOGGER.info(res2.text)
    assert res2.status_code == 200 and user_fix1.to_json()["username"] == res2.json()["username"], res2.text
def test_post_user_with_list(user_fix1,user_fix2,user_Api):
    temp_users_list =[user_fix1.to_json(),user_fix2.to_json()]
    data = json.dumps(temp_users_list)
    res1 = user_Api.post_users_with_list(data=data)
    LOGGER.info(res1.text)
    assert res1.status_code == 200 and data == res1.json() ,res1.text
def test_logout(user_Api):
    res1 = user_Api.get_logout()
    LOGGER.info(res1.text)
    assert res1.status_code == 200
def test_put_username(user_fix3,user_Api):
    res1 = user_Api.post_user(data=user_fix3.to_json())
    LOGGER.info(res1.text)
    assert res1.status_code == 200 and user_fix3.to_json()["username"] == res1.json()["username"],res1.text
    username = user_fix3.username
    user_fix3.username = "Danny1250"
    res2 = user_Api.put_username(username= username,data=user_fix3.to_json())
    LOGGER.info(res2.text)
    assert res2.status_code == 200 and user_fix3.username == res2.json()["username"], res2.text
def test_delete_username(user_fix3,user_Api):
    res1 = user_Api.delete_username(username=user_fix3.username)
    LOGGER.info(res1.text)
    assert res1.status_code == 200
    res2 = user_Api.get_username(username=user_fix3.username)
    LOGGER.info(res2.text)
    assert res2.status_code == 404
