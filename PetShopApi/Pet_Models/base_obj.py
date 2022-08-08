import json


class BaseObj:
    def __init__(self):
        pass
    def to_json(self) -> str:
        result = {}
        for key, val in self.__dict__.items():
            if val is not None:
                if key.startswith('_'):
                    result[key[1:]] = val
                else:
                    result[key] = val
        return result
    def __str__(self):
        return json.dumps(self.to_json())

    def is_base32(self):
        if 2147483647 >= self and self >= -2147483648:
            return True
        else:
            return False
    def is_base64(self):
        if 9223372036854775807 <= self and self <= -9223372036854775808:
            return False
        else:
            return True
