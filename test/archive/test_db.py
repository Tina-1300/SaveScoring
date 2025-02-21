from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column

import random

# where /r C:\ "test.db"

db = SQLAlchemy()
# create the app
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

    # for i in range(9000):

    #     password_length = 10
    #     password_chars = "abcdefghijklmnopqrstuvwxyz"
    #     url = "".join(random.choices(password_chars, k=password_length))
    #     category = ["web", "hacking", "python", "C++", "JavaScript, Python", "Petit coquin"]
    #     category_id = random.randint(0, len(category)-1)
    #     category_aleat = category[category_id]


    #     db.session.add(User(url=f"https://www.{url}.com", titre="Mes sites favorit", section=f"{category_aleat}"))
    #     db.session.commit()

    users = db.session.execute(db.select(User).order_by(User.url)).scalars()
    print(users)



    

    
