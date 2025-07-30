from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    amount = db.Column(db.Float)
    date = db.Column(db.String(20))
    note = db.Column(db.String(200))

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    plan = db.Column(db.String(50))
    start_date = db.Column(db.String(20))

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    space_type = db.Column(db.String(50))
    from_date = db.Column(db.String(20))
    to_date = db.Column(db.String(20))

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    due_date = db.Column(db.String(20))
    status = db.Column(db.String(20))

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    role = db.Column(db.String(50))
    salary = db.Column(db.Float)
    join_date = db.Column(db.String(20))

def init_db():
    db.create_all()