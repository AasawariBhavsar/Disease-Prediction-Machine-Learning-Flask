from flask import Flask, render_template, url_for, flash, redirect
from Heart_API.app import heart
import sys
import logging
from Diabetes_API.app import diabetes
app = Flask(__name__, template_folder='templates',static_folder="static")
app.register_blueprint(heart,url_prefix='/heart')
app.register_blueprint(diabetes,url_prefix="/diabetes")

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)