# from app import db
# from flask import Blueprint, jsonify

class Toy:
    def __init__(self, id, name, price, brand):
        self.id = id
        self.name = name
        self.price = price
        self.brand = brand
    
    
toy = [
    Toy(1, "Mirabel", 2.50, "telecom"),
    Toy(2, "Isabella", 50.00, "Encanto"),
    Toy(3, "Bruno", 30.00, "Disney"),
]
