# Модели таблиц
from database import db

class Product(db.Model):
    __tablename__= "product"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),nullable = False)
    quantity = db.Column(db.Integer,nullable=False)
    category = db.Column(db.String(50),nullable=False)
    price = db.Column(db.Float,default = 0.0)
    article = db.Column(db.String(100),nullable=False,unique = True)

    def __str__(self):
        return self.name
