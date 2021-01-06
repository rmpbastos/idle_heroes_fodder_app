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

#List of heroes that can be fused to 5 stars from 4 stars heroes (no heroes that go 10 stars and beyond can be fused from 4 stars)
hero_5_star_fused = hero_9_stars + hero_5_stars

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



'''***FUNCTIONS***'''

def find_faction(hero):
    for faction in heroes_by_faction.keys():
        if hero in heroes_by_faction[faction]:
            return faction

'''***FUNCTIONS***'''




'''***FODDER NEEDS T0 BUILD A HERO***'''

#Fodder needs to build a hero
hero = 'Sigmund' #later wll be user input
stars_start = '7' #which shards the user will start upgrading from - later wll be user input
stars_end = '8' #upgrade the hero until - later wll be user input
initial_3star = 3200 #number of 3 star in shards owned - later will be user input
initial_4star = 3600 #number of 4 star in shards owned - later will be user input
initial_5star = 125 #number of 5 star in shards owned - later will be user input

print('**********')
print('You can build ' + str(initial_4star // 8) + ' x 5 star heroes with ' + str(initial_4star) + ' shards.')
print('You can have ' + str((initial_4star // 8) + initial_5star) + ' x 5 star heroes.')
print('**********')



'''
TODO
ask how many heroes the user have in shards (3*, 4*, 5*)
show how many 5 star hero the user can build with that amount of shard heroes
from the result of the "start / end", extract the number of heroes needed and subtract from the available heroes

add the amount of gold and spirit needed for the upgrade

later, build a calculator like the TABLE C.2
'''

'''
the fodder_needs variable will have the following tuple structure:
starting at 5 star:
('5 star same fac', n, '5 star hero', n, '5 star any fac', n)
'''

#Staring from 4 stars
if stars_start == '4':
    if hero not in hero_5_star_fused:
        print("This hero doesn't have a 4 star form") #later return 1 and print an error message / maybe add a break point here
    else:
        if (hero in hero_5_stars) and (hero not in hero_9_stars):
            print('You can build this hero only up to 5 stars')
        else:
            print('You can build this hero only up to 9 stars')

    #Up to 5 stars
    if stars_end == '5':
        #Define hero faction
        fac = find_faction(hero)
        message = ('* 4 x 3 star ' + fac + '\n* 6 x 4 star ' + fac + '\n* 2 x 4 star ' + hero)
    
    #Up to 6 stars
    if stars_end == '6':
        #Define hero faction
        fac = find_faction(hero)
        message = ('***From 4 to 5*** (Here we need to build 2 x 5 star copies of the desired hero)\n* 8 x 3 star ' + fac + '\n* 12 x 4 star ' + fac + '\n* 4 x 4 star ' + hero + 
                '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac)
    
    #Up to 7 stars
    if stars_end == '7':
        #Define hero faction
        fac = find_faction(hero)
        message = ('***TOTAL***\n* 8 x 3 star ' + fac + '\n* 12 x 4 star ' + fac + '\n* 4 x 4 star ' + hero +
                '\n* 8 x 5 star ' + fac + '\n***TOTAL***' +
                '\n\n***From 4 to 5*** (Here we need to build 2 x 5 star copies of the desired hero)\n* 8 x 3 star ' + fac + '\n* 12 x 4 star ' + fac + '\n* 4 x 4 star ' + hero + 
                '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + 
                '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac)

    #Up to 8 stars
    if stars_end == '8':
        #Define hero faction
        fac = find_faction(hero)
        message = ('* 8 x 3 star ' + fac + '\n* 12 x 4 star ' + fac + '\n* 4 x 4 star ' + hero +
                '\n* 11 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                '\n\n***TOTAL***\n* 8 x 3 star ' + fac + '\n* 12 x 4 star ' + fac + '\n* 4 x 4 star ' + hero +
                '\n* 17 x 5 star ' + fac + '\n***TOTAL***' +
                '\n\n***From 4 to 5*** (Here we need to build 2 x 5 star copies of the desired hero)\n* 8 x 3 star ' + fac + '\n* 12 x 4 star ' + fac + '\n* 4 x 4 star ' + hero + 
                '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + 
                '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac + 
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac)
    
    #Up to 9 stars
    if stars_end == '9':
        #Define hero faction
        fac = find_faction(hero)
        message = ('* 8 x 3 star ' + fac + '\n* 12 x 4 star ' + fac + '\n* 4 x 4 star ' + hero +
                '\n* 13 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + 
                '\n\n***TOTAL***\n* 8 x 3 star ' + fac + '\n* 12 x 4 star ' + fac + '\n* 4 x 4 star ' + hero +
                '\n* 19 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n***TOTAL***' + 
                '\n\nFrom 4 to 5*** (Here we need to build 2 x 5 star copies of the desired hero)\n* 8 x 3 star ' + fac + '\n* 12 x 4 star ' + fac + '\n* 4 x 4 star ' + hero + 
                '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + 
                '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac + 
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac + 
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac)

#Starting from 5 stars
if stars_start == '5':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to 6 stars
    if stars_end == '6':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (4, 2, 0)
        message = ('* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero)

    #Up to 7 stars
    if stars_end == '7':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (8, 2, 0)
        message = ('***TOTAL***\n* 8 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + '\n***TOTAL***' + 
                '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac)

    #Up to 8 stars
    if stars_end == '8':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (17, 2, 0)
        message = ('* 11 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                '\n\n***TOTAL****\n* 17 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + '\n***TOTAL***' +  
                '\n\n***From 5 to 6***\n* 4 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + 
                '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac)

    #Up to 9 stars
    if stars_end == '9':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (25, 3, 0)
        message = ('* 13 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 2 x 6 star ' + fac +
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
        message = ('* 13 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' + 
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
        message = ('* 13 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 2 x 9 star (any faction)' + 
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
        message = ('* 13 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' + 
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
        message = ('* 13 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 1 x 10 star (any faction)' + 
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
        message = ('* 13 x 5 star ' + fac + '\n* 8 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 2 x 10 star (any faction)' + 
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
        message = ('* 13 x 5 star ' + fac + '\n* 9 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 3 x 10 star (any faction)' + 
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

#Starting from 6 stars
if stars_start == '6':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to 7 stars
    if stars_end == '7':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (4, 0, 0)
        message = ('* 4 x 5 star ' + fac)

    #Up to 8 stars
    if stars_end == '8':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (13, 0, 0)
        message = ('* 7 x 5 star ' + fac + '\n* 1 x 6 star ' + fac + 
                '\n\n***TOTAL***\n* 13 x 5 star ' + fac + '\n***TOTAL***' + 
                '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac)

    #Up to 9 stars
    if stars_end == '9':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (21, 1, 0)
        message = ('* 9 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + 
                '\n\n***TOTAL***\n* 21 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n***TOTAL***' + 
                '\n\n***From 6 to 7***\n* 4 x 5 star ' + fac +
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac)

    #Up to 10 stars
    if stars_end == '10':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (27, 3, 28)
        message = ('* 9 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +  
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
        message = ('* 9 x 5 star ' + fac + '\n* 4 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 2 x 9 star (any faction)' +  
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
        message = ('* 9 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' +  
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
        message = ('* 9 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 1 x 10 star (any faction)'  
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
        message = ('* 9 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 2 x 10 star (any faction)'  
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
        message = ('* 9 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 3 x 10 star (any faction)'  
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

#Starting from 7 stars
if stars_start == '7':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to 8 stars
    if stars_end == '8':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (9, 0, 0)
        message = ('* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                '\n\n***TOTAL***\n* 9 x 5 star ' + fac + '\n***TOTAL***')

    #Up to 9 stars
    if stars_end == '9':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (17, 1, 0)
        message = ('* 5 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + 
                '\n\n***TOTAL***\n* 17 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n***TOTAL***' + 
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac)

    #Up to 10 stars
    if stars_end == '10':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (23, 3, 28)
        message = ('* 5 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***TOTAL***\n* 23 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 28 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)')

    #Up to E1
    if stars_end == 'E1':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (23, 4, 56)
        message = ('* 5 x 5 star ' + fac + '\n* 4 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 2 x 9 star (any faction)' +
                '\n\n***TOTAL***\n* 23 x 5 star ' + fac + '\n* 4 x 5 star ' + hero + '\n* 56 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)') 

    #Up to E2
    if stars_end == 'E2':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (23, 5, 84)
        message = ('* 5 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' +
                '\n\n***TOTAL***\n* 23 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 84 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)') 

    #Up to E3
    if stars_end == 'E3':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (23, 5, 148)
        message = ('* 5 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' + '\n* 1 x 10 star (any faction)'
                '\n\n***TOTAL***\n* 23 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 148 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)')

    #Up to E4
    if stars_end == 'E4':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (23, 6, 212)
        message = ('* 5 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' + '\n* 2 x 10 star (any faction)'
                '\n\n***TOTAL***\n* 23 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 212 x 5 star (any faction)\n***TOTAL***' + 
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
        fodder_needs = (23, 7, 276)
        message = ('* 5 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 3 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' + '\n* 3 x 10 star (any faction)'
                '\n\n***TOTAL***\n* 23 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 276 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 7 to 8***\n* 3 x 5 star ' + fac + '\n* 1 x 6 star ' + fac +
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' +
                '\n\n***From E4 to E5***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

#Starting from 8 stars
if stars_start == '8':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to 9 stars
    if stars_end == '9':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (8, 1, 0)
        message = ('* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                '\n\n***TOTAL\n* 8 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n***TOTAL***')

    #Up to 10 stars
    if stars_end == '10':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (14, 3, 28)
        message = ('* 2 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***TOTAL***\n* 14 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 28 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)')

    #Up to E1
    if stars_end == 'E1':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (14, 4, 56)
        message = ('* 2 x 5 star ' + fac + '\n* 4 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + '\n* 2 x 9 star (any faction)' +
                '\n\n***TOTAL***\n* 14 x 5 star ' + fac + '\n* 4 x 5 star ' + hero + '\n* 56 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)')

    #Up to E2
    if stars_end == 'E2':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (14, 5, 84)
        message = ('* 2 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' +
                '\n\n***TOTAL***\n* 14 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 84 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)') 

    #Up to E3
    if stars_end == 'E3':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (14, 5, 148)
        message = ('* 2 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' + '\n* 1 x 10 star (any faction)' + 
                '\n\n***TOTAL***\n* 14 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 148 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)')

    #Up to E4
    if stars_end == 'E4':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (14, 6, 212)
        message = ('* 2 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' + '\n* 2 x 10 star (any faction)' + 
                '\n\n***TOTAL***\n* 14 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 212 x 5 star (any faction)\n***TOTAL***' + 
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
        fodder_needs = (14, 7, 276)
        message = ('* 2 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 2 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' + '\n* 3 x 10 star (any faction)' + 
                '\n\n***TOTAL***\n* 14 x 5 star ' + fac + '\n* 7 x 5 star ' + hero + '\n* 276 x 5 star (any faction)\n***TOTAL***' + 
                '\n\n***From 8 to 9***\n* 2 x 5 star ' + fac + '\n* 1 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + 
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' +
                '\n\n***From E4 to E5***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

#Starting from 9 stars
if stars_start == '9':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to 10 stars
    if stars_end == '10':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (6, 2, 28)
        message = ('* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' + 
                '\n\n***TOTAL\n* 6 x 5 star ' + fac + '\n* 2 x 5 star ' + hero + '\n* 28 x 5 star (any faction)\n***TOTAL***')

    #Up to E1
    if stars_end == 'E1':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (6, 3, 56)
        message = ('* 3 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 2 x 9 star (any faction)' +
                '\n\n***TOTAL\n* 6 x 5 star ' + fac + '\n* 3 x 5 star ' + hero + '\n* 56 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)')

    #Up to E2
    if stars_end == 'E2':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (6, 4, 84)
        message = ('* 4 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 3 x 9 star (any faction)' +
                '\n\n***TOTAL\n* 6 x 5 star ' + fac + '\n* 4 x 5 star ' + hero + '\n* 84 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)') 

    #Up to E3
    if stars_end == 'E3':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (6, 4, 148)
        message = ('* 4 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 1 x 10 star (any faction)' +
                '\n\n***TOTAL\n* 6 x 5 star ' + fac + '\n* 4 x 5 star ' + hero + '\n* 148 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)')

    #Up to E4
    if stars_end == 'E4':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (6, 5, 212)
        message = ('* 5 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 2 x 10 star (any faction)' +
                '\n\n***TOTAL\n* 6 x 5 star ' + fac + '\n* 5 x 5 star ' + hero + '\n* 212 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

    #Up to E5
    if stars_end == 'E5':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (6, 6, 276)
        message = ('* 6 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 3 x 9 star (any faction)\n* 3 x 10 star (any faction)' +
                '\n\n***TOTAL\n* 6 x 5 star ' + fac + '\n* 6 x 5 star ' + hero + '\n* 276 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From 9 to 10***\n* 2 x 5 star ' + hero + '\n* 1 x 6 star ' + fac + '\n* 1 x 9 star (any faction)' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' +
                '\n\n***From E4 to E5***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

#Starting from 10 stars
if stars_start == '10':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to E1
    if stars_end == 'E1':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 1, 28)
        message = ('* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***TOTAL\n* 1 x 5 star ' + hero + '\n* 28 x 5 star (any faction)\n***TOTAL***')

    #Up to E2
    if stars_end == 'E2':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 2, 56)
        message = ('* 2 x 5 star ' + hero + '\n* 2 x 9 star (any faction)' + 
                '\n\n***TOTAL\n* 2 x 5 star ' + hero + '\n* 56 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)') 

    #Up to E3
    if stars_end == 'E3':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 2, 120)
        message = ('* 2 x 5 star ' + hero + '\n* 2 x 9 star (any faction)\n* 1 x 10 star (any faction)' + 
                '\n\n***TOTAL\n* 2 x 5 star ' + hero + '\n* 120 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)') 

    #Up to E4
    if stars_end == 'E4':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 3, 184)
        message = ('* 3 x 5 star ' + hero + '\n* 2 x 9 star (any faction)\n* 2 x 10 star (any faction)' + 
                '\n\n***TOTAL\n* 3 x 5 star ' + hero + '\n* 184 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

    #Up to E5
    if stars_end == 'E5':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 4, 248)
        message = ('* 4 x 5 star ' + hero + '\n* 2 x 9 star (any faction)\n* 3 x 10 star (any faction)' + 
                '\n\n***TOTAL\n* 4 x 5 star ' + hero + '\n* 248 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From 10 to E1***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' +
                '\n\n***From E4 to E5***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

#Starting from E1
if stars_start == 'E1':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to E2
    if stars_end == 'E2':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 1, 28)
        message = ('* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***TOTAL\n* 1 x 5 star ' + hero + '\n* 28 x 5 star (any faction)\n***TOTAL***')

    #Up to E3
    if stars_end == 'E3':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 1, 92)
        message = ('* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)\n* 1 x 10 star (any function)' + 
                '\n\n***TOTAL\n* 1 x 5 star ' + hero + '\n* 92 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)') 

    #Up to E4
    if stars_end == 'E4':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 2, 156)
        message = ('* 2 x 5 star ' + hero + '\n* 1 x 9 star (any faction)\n* 2 x 10 star (any function)' + 
                '\n\n***TOTAL\n* 2 x 5 star ' + hero + '\n* 156 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

    #Up to E5
    if stars_end == 'E5':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 3, 220)
        message = ('* 3 x 5 star ' + hero + '\n* 1 x 9 star (any faction)\n* 3 x 10 star (any function)' + 
                '\n\n***TOTAL\n* 3 x 5 star ' + hero + '\n* 220 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From E1 to E2***\n* 1 x 5 star ' + hero + '\n* 1 x 9 star (any faction)' + 
                '\n\n***From E2 to E3***\n 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' +
                '\n\n***From E4 to E5***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

#Starting from E2
if stars_start == 'E2':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to E3
    if stars_end == 'E3':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 0, 64)
        message = ('* 1 x 10 star (any faction)' + 
                '\n\n***TOTAL\n* 64 x 5 star (any faction)\n***TOTAL***')

    #Up to E4
    if stars_end == 'E4':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 1, 128)
        message = ('* 1 x 5 star ' + hero + '\n* 2 x 10 star (any faction)' + 
                '\n\n***TOTAL\n* 1 x 5 star ' + hero + '\n* 128 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

    #Up to E5
    if stars_end == 'E5':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 2, 192)
        message = ('* 2 x 5 star ' + hero + '\n* 3 x 10 star (any faction)' + 
                '\n\n***TOTAL\n* 2 x 5 star ' + hero + '\n* 192 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From E2 to E3***\n* 1 x 10 star (any faction)' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' + 
                '\n\n***From E4 to E5***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

#Starting from E3
if stars_start == 'E3':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to E4
    if stars_end == 'E4':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0, 1, 64)
        message = ('* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' + 
                '\n\n***TOTAL\n* 1 x 5 star ' + hero + '\n* 64 x 5 star (any faction)\n***TOTAL***')

    #Up to E5
    if stars_end == 'E5':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0 ,1 ,128)
        message = ('* 2 x 5 star ' + hero + '\n* 2 x 10 star (any faction)' + 
                '\n\n***TOTAL\n* 2 x 5 star ' + hero + '\n* 128 x 5 star (any faction)\n***TOTAL***' +
                '\n\n***From E3 to E4***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' +
                '\n\n***From E4 to E5***\n* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)')

#Starting from E4
if stars_start == 'E4':
    if hero in hero_5_stars:
        print('This hero cannot be further upgraded.')
    else:
        if (hero in hero_9_stars) and (hero not in hero_10_stars):
            print('You can build this hero only up to 9 stars.')
        else:
            print('You can build this hero up to E5.') 

    #Up to E5
    if stars_end == 'E5':
        #Define hero faction
        fac = find_faction(hero)
        fodder_needs = (0 ,1 ,64)
        message = ('* 1 x 5 star ' + hero + '\n* 1 x 10 star (any faction)' + 
                '\n\n***TOTAL\n* 1 x 5 star ' + hero + '\n* 64 x 5 star (any faction)\n***TOTAL***')

#amount of 4 and 5 star heroes used in the upgrade
used_5star = (sum(fodder_needs))
used_4star = (used_5star * 8)

#remaining 4 and 5 star heroes after the upgrade
remaining_5star = ((initial_5star + (initial_4star // 8)) - used_5star)
remaining_4star = (initial_4star - used_4star)

#Show amount of heroes to be used and the remaining amount after the upgrade
print('**********')
print('This upgrade will use as food:' +
    '\n4 star heroes: ' + str(used_4star) + '\nor' +
    '\n5 star heroes: ' + str(used_5star))
print('**********')

print('\nNumber of foods available after the upgrade: ' +
    '\n5 star heroes: ' +  str(remaining_5star))
print('**********')


#Show necessary fodder
print('\nTo build a ' + stars_end + ' star ' + hero + ' from ' + stars_start + ' star shards, you need:')
print(message)
    


'''***FODDER NEEDS T0 BUILD A HERO***'''












#List of tuples containing the fodder needs to build a 5 star hero (hero_A is the hero we are building up to E5)
build_5_star = [('3_star_same_faction', 4), ('4_star_same_faction', 6), ('4_star_hero_A', 2)]

#List of tuplescontaining the fodder needs to build a 6 star hero
build_6_star = [('5_star_same_faction', 4), ('5_star_hero_A', 2)]

#List of tuples containing the fodder needs to build a 7 star hero
build_7_star = [('5_star_same_faction', 4)]

#List of tuples containing the fodder needs to build a 8 star hero
build_8_star = [('5_star_same_faction', 3), ('6_star_same_faction', 1)]

#List of tuples containing the fodder needs to build a 9 star hero
build_9_star = [('5_star_same_faction', 2), ('5_star_hero_A', 1), ('6_star_same_faction', 1)]

#List of tuples containing the fodder needs to build a 10 star hero
build_10_star = [('5_star_hero_A', 2), ('6_star_same_faction', 1), ('9_star_any_faction', 1)]

#List of tuples containing the fodder needs to build an E1
build_E1 = [('5_star_hero_A', 1), ('9_star_any_faction', 1)]

#List of tuples containing the fodder needs to build an E2
build_E2 = [('5_star_hero_A', 1), ('9_star_any_faction', 1)]

#List of tuples containing the fodder needs to build an E3
build_E3 = [('10_star_any_faction', 1)]

#List of tuples containing the fodder needs to build an E4
build_E4 = [('5_star_hero_A', 1), ('10_star_any_faction', 1)]

#List of tuples containing the fodder needs to build an E5
build_E5 = [('5_star_hero_A', 1), ('10_star_any_faction', 1)]

total_build = [build_5_star, build_6_star, build_7_star, build_8_star, build_9_star, build_10_star, 
            build_E1, build_E2, build_E3, build_E4, build_E5]

#Fodder needs to build an E5 (not counting the needs of "fodders of fodders")
totals = {}
for t in total_build:
  for key, value in t:
    totals[key] = totals.get(key, 0) + value

'''
{'10_star_any_faction': 3,
 '3_star_same_faction': 4,
 '4_star_hero_A': 2,
 '4_star_same_faction': 6,
 '5_star_hero_A': 9,
 '5_star_same_faction': 13,
 '6_star_same_faction': 3,
 '9_star_any_faction': 3}
 '''













'''
Probably won't use it. Trying to do the same thing but, instead of dicts, I will try with tuples.

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

#total_build = [build_5_star, build_6_star, build_7_star, build_8_star, build_9_star, build_10_star, 
#                build_E1, build_E2, build_E3, build_E4, build_E5]


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