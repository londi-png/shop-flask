# Запуск и маршруты
from flask import Flask,request,jsonify
from database import db
from models import Product

app = Flask(__name__)

# конфигурация подключения
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///products.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "Система управления магазином"

if __name__ == "__main__":
    app.run(debug=True)
