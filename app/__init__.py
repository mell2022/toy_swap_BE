from flask import Flask
from flask_cors import CORS
# Register Blueprints here
# from .routes import example_bp
# app.register_blueprint(example_bp)

def create_app(test_config=None):
    app = Flask(__name__)
    
    from app.toyroutes import toys_bp
    app.register_blueprint(toys_bp)

    CORS(app)
    return app
