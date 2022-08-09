from PetShopApi.Pet_Models.base_obj import BaseObj


class Category(BaseObj):

    def __init__(self, id: int = None, name: str = None):
        super(BaseObj, self).__init__()
        self._id = id
        self._name = name
        if id is not None and not BaseObj.is_base64(id):
            if not isinstance(id, int):
                raise AttributeError("Id must be id int64 base")
            self._id = id
        if name is not None:
            if not isinstance(name, str):
                raise AttributeError("name must be string")
            self._name = name
