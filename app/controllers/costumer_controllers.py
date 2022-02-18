from flask import jsonify, request, current_app
from app.exceptions.customer_exceptions import InvalidKeysError, InvalidValueTypeError, InvalidEmailError
from sqlalchemy.exc import IntegrityError
from app.utils.check_functions import check_create_data_keys, check_data_values, check_email

from app.models.customer_model import CustomerModel


def create():

    data = request.get_json()

    try:

        check_create_data_keys(data)
        check_data_values(data)
        check_email(data["email"])

        password_to_hash = data.pop("password")

        custumer = CustomerModel(**data)
        custumer.password = password_to_hash
        current_app.db.session.add(custumer)
        print("*" * 15, custumer.password_hash, "*" * 15)

        current_app.db.session.commit()
        return jsonify({'data': custumer}), 201
    except InvalidKeysError as error:
        return jsonify(error.message), 400
    except InvalidValueTypeError as error:
        return jsonify(error.message), 400
    except InvalidEmailError as error:
        return jsonify(error.message), 400
    except IntegrityError:
        return jsonify({"message": "email already exists"}), 409


def get_all_customers():

    all_clients = CustomerModel.query.all()
    return jsonify(all_clients), 200
