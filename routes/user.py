from flask import Blueprint, render_template

from flask_login import login_required

from models.user import User

user = Blueprint(
    "user",
    __name__
)

@user.route("/users")
@login_required
def index():

    users = User.query.order_by(
        User.full_name
    ).all()

    return render_template(
        "users/index.html",
        users=users
    )