from rrprojects.app import db, Project
from flask_login import current_user
from sqlalchemy import func

def create_project(project_json):
    """
    JSON KEYS:
    | title:         String (64)
    | repo_link:     String (256)
    | live_link:     String (256)
    | description:   String (8192)
    | img_filename:  String (128)
    
    -> Project
    """

    project = project = Project(title=title, repo_link=repo_link, live_link=live_link, description=description, img_filename=img_filename)

    db.session.add(project)
    db.session.commit()

    return project

def get_project(project_id):
    """
    Gets a single project from the database specified by the project_id

    Parameters:
    ===========
    project_id: int

    -> Project or None
    """

    project = Project.query.filter_by(id=project_id).first()
    
    return project

def get_all():
    """
    Creates a multi project object that has all the projects in the database

    -> project(s) JSON
    """
    projects = Project.query.all()
    print(projects)
    return projects

def random_project():
    """
    Gets a random Project from the database

    -> Project
    """

    return Project.query.order_by(func.random()).first()