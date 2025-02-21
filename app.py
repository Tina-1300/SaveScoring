from flask import Flask
from flask import Flask, request, redirect, url_for, flash
from markupsafe import escape
from flask import render_template
from mxbdd import MXDBB
from crawler import CrawlerRootMe, CrawlerNewbieContest, BaseCrawler
import json
import os
from tasks import BruteForce



# Scripts\activate

data = json.load(open("data/challenges.json"))

# https://bitbelle.wordpress.com/2018/01/10/root-me-web-server-challenge-solutions/

UsersDataBase = MXDBB("users.db")

site_mapping = {"Rootme": CrawlerRootMe, "NewbieContest": CrawlerNewbieContest}

# UsersDataBase.insert_in_data_base("NewbieContest", 0, 0) # Insert a value in a database
# UsersDataBase.insert_in_data_base("Rootme", 0, 0) # insert a value in a database
# UsersDataBase.update_in_data_base_score(86, "NewbieContest") # Update a value in a database


url_root_me = "https://www.root-me.org/Tina-853821"
url_newbiecontest = "https://www.newbiecontest.org/index.php?page=info_membre&id=98720"


app = Flask("tasks")
app.secret_key = os.getenv("SECRET_KEY")
#celery -A tasks:app worker --loglevel=INFO -P gevent


@app.route("/bruteforce_l")
def bruteforce_l():
    return render_template("brute.html")

@app.route("/bruteforce", methods=["POST"])
def brute_force():
    password_a_tester = request.form.get("password") # hash du mot de passe à tester 
    for i in range(0, 1000):
        found_password = BruteForce.delay(password_a_tester, i)
        if found_password.get() != None:
            return render_template("brute.html", found_password=found_password.get())
        



@app.route("/score")
def score():
    scores = UsersDataBase.read_in_data_base()  # Read value in a data base
    return render_template("score.html", scores=scores)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/404")
def error():
    return render_template("error.html")


@app.route("/score/sync", methods=["POST"])
def sync_score():
    site = request.form.get("site")
    cls_crawler = site_mapping.get(site)()
    if site == "Rootme":
        content_page = cls_crawler.request_get_content_source_code_page(url_root_me)
    elif site == "NewbieContest":
        content_page = cls_crawler.request_get_content_source_code_page(
            url_newbiecontest
        )
    else:
        redirect(url_for("error"))
    find_score = cls_crawler.find_score(content_page)
    find_place = cls_crawler.find_place(content_page)
    UsersDataBase.update_in_data_base_score(find_score, site)
    UsersDataBase.update_in_data_base_place(find_place, site)
    flash("The score has been modified")
    return redirect(url_for("score"))


@app.route("/score/allsync", methods=["POST"])
def all_sync():
    for i in data:
        site = i.get("site")
        url = i.get("url")
        cls_crawler = site_mapping.get(site)()
        score = cls_crawler.request_get_content_source_code_page(url)
        find_score = cls_crawler.find_score(score)
        UsersDataBase.update_in_data_base_score(find_score, site)
    flash("The score has been modified")
    return redirect(url_for("score"))


@app.route("/links")
def links():
    return render_template("links.html")


# chaque categorie dois pouvoir stocker (url du site, titre, quelle categorie)
# on ne dois pas afficher l'url du sit on dois afficher le titre quand on click sur le
# titre ça nous redirige vers le site web | et la categorie nous sert à trier les lien
@app.route("/new_save", methods=["POST"])
def new_save():
    category = request.form.get("category")
    print(category)
    return render_template("links.html")


app.run(host="127.0.0.1", port=8000, debug=True)

# https://www.root-me.org/Tina-853821?lang=fr#a782c28c408dd3cd3ff77d79092d2838

# put debug=False when you launch the server in production!!!
# command to turn on the server : python app.py
