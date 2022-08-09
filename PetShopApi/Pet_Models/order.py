from PetShopApi.Pet_Models.base_obj import BaseObj
import datetime
from enum import Enum


class Status(Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered "


class Order(BaseObj):

    def __init__(self, id: int, petId: int, quantity=None, shipDate=None, status=None, complete=False):
        super(BaseObj, self).__init__()
        if not str(id).isdigit() and not BaseObj.is_base64(id):
            raise TypeError("order id must be a integer!")
        if not str(petId).isdigit() and not BaseObj.is_base64(id):
            raise TypeError("order pet_id must be a integer!")

        self._id = id
        self._petId = petId
        self._quantity = quantity
        self._shipDate = shipDate
        self._status = status
        self._complete = complete
        if quantity is not None:
            if not str(quantity).isdigit() and not BaseObj.is_base64(id):
                raise TypeError("order quantity must be a integer!")
            self._quantity = quantity
        if shipDate is not None:
            if not isinstance(shipDate, datetime.datetime):
                raise TypeError("order shipDate must be a datetime!")
            self._shipDate = shipDate
        if status is not None:
            if not isinstance(status, str):
                raise TypeError("order status must be a string!")
            Status(status)
            self._status = status
        if complete is not False:
            if not isinstance(complete, bool):
                raise TypeError("order complete must be a boolean!")
            self._complete = complete

    @property
    def id(self):
        """Gets the id of this Order.
        :return: The id of this Order.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, Id):
        """Sets the id of this Order.
        :param Id: The id of this Order.
        :type: int
        """
        self._id = Id

    @property
    def pet_id(self):
        """Gets the petId of this Order.
        :return: The petId of this Order.
        :rtype: int
        """
        return self._petId

    @pet_id.setter
    def pet_id(self, petId):
        """Sets the petId of this Order.
        :param petId: The petId of this Order.
        :type: int
        """
        self._petId = petId

    @property
    def quantity(self):
        """Gets the quantity of this Order.
        :return: The quantity of this Order.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Order.
        :param quantity: The quantity of this Order.
        :type: int
        """
        self._quantity = quantity

    @property
    def shipDate(self):
        """Gets the shipDate of this Order.
        :return: The shipDate of this Order.
        :rtype: datetime
        """
        return self._shipDate

    @shipDate.setter
    def shipDate(self, shipDate):
        """Sets the shipDate of this Order.
        :param shipDate: The quantity of this Order.
        :type: datetime
        """
        if shipDate is None:
            raise ValueError("Invalid value for `shipDate`, must not be `None`")
        self._shipDate = shipDate

    @property
    def status(self):
        """Gets the status of this Order.
        :return: The status of this Order.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.
        :param status: The quantity of this Order.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        self._status = status

    @property
    def complete(self):
        """Gets the complete of this Order.
        :return: The complete of this Order.
        :rtype: boolean
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this Order.
        :param complete: The quantity of this Order.
        :type: boolean
        """
        if complete is None:
            raise ValueError("Invalid value for `complete`, must not be `None`")
        self._complete = complete
