from flask import jsonify
 

def welcome():

    return jsonify({"msg": "Welcome to my API"}), 200
