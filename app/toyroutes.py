# from app import db
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from app.models.toy import Toy, User
from flask import Blueprint, request, jsonify, make_response, abort

# Use a service account to access our firebase
cred = credentials.Certificate('/Users/melleygebretatios/Developers/capstone/toyswap-0125-30fa05cd6bd3.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

toys_bp = Blueprint("toys_bp", __name__, url_prefix="/toys")

@toys_bp.route("/<email>", methods=["GET"])
def get_one_user(email):
    users_ref = db.collection(u'users')
    user = users_ref.document(email).get()
    return jsonify(user.to_dict()), 200

@toys_bp.route("", methods=["GET"])
def get_all_toys():
    users_ref = db.collection(u'users')
    all_users = [doc.to_dict() for doc in users_ref.stream()]
    return jsonify(all_users), 200

@toys_bp.route("/<email>", methods=["POST"])
def create_user(email):
    request_body = request.get_json()
    doc_ref = db.collection(u'users').document(email)
    doc_ref.set(request_body)
    return make_response(request_body,201)

@toys_bp.route("/swap/<email1>/<toy1>/<email2>/<toy2>", methods=["POST"])
def swap_toy(email1, toy1, email2, toy2):
    # Get users collection
    users_ref = db.collection(u'users')
    
    # Get the user referenced by email1
    user1 = users_ref.document(email1).get().to_dict()
    # Get the toy to be swapped for user1
    user1_toy = [toy for toy in user1["toys"] if toy["name"] == toy1]
    
    # Get the user referenced by email2
    user2 = users_ref.document(email2).get().to_dict()
    # Get the toy to be swapped for user2
    user2_toy = [toy for toy in user2["toys"] if toy["name"] == toy2]
    
    # Add user2's toy to user1's toys list
    user1["toys"].append(user2_toy[0])
    # Add user1's toy to user2's toys list
    user2["toys"].append(user1_toy[0])
    
    # TODO: Remove swapped items from list
    # ind = get_toy_index(user1["toys"], user1_toy)
    # user1["toys"][ind].clear()
    
    return make_response(jsonify(user1),200)

def get_toy_index(toys, toy):
    for i in range(len(toys)):
        if toys[i]["name"] == toy["name"]:
            print(i)
            return i 


