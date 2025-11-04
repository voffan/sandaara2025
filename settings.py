from flask import Flask
from data.database import db, migrate
from flask_admin import Admin
from flask_admin.base import Bootstrap4Theme
from flask_login import LoginManager
from data.models.pet import Pet
from data.models.user import User
from data.models.donate import Donate
from data.models.species import Species
from admin.views import UserView, PetView, DonateView, SpeciesView


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pets.db"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SECRET_KEY'] = 'your-random-secret-key'
app.config['UPLOAD_FOLDER'] = r'static\images\pets'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

db.init_app(app)
migrate.init_app(app, db)
admin = Admin(app, name="Панель администратора", theme=Bootstrap4Theme())

admin.add_view(UserView(User, db.session))
admin.add_view(PetView(Pet, db.session))
admin.add_view(DonateView(Donate, db.session))
admin.add_view(SpeciesView(Species, db.session))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
