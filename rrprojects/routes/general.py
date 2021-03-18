from flask import render_template, Blueprint, redirect, session, request

general = Blueprint("general", __name__)


@general.route("/")
def index():
    return "<h1>This will be the main page</h1>"
