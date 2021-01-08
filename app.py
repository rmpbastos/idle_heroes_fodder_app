from flask import Flask, flash, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    """Get data from user to return hero food needs"""

    #if user reached route via POST
    if request.method == "POST":
        
        #Get data from form
        hero = request.form.get("hero")
        stars_start = request.form.get("stars_start")
        stars_end = request.form.get("stars_end")
        

        return render_template("results.html", hero=hero, stars_start=stars_start, stars_end=stars_end)


    #if user reached route via GET
    else:
        return render_template("index.html")