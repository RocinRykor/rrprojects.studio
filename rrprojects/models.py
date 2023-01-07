from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    """
    | id:            The primary key for the user
    | username:      A string containing the user's login name
    | password:      A password hashed with werkzeug.generate_password_hash
    | is_admin:      A boolean determining whether or not the user is an admin
    | authenticated: Whether or not the user has logged in.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)

    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return True

    @property
    def password(self):
        return self.password_hash

    def get_id(self):
        return self.id

    def set_password(self, to_set):
        self.password_hash = generate_password_hash(to_set, method='pbkdf2:sha256',
                                               salt_length=24)

    def jsonify(self):
        """
        Returns the user as a JSON object

        -> JSON Object
        """

        return {
            "id": self.id,
            "username": self.username,
          }

class Project(db.Model):
    """
    | id:            The primary key for the project
    | title:         A string for the name of the project
    | repo_link:     URL to the github repository for the project
    | live_link:     URL to the active page for the project (such as Github Pages) 
    | description:   Large text desciprion for the project
    | img_filename:  Filename for an image representing the project 
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    repo_link = db.Column(db.String(256))
    live_link = db.Column(db.String(256))
    description = db.Column(db.String(8192))
    img_filename = db.Column(db.String(128))

    def jsonify(self):
        """
        Returns the Project as a JSON object

        -> JSON Object
        """

        return {
            "id": self.id,
            "title": self.title,
            "repo_link": self.repo_link,
            "live_link": self.live_link,
            "description": self.description,
            "img_filename": self.img_filename,
        }