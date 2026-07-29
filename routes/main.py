from flask import Blueprint, render_template

from models.customer import Customer

from flask_login import login_required

main = Blueprint("main", __name__)


@main.route("/")
@login_required
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

    chart_data = {

        "active": active_customer,

        "prospect": prospect_customer,

        "inactive": inactive_customer

    }

    recent_customers = Customer.query.order_by(
        Customer.created_at.desc()
    ).limit(5).all()
    
    return render_template(
        "dashboard.html",
        total_customer=total_customer,
        active_customer=active_customer,
        prospect_customer=prospect_customer,
        inactive_customer=inactive_customer,
        recent_customers=recent_customers,
        chart_data=chart_data
    )
