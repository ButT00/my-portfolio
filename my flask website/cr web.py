from flask import Flask, render_template

# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return render_template('index.html')

app = Flask(__name__)
@app.route("/Abdullah")
def hello():
    name = " mirza moon"
    return render_template('index.html' ,name2 = name)
@app.route("/bootstrap")
def bootstrap():

    return render_template('1.png')
app.run(debug=True)