from flask_sqlalchemy import SQLAlchemy
from data.models.base import BaseModel
from flask_migrate import Migrate


db = SQLAlchemy(model_class=BaseModel)
migrate = Migrate()