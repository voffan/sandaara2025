from flask import render_template
from data.models.pet import Pet
from data.database import db
from settings import app


@app.route("/")
def index():
    pets = db.session.query(Pet).all()
    return render_template('index.html', pets=pets)

@app.route("/pets", methods=["GET", "DELETE"])
def pets_list():
    return "pets list"

@app.route("/petadd", methods=["GET", "POST"])
def pet_add():
    return "pet add"

@app.route("/petedit", methods=["GET", "PATCH"])
def pet_edit():
    return "pet add"

@app.route("/petdonates", methods=["POST"])
def pet_donates():
    return "Pet donated"

@app.route("/my_donates", methods=["GET"])
def my_donates():
    return "my dontes"

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')

@app.route("/logout", methods=["POST"])
def logout():
    return "logout"

@app.route("/me", methods=["GET", "POST"])
def my_profile():
    return "my profile"
