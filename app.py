# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 17:32:25 2022

@author: 23637
"""

from flask import Flask, render_template,request
import joblib
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model = joblib.load("regression")
        r = model.predict([[rates]])
        return render_template("testpage.html",result=r)
    else:
        return render_template("testpage.html",result="WAITING")
if __name__ == "__main__":
    app.run()



