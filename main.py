'''
But :
        0) Vérifier si la personne a une sauvegarde
        1) Créer des fiches pour des bêtes/plantes vivantes.
            1.1) Si doublon, prévenir la personne en question
        2) Pouvoir faire une recherche de toutes les espèces déjà existantes
        3) Pouvoir modifier une fiche déjà existante
''' 

def main():
    entry_dict = {'Wolf': {'a': 'a', 'b': 'b'}}
    print('''Welcome to the Ad Infinitum Bestiary.



Press "1" if you want to LOAD a save.                                       [Pas encore implémenté]
Press "2" if you want to CREATE an entry.                                   
Press "3" if you want to LOOK UP all entries that have been written.        [Pas encore implémenté]
Press "4" if you want to MODIFY an already existing entry.                  [Pas encore implémenté]
Press "5" if you want to SAVE your current Bestiary.                        [Pas encore implémenté]
Press "6" if you want to EXIT the Bestiary.                                 
''')
    
    #def load_save():
        #...
        
    def create_entry():
        print('''From there, you will be asked a name for your entry.
After that, you will be asked the name of a category (for example, life expectancy),
Then the description fit for that category (for example, 10 years).
You will finally be asked whether or not you want to make another category.
              
I recommend starting with the most important, as they will be ordered by which
one you decided to input first.

If you make a mistake somewhere, you will be able to modify the entry's category or description later.
              
              
              ''')
        entry_name = input("What is your entry's name ? - ")
        entry_cat_desc = {}
        category = ""
        desc = ""
        loop_counter = 0
        while True:
            loop_counter += 1
            category = input(f'What is the name of category n°{loop_counter} ? - ')
            desc = input(f'What is the description fit for the category called "{category}" ? - ')
            entry_cat_desc[category] = desc
            continuer = input('Input 1 if you want to add more categories. - ')
            if continuer == "1":
                continue
            else : break
        
                
        if entry_name not in entry_dict:
            entry_dict[entry_name] = entry_cat_desc
            print (f'{entry_name}: {entry_dict[entry_name]}')
        else:
            while True:
                entry_name = input("This name already exists within the dictionary. Please choose a new one : - ")
                if entry_name not in entry_dict:
                    entry_dict[entry_name] = entry_cat_desc
                    print(entry_dict)
                    print (f'{entry_name}: {entry_dict[entry_name]}')
                    break
                else:
                    continue
        #input "another entry ?" 
        #if yes recursion
        #else main(). SHOULD MAKE THE MAIN MENU A MENU() FUNC
            
        

    #def search_entry():
        #...
    #def modify_entry():
        #...
    #def overwrite_save():
        #...
    def stop_bestiary():
        exit()
        
    pr_menu_acts = {'1':'load_save',      '2': create_entry, #int:func, int:func
                    '3':'search_entry',   '4':'modify_entry', #int:func, int:func
                    '5':'Sauvegarder',    '6': stop_bestiary}  #int:func, int:func
    
    while True :
        ac_choice = pr_menu_acts.get(input('Your choice -> '))
        if ac_choice is not None:                   
            break                            #Breaks the loop
        print('''Your answer is not valid.
                  ''')
    ac_choice()
            
            
            
if __name__ == '__main__':
    main()