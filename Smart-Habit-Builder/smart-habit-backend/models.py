from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()  # ⚠️ No app reference here

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    habit_name = db.Column(db.String(120), nullable=False)
    start_date = db.Column(db.Date, nullable=False)

class HabitLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    log_date = db.Column(db.Date, default=date.today)
    status = db.Column(db.Boolean, default=False)
