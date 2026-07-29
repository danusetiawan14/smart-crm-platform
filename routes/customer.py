from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from extensions import db

from models.customer import Customer

from models.customer import Customer

from flask_login import login_required

customer = Blueprint(
    "customer",
    __name__
)


@customer.route("/customers")
@login_required
def index():

    search = request.args.get("search", "")

    query = Customer.query

    if search:

        query = query.filter(

            Customer.company_name.contains(search)

            |

            Customer.contact_person.contains(search)

            |

            Customer.phone.contains(search)

        )

    customers = query.order_by(
        Customer.company_name
    ).all()

    return render_template(
        "customers/index.html",
        customers=customers
    )

@customer.route("/customers/create", methods=["GET"])
@login_required
def create():

    return render_template(
        "customers/create.html"
    )

@customer.route("/customers/store", methods=["POST"])
@login_required
def store():

    customer = Customer(

        company_name=request.form["company_name"],

        contact_person=request.form["contact_person"],

        phone=request.form["phone"],

        email=request.form["email"],

        website=request.form["website"],

        industry=request.form["industry"],

        address=request.form["address"],

        status=request.form["status"]

    )

    db.session.add(customer)

    db.session.commit()

    flash(
        "Customer created successfully!",
        "success"
    )

    return redirect(
        url_for("customer.index")
    )

@customer.route("/customers/edit/<int:id>", methods=["GET"])
@login_required
def edit(id):

    customer_data = Customer.query.get_or_404(id)

    return render_template(
        "customers/edit.html",
        customer=customer_data
    )

@customer.route("/customers/update/<int:id>", methods=["POST"])
@login_required
def update(id):

    customer_data = Customer.query.get_or_404(id)

    customer_data.company_name = request.form["company_name"]
    customer_data.contact_person = request.form["contact_person"]
    customer_data.phone = request.form["phone"]
    customer_data.email = request.form["email"]
    customer_data.website = request.form["website"]
    customer_data.industry = request.form["industry"]
    customer_data.address = request.form["address"]
    customer_data.status = request.form["status"]

    db.session.commit()

    flash(
        "Customer updated successfully!",
        "success"
    )

    return redirect(
        url_for("customer.index")
    )

@customer.route("/customers/delete/<int:id>", methods=["POST"])
@login_required
def delete(id):

    customer = Customer.query.get_or_404(id)

    db.session.delete(customer)

    db.session.commit()

    flash(
        "Customer deleted successfully!",
        "success"
    )

    return redirect(
        url_for("customer.index")
    )