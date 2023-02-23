from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    
    from app.toyroutes import toys_bp
    app.register_blueprint(toys_bp)

    CORS(app)
    return app
