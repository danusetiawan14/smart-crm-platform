from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from models.customer import Customer

customer = Blueprint(
    "customer",
    __name__
)


@customer.route("/customers")
def index():

    customers = Customer.query.order_by(
        Customer.company_name
    ).all()

    return render_template(
        "customers/index.html",
        customers=customers
    )

@customer.route("/customers/create", methods=["GET"])
def create():

    return render_template(
        "customers/create.html"
    )