from flask import render_template, Blueprint, redirect, session, request

general = Blueprint("general", __name__)


@general.route("/")
def index():
    return render_template("index.html")
