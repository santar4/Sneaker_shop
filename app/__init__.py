from flask import Flask, send_from_directory
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "sdkjl;fgs;dlf"
app.config['UPLOAD_FOLDER'] = 'static/media/'


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "login"



from app.models import User

@login_manager.user_loader
def load_user(user_id: int):
    user = db.session.execute(db.select(User).where(User.id == user_id)).scalar()
    print(user)
    return user

from app.routes import *
from app.filter import *
@app.route("/media/<path:filename>")
def media(filename):
    return send_from_directory("media", filename)