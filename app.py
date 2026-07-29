from flask import Flask

from config import Config
from extensions import db, login_manager

from routes.main import main

from models import Customer

from routes.customer import customer

from models import Customer, User

from routes.auth import auth

from extensions import db, login_manager

from werkzeug.security import generate_password_hash

from routes.user import user

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

login_manager.init_app(app)

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

    if User.query.count() == 0:

        admin = User(

            full_name="Administrator",

            email="admin@smartcrm.com",

            password=generate_password_hash("admin123"),

            role="Owner"

        )

        db.session.add(admin)

        db.session.commit()

# Register Blueprint
app.register_blueprint(main)
app.register_blueprint(customer)
app.register_blueprint(auth)
app.register_blueprint(user)

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(
        int(user_id)
    )


if __name__ == "__main__":
    app.run(debug=True)