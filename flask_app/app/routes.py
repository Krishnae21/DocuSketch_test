from db import collection
from flask import request, Blueprint, jsonify

keys_router = Blueprint("keys_router", __name__)


@keys_router.route("/key", methods=["GET", "POST", "PUT"])
def handle_key():
    if request.method == "POST":
        data = request.get_json()
        key = data.get("key")
        if key is None:
            return jsonify(
                {"status": 4, "message": "Key not found", "key": None, "value": None}
            )
        return post_handle(key, data)

    if request.method == "PUT":
        data = request.get_json()
        key = data.get("key")
        if key is None:
            return jsonify(
                {"status": 4, "message": "Key not found", "key": None, "value": None}
            )

        return put_handle(key, data)

    if request.method == "GET":
        key = request.args.get("key")
        if key is None:
            return jsonify(
                {"status": 4, "message": "Key not found", "key": None, "value": None}
            )
        return get_handle(key)


def post_handle(key: str, data: dict):
    value = data.get("value")
    if value is None:
        return jsonify(
            {"status": 5, "message": "Value not found", "key": None, "value": None}
        )

    result = collection.find_one({"key": key})
    if result is None:
        collection.insert_one({"key": key, "value": value})
        return jsonify(
            {"status": 0, "message": "Key added", "key": key, "value": value}
        )
    else:
        return jsonify(
            {
                "status": 1,
                "message": "The key already exists",
                "key": key,
                "value": None,
            }
        )


def put_handle(key: str, data: dict):
    new_value = data.get("value")
    if new_value is None:
        return jsonify(
            {"status": 6, "message": "Value not found", "key": None, "value": None}
        )

    check_key = collection.find_one({"key": key})
    if check_key:
        if check_key.get("value") == new_value:
            return jsonify(
                {
                    "status": 7,
                    "message": "The key has already been updated",
                    "key": key,
                    "value": new_value,
                }
            )

    result = collection.update_one({"key": key}, {"$set": {"value": new_value}})
    if result.modified_count > 0:
        return jsonify(
            {"status": 0, "message": "Key updated", "key": key, "value": new_value}
        )
    else:
        return jsonify(
            {
                "status": 2,
                "message": "Update error check key value",
                "key": key,
                "value": None,
            }
        )


def get_handle(key: str):
    result = collection.find_one({"key": key})
    if result:
        return jsonify(
            {"status": 0, "message": "Key found", "key": key, "value": result["value"]}
        )
    else:
        return jsonify(
            {"status": 3, "message": "Key doesn't exist", "key": key, "value": None}
        )
