# from app import db
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from app.models.toy import Toy
from flask import Blueprint, request, jsonify, make_response, abort

# Use a service account to access our firebase
cred = credentials.Certificate('/Users/melleygebretatios/Developers/capstone/toyswap-0125-30fa05cd6bd3.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

toys_bp = Blueprint("toys_bp", __name__, url_prefix="/toys")

@toys_bp.route("", methods=["POST"])
def create_user():
    request_body = request.get_json()
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1965
    })
    return make_response(request_body,201)

@toys_bp.route("/<user_id>", methods=["GET"])
def get_one_user(user_id):
    users_ref = db.collection(u'users')
    user = users_ref.document(user_id).get()
    return jsonify(user.to_dict()), 200

@toys_bp.route("", methods=["GET"])
def get_all_toys():
    users_ref = db.collection(u'users')
    all_users = [doc.to_dict() for doc in users_ref.stream()]
    return jsonify(all_users), 200
        


