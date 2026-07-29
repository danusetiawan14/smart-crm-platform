from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from models.user import User

from werkzeug.security import check_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:

        return redirect(
            url_for("main.home")
        )

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if user and check_password_hash(user.password, password):

            remember = request.form.get("remember") == "on"

            login_user(
                user,
                remember=remember
            )

            flash(
                "Welcome back!",
                "success"
            )

            return redirect(
                url_for("main.home")
            )

        flash(
            "Invalid email or password.",
            "danger"
        )

    return render_template("auth/login.html")

@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "You have successfully logged out.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )