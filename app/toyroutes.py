# from app import db
from app.models.toy import Toy
from flask import Blueprint, request, jsonify, make_response, abort
import os, requests

toys_bp = Blueprint("toys_bp", __name__, url_prefix="/toys")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

@toys_bp.route("", methods=["POST"])
def create_toy():
    request_body = request.get_json()
    return make_response(request_body,201)
    # new_toy = Toy.from_dict(request_body)
    
    # db.session.add(new_toy)
    # db.session.commit()
    
    # return make_response(jsonify(new_toy.to_dict()), 201)

@toys_bp.route("/<toy_id>", methods=["GET"])
def get_one_toy(toy_id):
    # fake_toy = Toy(int(toy_id),"maribel", 2.50, "telecom")
    fake_toy = {
        "id": "4",
        "name": "mirabel",
        "price":"2.50",
        "brand": "telecom"
    }
    return make_response(fake_toy, 200)
#     toy = validate_model(Toy, toy_id)
#     # return toy.to_dict()
#     



