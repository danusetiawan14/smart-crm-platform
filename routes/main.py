from flask import Blueprint, render_template

# Membuat Blueprint
main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("dashboard.html")