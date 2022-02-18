
class InvalidKeysError(Exception):
    def __init__(self, passed: list, mandatory: list):
        self.message = {
            "mandatory keys": mandatory,
            "keys sent": passed
        }
        super().__init__(self.message)


class InvalidValueTypeError(Exception):
    keys = {
        "name": "string",
        "last_name": "string",
        "email": "string",
        "password": "string",
        "cep": "string",
        "street": "string",
        "neighborhood": "string",
        "state": "string",
        "phone": "string"
    }

    received = {
        str: "string",
        int: "integer",
        float: "float",
        list: "list",
        dict: "dictionary",
        bool: "boolean",
    }

    def __init__(self, data: dict):
        self.message = {
            "expected": self.keys,
            "received": {key: self.received[type(value)] for key, value in data.items()}
        }
        super().__init__(self.message)


class InvalidEmailError(Exception):
    def __init__(self):
        self.message = "Invalid Email"
        super().__init__(self.message)
