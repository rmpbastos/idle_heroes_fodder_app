from flask import Flask, flash, jsonify, redirect, render_template, request
from backing import find_faction
from backing_data import hero_10_stars, hero_9_stars, hero_5_stars, hero_5_star_fused, heroes_by_faction

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
        initial_4star = request.form.get("initial_4star")
        initial_5star = request.form.get("initial_5star")
     
        #Variables passed to the template
        if initial_4star and initial_5star:
            parcial_available = int(initial_4star) // 8
            total_available = parcial_available + int(initial_5star)
        else:
            parcial_available = total_available = 0
        
        return render_template("results.html", hero=hero, stars_start=stars_start, 
                stars_end=stars_end, initial_4star=initial_4star, initial_5star=initial_5star,
                parcial_available=parcial_available, total_available=total_available)

    #if user reached route via GET
    else:
        return render_template("index.html")