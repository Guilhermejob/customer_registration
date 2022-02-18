from app.exceptions.customer_exceptions import InvalidKeysError, InvalidValueTypeError, InvalidEmailError

from re import S, fullmatch

from app.models.customer_model import CustomerModel


def check_email(email: str):
    pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    is_valid = fullmatch(pattern, email)
    if not is_valid:
        raise InvalidEmailError


def check_create_data_keys(data):
    if (len(data) < len(CustomerModel.mandatory_keys)):
        raise InvalidKeysError(
            list(data.keys()), CustomerModel.mandatory_keys)


def check_data_values(data):

    for key, value in data.items():
        if ((
            key == "name" or
            key == "last_name" or
            key == "email" or
            key == "password" or
            key == "cep" or
            key == "street" or
            key == "neighborhood" or
            key == "state" or
            key == "phone"
        ) and type(value) != str):
            raise InvalidValueTypeError(data)
