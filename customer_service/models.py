from customer_service.app import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    preference = db.Column(db.String(10), nullable=False)  # 'email' or 'sms'




    def __repr__(self):
        return f'<Customer {self.name}>'
