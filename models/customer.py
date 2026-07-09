from datetime import datetime
from extensions import db


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)

    company_name = db.Column(db.String(150), nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)

    phone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(150), nullable=True)

    industry = db.Column(db.String(80), nullable=True)

    address = db.Column(db.Text, nullable=True)
    city = db.Column(db.String(80), nullable=True)
    country = db.Column(db.String(80), nullable=True)

    status = db.Column(
        db.String(20),
        nullable=False,
        default="Prospect"
    )

    notes = db.Column(db.Text, nullable=True)

    owner_id = db.Column(
        db.Integer,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Customer {self.company_name}>"