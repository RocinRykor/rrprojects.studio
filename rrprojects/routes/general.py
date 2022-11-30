from flask import render_template, Blueprint  # , redirect, session, request

general = Blueprint("general", __name__)

@general.route("/")
def index():
    return render_template("index.html", title="Portfolio Site")

@general.route("/work")
def work():
    return render_template("work.html", title="Steven's Projects")

@general.route("/about")
def about():
    return render_template("about.html", title="About Steven")


@general.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Steven")

@general.route("/error")
def error_page():
    return render_template("error.html", title="404 - Page Not Found!")