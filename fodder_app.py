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

print(heroes_by_faction.values())

hero_A = input('Which hero do you want to build? ')

