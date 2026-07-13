from flask import Blueprint, render_template

from models.customer import Customer

main = Blueprint("main", __name__)


@main.route("/")
def home():

    total_customer = Customer.query.count()

    active_customer = Customer.query.filter_by(
        status="Active"
    ).count()

    prospect_customer = Customer.query.filter_by(
        status="Prospect"
    ).count()

    inactive_customer = Customer.query.filter_by(
        status="Inactive"
    ).count()

    return render_template(
        "dashboard.html",
        total_customer=total_customer,
        active_customer=active_customer,
        prospect_customer=prospect_customer,
        inactive_customer=inactive_customer
    )
