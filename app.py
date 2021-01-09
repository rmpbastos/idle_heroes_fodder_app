from flask import Flask, flash, jsonify, redirect, render_template, request
from backing import find_faction
from backing_data import hero_10_stars, hero_9_stars, hero_5_stars, hero_5_star_fused, heroes_by_faction

# Configure application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def food():
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
        
        if stars_start == '5':
            if hero in hero_5_stars:
                message_warning = "This hero cannot be further upgraded."
                message_build = False
            else:
                if (hero in hero_9_stars) and (hero not in hero_10_stars):
                    message_warning = "You can build this hero only up to 9 stars."
                else:
                    message_warning = "You can build this hero up to E5."
                message_build = "To build a " + stars_end + " star " + hero + " from " + stars_start + " star shards, you need:"

                #Up to 6 stars
                if stars_end == '6':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (4, 2, 0)
                    message_food = ("* 4 x 5 star " + fac + "\n* 2 x 5 star " + hero)

                message_food = message_food.split("\n")

                used_5star = (sum(fodder_needs))
                used_4star = (used_5star * 8)
                #if initial_5star and initial_4star are provided
                remaining_5star = ((int(initial_5star) + (int(initial_4star) // 8)) - used_5star)
                remaining_4star = (int(initial_4star) - used_4star)

                
                message_food_used = ("This upgrade will use as food:" + "\n4 star heroes: " + str(used_4star) + 
                            "\nor\n5 star heroes: " + str(used_5star))
                message_food_used = message_food_used.split("\n")

                message_food_available = ("Number of foods available after the upgrade: " + 
                            "\n5 star heroes: " + str(remaining_5star))
                message_food_available = message_food_available.split("\n")

        return render_template("results.html", hero=hero, stars_start=stars_start, 
                stars_end=stars_end, initial_4star=initial_4star, initial_5star=initial_5star,
                parcial_available=parcial_available, total_available=total_available, message_warning=message_warning,
                message_build=message_build, message_food=message_food, used_5star=used_5star, used_4star=used_4star,
                remaining_5star=remaining_5star, remaining_4star=remaining_4star, message_food_used=message_food_used,
                message_food_available=message_food_available)

    #if user reached route via GET
    else:
        return render_template("index.html")