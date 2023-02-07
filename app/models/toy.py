# from app import db
# from flask import Blueprint, jsonify

class Toy:
    def __init__(self, name, brand, category, imageurl, description, owner_email, owner_first, owner_last):
        self.name = name
        self.brand = brand
        self.category = category
        self.imageurl = imageurl
        self.description = description
        self.owner_email = owner_email
        self.owner_first = owner_first
        self.owner_last = owner_last
    
    
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
            toys= Toy(req_body["name"],req_body["brand"],req_body["category"]
                    ,req_body["imageurl"],req_body["description"]
                    ,req_body["owner_email"],req_body["owner_first"],req_body["owner_last"])
        )    
        
    
    
