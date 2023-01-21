from flask import render_template, Blueprint, redirect, request
from flask_login import login_required, current_user
from rrprojects.app import db, User, Project
from rrprojects.forms import ProjectForm
from rrprojects.routes.api.projects import projects_api
from rrprojects.utils import replace_bbcode, replace_markdown

project = Blueprint("project", __name__, url_prefix="/project")

@project.route("/")
def projects():
    projects = projects_api.get_all()
    return render_template("public/projects/projects.html", 
                            title="Steven's Projects", 
                            projects=projects, 
                            replace_func=replace_markdown)

@project.route("/<project_name>")
def project_page(project_name):
    project = projects_api.get_project_by_name(project_name)

    return render_template("public/projects/project_page.html", project=project,
                            title=project_name,
                            replace_func=replace_markdown)

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
    repo_link_description = form.repo_link_description.data
    live_link = form.live_link.data
    live_link_description = form.live_link_description.data
    short_description = form.short_description.data
    description = form.description.data
    img_filename = form.img_filename.data

    project = Project(title=title, repo_link=repo_link, repo_link_description=repo_link_description, 
                                    live_link=live_link, live_link_description=live_link_description, 
                                    short_description=short_description, description=description, 
                                    img_filename=img_filename)

    db.session.add(project)
    db.session.commit()

    return projects()