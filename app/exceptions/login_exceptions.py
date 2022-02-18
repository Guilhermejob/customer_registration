class EmailNotFoundError(Exception):

    def __init__(self, email) -> None:

        self.message = {
            "message": "Email or password mismatch"
        }

        super().__init__(self.message)


class IncorrectPasswordError(Exception):

    def __init__(self) -> None:

        self.message = {
            "message": "Email or password mismatch"
        }

        super().__init__(self.message)


class InvalidKeyError(Exception):

    def __init__(self, data) -> None:
        self.message = {
            "mandatory keys": {
                "email": "string",
                "password": "string"
            },
            "key sent": [
                {
                    "key": key
                } for key in data
            ]
        }
        super().__init__(self.message)
