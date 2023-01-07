from .config import Config
from . import models
from flask import Flask, redirect
from flask_login import LoginManager
from flask_migrate import Migrate

db = models.db

# Create any items that will be used in the app
User = models.User
Project = models.Project

migrate = Migrate()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(id=user_id).first()


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login/')


def check_user():
    """
    A function that can be used to do some form of authentication for user
    login to view the statistics page. Currently this just returns True,
    which is no check at all, but you can add this in later.
    """
    return True


def build_app():

    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app, db)

    with app.app_context():
        # Base Routes
        from .routes.general import general
        #from .routes.auth import auth

        #API Routes
        
        app.register_blueprint(general)
        #app.register_blueprint(auth)


        print("Creating")
        db.create_all()
        print("done")

    return app


application = build_app()


if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0")
