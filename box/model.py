from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class BoxModel(db.Model):
    __tablename__ = "Box"
 
    id = db.Column(db.Integer, primary_key=True)
    box_id = db.Column(db.Integer(),unique = True)
    name_box = db.Column(db.String(80))
    size_box = db.Column(db.String(80))
    description_box = db.Column(db.String())
 
    def __init__(self, box_id,name_box,size_box,description_box):
        self.box_id = box_id
        self.name_box = name_box
        self.size_box = size_box
        self.description_box = description_box
 
    def __repr__(self):
        return f"{self.name_box}:{self.box_id}"