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
    user1_ref = users_ref.document(email1)
    user1 = user1_ref.get().to_dict()
    
    # Get the toy to be swapped for user1
    user1_toy = [toy for toy in user1["toys"] if toy["name"].upper() == toy1.upper()]
    
    # Get the user referenced by email2
    user2_ref = users_ref.document(email2)
    user2 = user2_ref.get().to_dict()
    
    # Get the toy to be swapped for user2
    user2_toy = [toy for toy in user2["toys"] if toy["name"].upper() == toy2.upper()]
    
    
    # Add user2's toy to user1's toys list
    user1["toys"].append(user2_toy[0])
    # Add user1's toy to user2's toys list
    user2["toys"].append(user1_toy[0])
    #use remove builtin function
    user2["toys"].remove(user2_toy[0])
    user1["toys"].remove(user1_toy[0])

    # Save to Firebase
    user1_ref.set(user1)
    user2_ref.set(user2)
    
    results = [user1, user2]
    
    return make_response(jsonify(results),200)



