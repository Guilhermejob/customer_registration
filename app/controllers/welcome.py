from flask import jsonify


def welcome():

    return jsonify({"msg": "Welcome to my API", "my_github_url": "https://github.com/Guilhermejob"}), 200
