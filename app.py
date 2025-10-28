from flask import render_template, redirect, url_for, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.orm import joinedload
from data.models.pet import Pet
from data.models.user import User
from data.models.species import Species
from data.models.donate import Donate
from data.database import db
from settings import app, login_manager


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter(User.id == int(user_id)).first()

@app.route("/")
def index():
    return redirect(url_for('pets_list'))

@app.route("/pets", methods=["GET"])
@app.route("/pets/<msg>", methods=["GET"])
def pets_list(msg=None):
    pets = db.session.query(Pet).all()
    return render_template('pets_list.html', pets=pets, msg=msg)

@app.route("/pet-delete/<int:id>", methods=["POST"])
def pet_delete(id):
    msg = ""
    pet = db.session.query(Pet).filter(Pet.id == id).options(joinedload(Pet.pet_donates)).first()
    if not pet:
        msg += "Питомец не найден!"
    elif current_user.id != pet.owner_id:
        msg += "Вы можете редактировать только своих питомецев!"
    elif len(pet.pet_donates) > 0:
        msg += "Питомецев, у которых есть пожертвования нельзя удалить!"
    else:
        db.session.delete(pet)
        db.session.commit()
    return redirect(url_for('pets_list', msg=msg))

@app.route("/pet-add", methods=["GET", "POST"])
@login_required
def pet_add():
    if request.method == "POST":
        p = Pet()
        p.name = request.form['name']
        p.species_id = int(request.form['species'])
        p.needed = request.form['needed']
        p.owner_id = current_user.id
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('pets_list'))
    species = db.session.query(Species).all()
    return render_template('pet_add.html', species=species)

@app.route("/pet-edit/<int:id>", methods=["GET", "POST"])
@login_required
def pet_edit(id):
    pet = db.session.query(Pet).filter(Pet.id == id).first()
    if not pet:
        msg = "Питомец не найден!"
        return redirect(url_for('pets_list', msg=msg))
    elif current_user.id != pet.owner_id:
        msg = "Вы можете редактировать только своих питомецев!"
        return redirect(url_for('pets_list', msg=msg))
    if request.method == 'POST':
        pet.name = request.form['name']
        pet.species_id = int(request.form['species'])
        pet.needed = request.form['needed']
        db.session.commit()
        return redirect(url_for('pets_list'))
    species = db.session.query(Species).all()
    return render_template('pet_edit.html', pet=pet, species=species)

@app.route("/pet-details/<int:id>", methods=["GET", "POST"])
@login_required
def pet_details(id):
    pet = db.session.query(Pet).filter(Pet.id == id).first()
    if not pet:
        abort(404)
    return render_template('pet_details.html', pet=pet)

@app.route("/pet-donate/<int:id>", methods=["GET","POST"])
@login_required
def pet_donate(id):
    pet = db.session.query(Pet).filter(Pet.id == id).first()
    if not pet:
        msg = "Питомец не найден!"
        return redirect(url_for('pets_list', msg=msg))
    if current_user.id == pet.owner_id:
        msg = "Вы не можете пожертвовать деньги на своих питомецев!"
        return redirect(url_for('pets_list', msg=msg))
    if request.method == 'POST':
        d = Donate()
        d.pet_id = pet.id
        d.donator_id = current_user.id
        d.value = request.form['amount']

        pet.balance += int(request.form['amount'])

        db.session.add(d)
        db.session.commit()
        return redirect(url_for('pets_list'))
    species = db.session.query(Species).all()
    return render_template('pet_donate.html', pet=pet, species=species)

@app.route("/pet-donates", methods=["GET"])
def pet_donates():
    return "Pet donated"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        user = db.session.query(User).filter(User.email == email).first()
        if user and user.password == pwd:
            login_user(user)
            return redirect(url_for('pets_list'))
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
@login_required
def logout():
    logout_user()
    return redirect(url_for('pets_list'))

@app.route("/me", methods=["GET", "POST"])
@login_required
def my_profile():
    return "my profile"

@app.route("/my-donates", methods=["GET"])
@login_required
def my_donates():
    return "my dontes"
