from flask import Flask
# Register Blueprints here
# from .routes import example_bp
# app.register_blueprint(example_bp)

def create_app(test_config=None):
    app = Flask(__name__)
    
    from app.toyroutes import toys_bp
    app.register_blueprint(toys_bp)


    return app
