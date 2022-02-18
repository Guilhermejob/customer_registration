from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.models.customer_model import CustomerModel
from app.exceptions.login_exceptions import EmailNotFoundError, IncorrectPasswordError, InvalidKeyError


def signin_customer():
    data = request.get_json()

    try:
        if len(data) > 2 or not 'email' in data.keys() or not 'password' in data.keys():
            raise InvalidKeyError(data)

        customer = CustomerModel.query.filter_by(email=data['email']).first()

        if not customer:
            raise EmailNotFoundError()

        if not customer.check_password(data['password']):
            raise IncorrectPasswordError()

        access_token = create_access_token(customer)

    except EmailNotFoundError as error:
        return jsonify(error.message), 404
    except IncorrectPasswordError as error:
        return jsonify(error.message), 401
    except InvalidKeyError as error:
        return jsonify(error.message), 400

    return {"access_token": access_token}, 200
