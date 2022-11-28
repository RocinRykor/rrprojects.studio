from flask import render_template, Blueprint  # , redirect, session, request

general = Blueprint("general", __name__)


@general.route("/")
def index():
    return render_template("index.html")

@general.route("/work")
def work():
    return render_template("work.html")

@general.route("/about")
def about():
    return render_template("about.html")


@general.route("/contact")
def contact():
    return render_template("contact.html")
