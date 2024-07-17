<<<<<<< HEAD
from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from . import routes
        return app
=======
from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from . import routes
        return app
>>>>>>> 383a55dab16c3c6b2eb3e0ff1b362f6ccf4b9ca8
