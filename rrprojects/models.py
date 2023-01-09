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

        output = {
            "id": self.id,
            "title": self.title,
            "repo_link": self.repo_link,
            "live_link": self.live_link,
            "description": self.description,
            "img_filename": self.img_filename,
        }

        print(output)

        return output

class BlogPost(db.Model):
    """
    A model representing a blog post.
    | id:            The primary key for the blog post
    | title:         A string containing the title of the blog post
    | content:       A string containing the content of the blog post
    | author_id:     An integer representing the user who wrote the blog post
    | author:        A relationship to the user who wrote the blog post
    | created_at:    A datetime object representing the date and time the blog post was created
    | updated_at:    A datetime object representing the date and time the blog post was last updated
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    author = db.relationship('User', back_populates='blog_posts')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def jsonify(self):
        """
        Returns the blog post as a JSON object.

        -> JSON object
        """
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author_id": self.author_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }