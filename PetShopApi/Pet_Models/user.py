from PetShopApi.Pet_Models.base_obj import BaseObj

class User(BaseObj):

    def __init__(self, id: int,userStatus, username: str=None, firstName=None, password: str = None, lastName=None, email=None, phone=None):
        if not str(id).isdigit() and not BaseObj.is_base64(id):
            raise TypeError("user id must be a integer!")
        self._id = id
        if not isinstance(username, str):
            raise TypeError("user name must be string!")
        self._username = username
        if password is not None:
            if not isinstance(password, str):
                raise TypeError("password must be string")
        self._password = password
        self._firstName = firstName
        self._lastName = lastName
        self._email = None
        self._phone = None
        self._userStatus = None

        if firstName is not None:
            if not isinstance(firstName, str):
                raise TypeError("first name must be string!")
            self._firstName = firstName

        if lastName is not None:
            if not isinstance(lastName, str):
                raise TypeError("last name must be string!")
            self._lastName = lastName

        if email is not None:
            if not isinstance(email, str):
                raise TypeError("email must be string!")
            self._email = email

        if phone is not None:
            if not str(phone).isdigit():
                raise TypeError("phone must be integer!")
            self._phone = phone

        if userStatus is not None:
            if not str(userStatus).isdigit() and not BaseObj.is_base32(userStatus):
                raise TypeError("user status name must be a integer")
            self._userStatus = userStatus

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501
        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, Id):
        """Sets the id of this User.
        :param id: The id of this User.  # noqa: E501
        :type: int
        """
        self._id = Id

    @property
    def username(self):
        """Gets the user_name of this User.  # noqa: E501
        :return: The user_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the name of this User.
        :param user_name: The user_name of this User.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501
        self._username = username

    @property
    def password(self):
        """Gets the password of this User.  # noqa: E501
        :return: The password of this User.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.
        :param password: The password of this User.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        self._password = password

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501
        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._firstName

    @first_name.setter
    def first_name(self, firstName):
        """Sets the first_name of this User.
        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """
        if firstName is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        self._user_name = firstName

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501
        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._lastName

    @last_name.setter
    def last_name(self, lastName):
        """Sets the last_name of this User.
        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """
        if lastName is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        self._lastName = lastName

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501
        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.
        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        self._email = email

    @property
    def phone(self):
        """Gets the phone of this User.  # noqa: E501
        :return: The phone of this User.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this User.
        :param phone: The phone of this User.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501
        self._phone = phone

    @property
    def userStatus(self):
        """Gets the user_status of this User.  # noqa: E501
        :return: The user_status of this User.  # noqa: E501
        :rtype: str
        """
        return self._userStatus

    @userStatus.setter
    def user_status(self, userStatus):
        """Sets the user_status of this User.
        :param user_status: The user_status of this User.  # noqa: E501
        :type: str
        """
        if userStatus is None:
            raise ValueError("Invalid value for `user_status`, must not be `None`")  # noqa: E501
        self._userStatus = userStatus

