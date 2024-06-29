from flask import Flask
from constants.routes import TEST
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


## models
class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(300), nullable=True)
    block_id = db.Column(db.String(100), nullable=False)
    cdate = db.Column(db.DateTime, default=datetime.now)
    udate = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return "<Card %r>" % self.id
    
class Element(db.Model):
    __tablename__ = "elements"
    id = db.Column(db.Integer, primary_key=True)
    block_id = db.Column(db.String(100), nullable=False)
    cdate = db.Column(db.DateTime, default=datetime.now)
    udate = db.Column(db.DateTime, default=datetime.now)
    text = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return "<Texts %r>" % self.id
     

##routes
@app.route(TEST)
def test():
    return "Hello World!"

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)