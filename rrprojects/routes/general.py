from flask import render_template, Blueprint  # , redirect, session, request

general = Blueprint("general", __name__)


@general.app_errorhandler(404)
def custom_error_page(e):
    return render_template("public/error.html", title="404 - Page Not Found!")


@general.route("/")
def index():
    return render_template("public/index.html", title="Portfolio Site")

