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
        
        #calculate food needs for each combination start/end
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
                
                #Up to 7 stars
                if stars_end == '7':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (8, 2, 0)
                    message_food = ('***TOTAL***\n* 8 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + '\n***TOTAL***' + 
                            '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac)

                #Up to 8 stars
                if stars_end == '8':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (17, 2, 0)
                    message_food = ('* 11 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                            '\n\n***TOTAL****\n* 17 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + '\n***TOTAL***' +  
                            '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac)
                
                #Up to 9 stars
                if stars_end == '9':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (25, 3, 0)
                    message_food = ('* 13 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 2 x 6 star ' + fac +
                            '\n\n***TOTAL****\n* 25 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n***TOTAL***' +  
                            '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac)
                # #Up to 10 stars
                if stars_end == '10':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (31, 5, 28)
                    message_food = ('* 13 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***TOTAL****\n* 31 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 28 x 5 star (any faction)\n***TOTAL***' +
                            '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)')
                # #Up to E1
                if stars_end == 'E1':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (31, 6, 56)
                    message_food = ('* 13 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 2 x 9 star (any faction)' + 
                            '\n\n***TOTAL****\n* 31 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 56 x 5 star (any faction)\n***TOTAL***' +
                            '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)')
                # #Up to E2
                if stars_end == 'E2':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (31, 7, 84)
                    message_food = ('* 13 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' + 
                            '\n\n***TOTAL****\n* 31 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 84 x 5 star (any faction)\n***TOTAL***' +
                            '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)')
                # #Up to E3
                if stars_end == 'E3':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (31, 7, 148)
                    message_food = ('* 13 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 1 x 10 star (any faction)' + 
                            '\n\n***TOTAL****\n* 31 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 148 x 5 star (any faction)\n***TOTAL***' +
                            '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)')
                # #Up to E4
                if stars_end == 'E4':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (31, 8, 212)
                    message_food = ('* 13 x 5 star ' + fac + '\n* 8 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 2 x 10 star (any faction)' + 
                            '\n\n***TOTAL****\n* 31 x 5 star ' + fac + '\n* 8 x 5 star ' + hero + '\n* 212 x 5 star (any faction)\n***TOTAL***' +
                            '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                            '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')
                # #Up to E5
                if stars_end == 'E5':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (31, 9, 276)
                    message_food = ('* 13 x 5 star ' + fac + '\n* 9 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 3 x 10 star (any faction)' + 
                            '\n\n***TOTAL****\n* 31 x 5 star ' + fac + '\n* 9 x 5 star ' + hero + '\n* 276 x 5 star (any faction)\n***TOTAL***' +
                            '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                            '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                            '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' + 
                            '\n\n***From E4 to E5***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

        if stars_start == '6':
            if hero in hero_5_stars:
                message_warning = "This hero cannot be further upgraded."
                message_build = False
            else:
                if (hero in hero_9_stars) and (hero not in hero_10_stars):
                    message_warning = "You can build this hero only up to 9 stars."
                else:
                    message_warning = "You can build this hero up to E5."
                message_build = "To build a " + stars_end + " star " + hero + " from " + stars_start + " star shards, you need:"

                #Up to 7 stars
                if stars_end == '7':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (4, 0, 0)
                    message_food = ('* 4 x 5 star ' + fac)
                
                #Up to 8 stars
                if stars_end == '8':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (13, 0, 0)
                    message_food = ('* 7 x 5 star ' + fac + '\n* 1 x 6 star ' + fac + 
                            '\n\n***TOTAL***\n* 13 x 5 star ' + fac + '\n***TOTAL***' + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac)

                #Up to 9 stars
                if stars_end == '9':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (21, 1, 0)
                    message_food = ('* 9 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + 
                            '\n\n***TOTAL***\n* 21 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n***TOTAL***' + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac)

                #Up to 10 stars
                if stars_end == '10':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (27, 3, 28)
                    message_food = ('* 9 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +  
                            '\n\n***TOTAL***\n* 27 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 28 x 5 star (any faction)\n***TOTAL***' + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)')

                #Up to E1
                if stars_end == 'E1':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (27, 4, 56)
                    message_food = ('* 9 x 5 star ' + fac + '\n* 4 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 2 x 9 star (any faction)' +  
                            '\n\n***TOTAL***\n* 27 x 5 star ' + fac + '\n* 4 x 5 star ' + hero + '\n* 56 x 5 star (any faction)\n***TOTAL***' + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)')

                #Up to E2
                if stars_end == 'E2':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (27, 5, 84)
                    message_food = ('* 9 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' +  
                            '\n\n***TOTAL***\n* 27 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 84 x 5 star (any faction)\n***TOTAL***' + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)')

                #Up to E3
                if stars_end == 'E3':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (27, 5, 148)
                    message_food = ('* 9 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 1 x 10 star (any faction)'  
                            '\n\n***TOTAL***\n* 27 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 148 x 5 star (any faction)\n***TOTAL***' + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From E2 to E3***\n 1 x 10 star (any faction)')

                #Up to E4
                if stars_end == 'E4':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (27, 6, 212)
                    message_food = ('* 9 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 2 x 10 star (any faction)'  
                            '\n\n***TOTAL***\n* 27 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 212 x 5 star (any faction)\n***TOTAL***' + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                            '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

                #Up to E5
                if stars_end == 'E5':
                    #Define hero faction
                    fac = find_faction(hero)
                    fodder_needs = (27, 7, 276)
                    message_food = ('* 9 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 3 x 10 star (any faction)'  
                            '\n\n***TOTAL***\n* 27 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 276 x 5 star (any faction)\n***TOTAL***' + 
                            '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                            '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                            '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                            '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                            '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                            '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' +
                            '\n\n***From E4 to E5***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')



                

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