from flask import Flask, render_template, redirect, url_for, request, session
from constants.routes import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from constants.database import *
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)


## models
class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    subText = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=True)
    icon = db.Column(db.Text, nullable=True)
    block_id = db.Column(db.String(100), nullable=False)
    cdate = db.Column(db.DateTime, default=datetime.now)
    udate = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return "<Card %r>" % self.title + str(self.id)
    
class Element(db.Model):
    __tablename__ = "elements"
    id = db.Column(db.Integer, primary_key=True)
    block_id = db.Column(db.String(100), nullable=False)
    cdate = db.Column(db.DateTime, default=datetime.now)
    udate = db.Column(db.DateTime, default=datetime.now)
    text = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=True)
    subText = db.Column(db.Text, nullable=True)
    name = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return "<Texts %r>" % self.id
     
class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(300), nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<Admin %r>" % self.id
     
##routes
@app.route(TEST)
def test():    
    # bytes = "adminruben15082006".encode('utf-8') 
    # salt = bcrypt.gensalt() 
    # hash = bcrypt.hashpw(bytes, salt) 
    
    # admin = Admin(username="admin", password=hash)
    # db.session.add(admin)
    # db.session.commit()
    
    
    # card = Card(title="HTML/CSS", 
    #         text="html and css are technologies that I have been using and learning since I started my programming journey. They seem to be everywhere, so I've used them in almost every project I've made.",
    #         block_id=SKILLS)
    # db.session.add(card)
    # card = Card(title="Javascript", 
    #             text="I started learning JavaScript after I learned HTML and CSS. I noticed that I liked it a little more and started making games. My experience, which I gained on my own, helped me easily pass the programming course at TUMO.",
    #             block_id=SKILLS)
    # db.session.add(card)
    # card = Card(title="React JS", 
    #             text="The next step was Reactjs, in my opinion the most brilliant thing people could create. In fact, I've been studying this technology longer than anything else. Actually my best project is Kinder and its frontend part was written in React js using redux.",
    #             block_id=SKILLS)
    # db.session.add(card)

    # card = Card(title="Kinder", 
    #             text="kinder is a social webiste, where you can chat with your friends, post photos and more!",
    #             block_id=PROJECTS,
    #             subText="technologies that were used: React JS, Node JS, Express JS, Redux, JWT, Passport JS",
    #             url="https://github.com/RubenKarapetyann/kinder")
    # db.session.add(card)
    # card = Card(title="Shop", 
    #         text="online shop!",
    #         block_id=PROJECTS,
    #         subText="technologies that were used: React JS",
    #         url="https://github.com/RubenKarapetyann/shop")
    # db.session.add(card)
    
    # card = Card(title="Apple", 
    #         text="one year experience",
    #         block_id=EXPERIENCE)
    # db.session.add(card)
    
    # card = Card(title="github", 
    #         text="my github",
    #         block_id=CONTACTS,
    #         url="https://github.com/RubenKarapetyann",
    #         icon="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z")
    # db.session.add(card)
    
        
    # card = Card(title="linked in", 
    #         text="my linked in",
    #         block_id=CONTACTS,
    #         url="https://www.linkedin.com/in/ruben-karapetyan-6a67b7279",
    #         icon="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z")
    # db.session.add(card)
    
    
    # element = Element(block_id=INTRODUCTION, text="Tell me and I forget, teach me and I may remember, involve me and I learn.", name="quote")
    # db.session.add(element)
    # element = Element(block_id=INTRODUCTION, text="17 years", subText="old", name="secondary_info")
    # db.session.add(element)
    # element = Element(block_id=ABOUT, text="Hello, it's me Ruben! I have been studying web technologies and more since I was 14 years old. I have made many interesting projects that I will be glad to show you below. I can say about myself that I love learning something new and communicating with people!", name="about")
    # db.session.add(element)
    # element = Element(block_id=ABOUT, text="Born in", subText="Yerevan", name="fact_1")
    # db.session.add(element)
    # element = Element(block_id=ABOUT, text="Born on", subText="15 August 2006", name="fact_2")
    # db.session.add(element)
    # element = Element(block_id=ABOUT, text="Nationality", subText="Armenian", name="fact_3")
    # db.session.add(element)    
    # db.session.commit()
    return "done"

@app.route(INDEX)
def index():
    skills = db.session.execute(db.select(Card).filter_by(block_id=SKILLS)).scalars()
    projects = db.session.execute(db.select(Card).filter_by(block_id=PROJECTS)).scalars()
    experience = db.session.execute(db.select(Card).filter_by(block_id=EXPERIENCE)).scalars()
    contacts = db.session.execute(db.select(Card).filter_by(block_id=CONTACTS)).scalars()
    elements = Element.query.all()
    return render_template("portfolio.html", skills=skills, projects=projects, experience=experience, contacts=contacts, elements=elements)

@app.route(ADMIN_LOGIN, methods=["GET", "POST"])
def admin_login():
    if "username" in session:
        return redirect(url_for(ADMIN[1:]))
    if request.method == "POST":
        username = request.form["username"]   
        admin = Admin.query.filter_by(username=username).first()
        if not admin:
            return redirect(url_for("admin_login"))
        
        userPassword = request.form["password"]
        userBytes = userPassword.encode("utf-8")
        if not bcrypt.checkpw(userBytes, admin.password):
            return redirect(url_for("admin_login"))
            
        session["username"] = username
        return redirect(url_for(ADMIN[1:]))
        
    return render_template("admin_login.html")

@app.route(ADMIN)
def admin():
    if "username" in session:
        return render_template("admin.html")
    return redirect(url_for("admin_login"))
        
@app.route(LOGOUT)
def logout():
    session.pop("username", None)
    return redirect(url_for("admin_login"))


@app.route(CREATE, methods=["GET", "POST"])
def create(section):
    if "username" not in session:
        return redirect(url_for("admin_login"))
    
    if section not in SECTIONS:
        return redirect(url_for(ADMIN[1:]))

    if request.method == "POST":
        return "done"
    
    return render_template("create.html")


@app.route(SECTION)
def section(section):
    if "username" not in session:
        return redirect(url_for("admin_login"))

    if section not in SECTIONS:
        return redirect(url_for(ADMIN[1:])) 
    
    items = []
    try:
        if section in ELEMENTS:
            items = db.session.execute(db.select(Element).filter_by(block_id=section)).scalars()
        else:
            items = db.session.execute(db.select(Card).filter_by(block_id=section)).scalars()
    except:
        pass
        
    return render_template("section.html", items=items, section=section, need_button=(section in CARDS))

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
