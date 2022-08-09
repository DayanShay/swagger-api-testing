from PetShopApi.Pet_Models.petStatus import petStatus
from PetShopApi.Pet_Models.base_obj import BaseObj
from PetShopApi.Pet_Models.tag import Tag
from PetShopApi.Pet_Models.category import Category

data = {
    "id": 10,
    "name": "doggie",
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


class Pet(BaseObj):
    def __init__(self, id: int, name: str, category=None, photoUrls: list[str, str] = None, tags: Tag = None,
                 status: petStatus = None) -> object:
        super(BaseObj, self).__init__()
        if not isinstance(id, int) and not BaseObj.is_base64(id):
            raise AttributeError("Id must be id int")
        if not isinstance(name, str):
            raise AttributeError("name must be string")
        self._id = id
        self._name = name
        self._photo_Urls = photoUrls
        self._tags = tags
        if category is not None:
            if not isinstance(category, Category) and not isinstance(category, dict):
                raise TypeError("category must be instance of Category or dict!")
            if isinstance(category, dict) and isinstance(category, Category):
                category = Category(**category)
            self._category = category
        self._category = category
        if photoUrls is not None:
            if not isinstance(photoUrls, list):
                raise AttributeError("photoUrls must be a list")
            for item in photoUrls:
                if not isinstance(item, str):
                    raise AttributeError("photoUrls must be strings")
            self.photo_urls = photoUrls
        self._tags = tags
        if tags is not None:
            if isinstance(tags, list):
                self._tags = tags
        if status is not None and isinstance(status, petStatus):
            self._status = status.value
        if isinstance(status, str):
            self._status = status
        self._status = status

    @property
    def id(self):
        """Gets the id of this Pet.  # noqa: E501
        :return: The id of this Pet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pet.
        :param id: The id of this Pet.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Pet.
        :return: The name of this Pet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pet.
        :param name: The name of this Pet.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        self._name = name

    @property
    def status(self):
        """Gets the status of this Pet.
        :return: The status of this Pet.
        :rtype: enum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Pet.
        :param status: The status of this Pet.
        :type: enum
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this Pet.
        :return: The tags of this Pet.
        :rtype: Tag
        """
        return self._tags

    @tags.setter
    def tags(self, tags: Tag):
        """Sets the tags of this Pet.
        :param tags: The tags of this Pet.
        :type: Tag
        """
        self._tags = tags

    @property
    def photo_Urls(self):
        """Gets the Photo Urls of this Pet.
        :return: The Photo Urls of this Pet.
        :rtype: str
        """
        return self._photo_Urls

    @photo_Urls.setter
    def photo_Urls(self, photoUrls: list[str, str]):
        """Sets the photoUrls of this Pet.
        :param photo_Urls: The Photo Urls of this Pet.
        :type: str
        """
        self._photo_Urls = photoUrls


