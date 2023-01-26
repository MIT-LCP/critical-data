from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import pandas as pd

mentors = pd.read_csv("data/mentors.csv")
partners = pd.read_csv("data/partners.csv")
sch1 = pd.read_csv("data/schedule_day1.csv")
sch2 = pd.read_csv("data/schedule_day2.csv")

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html',
                           n_mentors=len(mentors), mentors=mentors,
                           n_partners=len(partners), partners=partners,
                           n_s1=len(sch1), sch1=sch1,
                           n_s2=len(sch2), sch2=sch2)

if __name__ == '__main__':
    app.run(use_reloader = True, debug=True)