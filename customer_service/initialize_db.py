from customer_service.app import app, db

# Create application context
with app.app_context():
    db.create_all()
