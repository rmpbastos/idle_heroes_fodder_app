#List of heroes that can be upgraded to 10 stars and above
hero_10_stars = ['Tix', 'Ithaqua', 'Gustin', 'Horus', 'Jahra', 'Kamath', 'Corpsedemon', 'Blood Blade', 'Walter', 
                 'Field', 'Kharma', 'Aidan', 'Baade', 'Lutz', 'Dominator', 'Inosuke', 'Sherlock', 'UniMax-3000', 
                 'Penny', 'Xia', 'Valentino', 'Sigmund', 'Flame Strike', 'Emily', 'Ormus', 'OD-01', 'Miki', 'Mirage',
                 'Bleecker', 'Iceblink', 'Honor Guard', 'Morax', 'Ignis', 'Delacium' ,'Nakia', 'Cthugha' ,'King Barton',
                 'Kroos', 'Skerei', 'Barea', 'Dantalian', 'Karim', 'Gusta', 'Fat Mu', 'Lord Balrog', 'Queen', 'Margaret',
                 'Flora', 'Rogan', 'Elyvia', 'Garuda', 'Oberon', 'Valkyrie', 'Heart Watcher', 'Vesa', 'Eddga', 'Rosa', 
                 'Malassa', 'Groo', 'Starlight', 'Faceless', 'Dragon Slayer', 'Demon Hunter', 'Phorcys', 'Drake', 'Carrie',
                 'Amen-Ra', 'Aspen', 'Mihm', 'Amuvor', 'Das Moge', 'Sleepless', 'Dark Arthindol', 'Russell', 'Tara', 'Aida',
                 'Belrain', 'Faith Blade', 'Michelle', 'Asmodel', 'Gerke']

#List of heroes that go up to 9 stars
hero_9_stars = ['Glen', 'Bonecarver', 'Deathsworm', 'Kristian', 'Roy', 'Sierra', 'Norma', 'Destroyer', 'Aleria', 'The Grey-eyed',
                'Zekkis', 'Thale', 'Dark Spirit', 'Divine Spirit']

#List of heroes that go up to 5 stars
hero_5_stars = ['Lamb', 'Bone General', 'Nightmare Knight', 'Gbagbo', 'Grumpy Corpse', 'Iron Bambi', 'LM-02', 'Liquor', 'Storm Hudde',
                'Time Mage', 'Immolatus', 'Lemegeton', 'Akasha', 'Tanner', 'Rogge', 'Kargath', 'Headstriker', 'Ent Elder', 'Chief',
                'Wind Walker', 'Logan', 'Darkness Fanella', 'Fegan', 'Disciple']

#Dictionary of lists containing all 5 star heroes divided by faction
heroes_by_faction = {
    'Shadow': ['Tix', 'Ithaqua', 'Gustin', 'Horus', 'Jahra', 'Kamath', 'Corpsedemon', 'Blood Blade', 'Walter', 
               'Field', 'Kharma', 'Aidan', 'Baade', 'Lutz', 'Dominator', 'Glen', 'Bonecarver', 'Deathsworm',
               'Lamb', 'Bone General', 'Nightmare Knight', 'Gbagbo', 'Grumpy Corpse'],
    'Fortress': ['Inosuke', 'Sherlock', 'UniMax-3000', 'Penny', 'Xia', 'Valentino', 'Sigmund', 'Flame Strike', 
                 'Emily', 'Ormus', 'OD-01', 'Miki', 'Mirage', 'Bleecker', 'Iceblink', 'Honor Guard', 'Kristian', 
                 'Roy', 'Sierra', 'Iron Bambi', 'LM-02', 'Liquor', 'Storm Hudde', 'Time Mage'],
    'Abyss': ['Morax', 'Ignis', 'Delacium' ,'Nakia', 'Cthugha' ,'King Barton', 'Kroos', 'Skerei', 'Barea', 
              'Dantalian', 'Karim', 'Gusta', 'Fat Mu', 'Lord Balrog', 'Queen', 'Margaret', 'Norma', 'Destroyer', 
              'Aleria', 'Immolatus', 'Lemegeton', 'Akasha', 'Tanner', 'Rogge'],
    'Forest': ['Flora', 'Rogan', 'Elyvia', 'Garuda', 'Oberon', 'Valkyrie', 'Heart Watcher', 'Vesa', 'Eddga', 'Rosa', 
               'Malassa', 'Groo', 'Starlight', 'Faceless', 'Dragon Slayer', 'Demon Hunter', 'The Grey-eyed',
               'Zekkis', 'Thale', 'Kargath', 'Headstriker', 'Ent Elder', 'Chief', 'Wind Walker'],
    'Dark': ['Phorcys', 'Drake', 'Carrie', 'Amen-Ra', 'Aspen', 'Mihm', 'Amuvor', 'Das Moge', 'Sleepless', 'Dark Arthindol',
             'Dark Spirit', 'Logan', 'Darkness Fanella'],
    'Light': ['Russell', 'Tara', 'Aida', 'Belrain', 'Faith Blade', 'Michelle', 'Asmodel', 'Gerke', 'Divine Spirit',
              'Fegan', 'Disciple']
}

#Dictionary containing the fodder needs to build a 5 star hero (hero_A is the hero we are building up to E5)
build_5_star = {
    '3_star_same_faction': 4,
    '4_star_same_faction': 6,
    '4_star_hero_A': 2
}

#Dictionary containing the fodder needs to build a 6 star hero
build_6_star = {
    '5_star_same_faction': 4,
    '5_star_hero_A': 2
}

#Dictionary containing the fodder needs to build a 7 star hero
build_7_star = {
    '5_star_same_faction': 4
}

#Dictionary containing the fodder needs to build a 8 star hero
build_8_star = {
    '5_star_same_faction': 3,
    '6_star_same_faction': 1,
}

#Dictionary containing the fodder needs to build a 9 star hero
build_9_star = {
    '5_star_same_faction': 2,
    '5_star_hero_A': 1,
    '6_star_same_faction': 1
}

#Dictionary containing the fodder needs to build a 10 star hero
build_10_star = {
    '5_star_hero_A': 2,
    '6_star_same_faction': 1,
    '9_star_any_faction': 1
}

#Dictionary containing the fodder needs to build an E1
build_E1 = {
    '5_star_hero_A': 1,
    '9_star_any_faction': 1
}

#Dictionary containing the fodder needs to build an E2
build_E2 = {
    '5_star_hero_A': 1,
    '9_star_any_faction': 1
}

#Dictionary containing the fodder needs to build an E3
build_E3 = {
     '10_star_any_faction': 1
}

#Dictionary containing the fodder needs to build an E4
build_E4 = {
    '5_star_hero_A': 1,
    '10_star_any_faction': 1
}

#Dictionary containing the fodder needs to build an E5
build_E5 = {
    '5_star_hero_A': 1,
    '10_star_any_faction': 1
}







'''
hero_A = input('Which hero do you want to build? ')

#Number of heroes available in 3 star shards
hero_shard_3 = input('How many heroes in 3 star shards? ')
print('3 star:', hero_shard_3)

#Number of heroes available in 4 star shards
hero_shard_4 = input('How many heroes in 4 star shards? ')
print('4 star:', hero_shard_4)

#Number of heroes available in 5 star shards
hero_shard_5 = input('How many heroes in 5 star shards? ')
print('5 star:', hero_shard_5)
'''