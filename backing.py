from backing_data import hero_10_stars, hero_9_stars, hero_5_stars, hero_5_star_fused, heroes_by_faction

#return the faction of the chosen hero
def find_faction(hero):
    for faction in heroes_by_faction.keys():
        if hero in heroes_by_faction[faction]:
            return faction
