from flask import Flask, render_template, url_for
import sqlalchemy
from datetime import datetime
import pandas as pd 
import numpy as np
import os 

app = Flask(__name__)

directory = "static/CSV Files/"
csv_dict = {}

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        csv_dict[filename] = np.asarray(pd.read_csv(directory + filename)).tolist()


#@app.route('/')
#def index():
#    return render_template('home.html', redflaglinkw = 'redflagquizw', greenflaglinkw = 'redflagquizw')

@app.route('/') #redflagquiz
def redflagquizm():
    return render_template('start.html',nextlink='appearance')

@app.route('/appearance')
def appearance():
    return render_template('index.html',itemlist=csv_dict['Quiz Categories - Appearance_grooming.csv'],nextlink='career',category="Appearance/Grooming")

@app.route('/career')
def career():
    return render_template('index.html',itemlist=csv_dict['Quiz Categories - Career_Professional.csv'],nextlink='emotional',category="Career/Professional")

@app.route('/emotional')
def emotional():
    return render_template('index.html',itemlist=csv_dict['Quiz Categories - Emotional Intelligence.csv'],nextlink='living',category="Emotional Intelligence")

@app.route('/living')
def living():
    return render_template('index.html',itemlist=csv_dict['Quiz Categories - Living.csv'],nextlink='mental',category="Living")

@app.route('/mental')
def mental():
    return render_template('index.html',itemlist=csv_dict['Quiz Categories - Mental Health.csv'],nextlink='quirks',category="Mental Health")

@app.route('/quirks')
def quirks():
    return render_template('index.html',itemlist=csv_dict['Quiz Categories - Quirks.csv'],nextlink='social',category="Quirks")

@app.route('/social')
def social():
    return render_template('index.html',itemlist=csv_dict['Quiz Categories - Social.csv'],nextlink='end',category="Social")

@app.route('/end')
def end():
    return render_template('end.html',nextlink='redflagquizm')



if __name__ == "__main__":
    app.run(debug=True)