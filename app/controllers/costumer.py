from flask import jsonify, request, current_app

from app.models.customer_model import CustomerModel


def create():

    data = request.get_json()

    try:
        password_to_hash = data.pop("password")

        custumer = CustomerModel(**data)
        custumer.password = password_to_hash
        current_app.db.session.add(custumer)
        print("*" * 15, custumer.password_hash, "*" * 15)

        current_app.db.session.commit()
        return jsonify({'data': custumer}), 201
    except:
        return jsonify({"msg": "Deu ruim"}), 400


def get_all_customers():
    
    all_clients = CustomerModel.query.all()
    return jsonify(all_clients), 200
