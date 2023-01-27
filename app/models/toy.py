# from app import db
# from flask import Blueprint, jsonify

class Toy:
    def __init__(self, name, brand, category):
        self.name = name
        self.brand = brand
        self.category = category
    
    
# toy = [
#     Toy(1, "Mirabel", "telecom"),
#     Toy(2, "Isabella", "Encanto"),
#     Toy(3, "Bruno", "Disney"),
# ]

class User:
    def __init__(self,first,last, email, toys=[]):
        self.first = first
        self.last = last
        self.email = email
        self.toys = toys
    def __init__(self):
        pass
    
    @classmethod   
    def from_json(cls, req_body):
        print(req_body)
        return cls(
            first= req_body["first"],
            last= req_body["last"],
            email= req_body["email"],
            toys= Toy(req_body["name"],req_body["brand"],req_body["category"])
        )    
        
    
    
