from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


engine = create_engine("sqlite:///test.db")
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()







class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'


class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True)
    site = Column(String(100), unique=True)
    score = Column(Integer)

    def __init__(self, site, score):
        self.site = site
        self.score = score

init_db()
