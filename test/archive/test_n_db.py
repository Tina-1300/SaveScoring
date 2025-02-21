from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column

# where /r C:\ "test.db"

db = SQLAlchemy()


app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///links.db"
# initialize the app with the extension
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(unique=True)
    titre: Mapped[str] = mapped_column(String(200))
    section: Mapped[str] = mapped_column(String(100))


with app.app_context():
    db.create_all()

    users = User.query.all()
    print(users)
