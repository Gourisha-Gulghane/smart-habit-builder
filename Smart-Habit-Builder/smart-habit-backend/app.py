from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from auth import auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smart_habit.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

db.init_app(app)  # ⚠️ connect db with app
jwt = JWTManager(app)

app.register_blueprint(auth_bp)  # ⚠️ register blueprint

@app.route("/")
def home():
    return "Smart Habit Backend Running 🚀"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

