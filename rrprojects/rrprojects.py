from config import Config
from flask import Flask
from flask_migrate import Migrate
from routes.general import general
from routes.admin import admin
from models import db


migrate = Migrate()


def build_app():

    app = Flask(__name__)
    app.config.from_object(Config())
    app.register_blueprint(general)
    app.register_blueprint(admin)
    db.init_app(app)
    migrate.init_app(app, db)

    return app


application = build_app()


if __name__ == "__main__":
    application.run(debug=True)
