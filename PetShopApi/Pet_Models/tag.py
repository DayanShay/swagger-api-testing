from PetShopApi.Pet_Models.base_obj import BaseObj


class Tag(BaseObj):
    def __init__(self, id: int = None, name: str = None) -> object:
        '''
        Constructor
        '''
        self._id = id
        self._name = name
        if id is not None:
            if not isinstance(id, int) or not str(id).isdigit():
                raise AttributeError("Id must be id int64 base")
            self._id = id
        if name is not None:
            if not isinstance(name, str):
                raise AttributeError("name must be string")
            self._name = name


    @property
    def name(self):
        """Gets the name of this tag.
        :return: The name of this tag.
        :rtype: int
        """
        return self._name

    def __repr__(self):
        return f"{self}".replace('"',"'")
