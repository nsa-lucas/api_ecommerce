from .products import products_bp
from .users import users_bp

def register_routes(app):
    app.register_blueprint(products_bp)
    app.register_blueprint(users_bp)