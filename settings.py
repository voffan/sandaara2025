from flask import Flask
from data.database import db, migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from data.models.pet import Pet
from data.models.user import User
from data.models.donate import Donate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pets.db"
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db.init_app(app)
migrate.init_app(app, db)
admin = Admin(app, name="Панель администратора", template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Pet, db.session))
admin.add_view(ModelView(Donate, db.session))