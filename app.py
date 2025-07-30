from flask import Flask, render_template, request, redirect
from models import db, init_db, Expense, Member, Booking, Invoice, Staff
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if request.method == 'POST':
        new_expense = Expense(
            category=request.form['category'],
            amount=float(request.form['amount']),
            date=request.form['date'],
            note=request.form['note']
        )
        db.session.add(new_expense)
        db.session.commit()
        return redirect('/expenses')
    all_expenses = Expense.query.all()
    return render_template('expenses.html', expenses=all_expenses)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)