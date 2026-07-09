from flask import Flask

from config import Config
from extensions import db

from routes.main import main

from models import Customer

from routes.customer import customer


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():

    db.create_all()

    if Customer.query.count() == 0:

        customer = Customer(
            company_name="PT Smart Indonesia",
            contact_person="Budi Santoso",
            phone="08123456789",
            email="budi@smartcrm.com",
            status="Active"
        )

        db.session.add(customer)
        db.session.commit()

# Register Blueprint
app.register_blueprint(main)
app.register_blueprint(customer)


if __name__ == "__main__":
    app.run(debug=True)