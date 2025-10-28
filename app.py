from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from data.models.pet import Pet
from data.models.user import User
from data.database import db
from settings import app, login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter(User.id == int(user_id)).first()

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
    return "pet edit"

@app.route("/petdonate", methods=["GET","POST"])
def pet_donate():
    return "Pet donated"

@app.route("/petdonates", methods=["GET"])
def pet_donates():
    return "Pet donated"

@app.route("/my_donates", methods=["GET"])
def my_donates():
    return "my dontes"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        user = db.session.query(User).filter(User.email == email).first()
        if user and user.password == pwd:
            login_user(user)
            return redirect(url_for('index'))
        else:
            pass
    return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        u = User()
        u.fullname = request.form['fullname']
        u.nickname = request.form['nickname']
        u.address = request.form['address']
        u.email = request.form['email']
        u.password = request.form['password']
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/me", methods=["GET", "POST"])
def my_profile():
    return "my profile"
