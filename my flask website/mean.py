from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime


with open('config.json.py', 'r') as c:
    params = json.load(c) ["params"]
local_server = True
app = Flask(__name__)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)

class Contacts(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120),  nullable=False)
    date = db.Column(db.String(12),  nullable=True)
    email = db.Column(db.String(25), unique=True, nullable=False)

@app.route("/B")
def home():
     return render_template('index.html',params = params)

@app.route("/about")
def about():
    return render_template('about.html',params = params )
@app.route("/contact",methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):

        name =request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')

        entry = Contacts(name=name ,phone_num=phone,msg=message,email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html',params = params)


app.run(debug=True)