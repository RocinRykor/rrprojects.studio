from flask import render_template, Blueprint, redirect, request
from flask_login import login_required, current_user
from rrprojects.app import db, User
from rrprojects.forms import ProjectForm

project = Blueprint("project", __name__, url_prefix="/project")

@project.route("/")
def projects():
    #get projects
    return render_template("public/projects/projects.html", title="Steven's Projects")#, projects=projects

@login_required
@project.route("/add", methods=["GET"])
def get_add_project():
    form = ProjectForm(request.form)
    return render_template("public/projects/add_project.html", form=form)

@login_required
@project.route("/add", methods=["POST"])
def finish_add_project():
    form = ProjectForm(request.form)

    title = form.title.data
    repo_link = form.repo_link.data
    live_link = form.live_link.data
    description = form.description.data
    portrait_filename = form.portrait_filename.data

    project = Project(title=title, repo_link=repo_link, live_link=live_link, description=description, portrait_filename=portrait_filename)

    db.session.add(project)
    db.session.commit()

    return projects()