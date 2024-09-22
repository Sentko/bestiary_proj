def create_entry(): #Function that creates entries
    entry_name = input("What is your entry's name ? - ").lower()
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
        if continuer != "1":
            break
    
            
    if entry_name not in entry_dict:
        entry_dict[entry_name] = entry_cat_desc
        print (f'{entry_name}: {entry_dict[entry_name]}')
    else:
        while True:
            entry_name = input("This name already exists within the dictionary. Please choose a new one : - ").lower()
            if entry_name in entry_dict:
                continue
            entry_dict[entry_name] = entry_cat_desc
            print(entry_dict)
            print (f'{entry_name}: {entry_dict[entry_name]}')
            break
            
    entry_recursor = input('Input 1 to create another different entry. - ')
    if entry_recursor == "1":
        create_entry()
    main_menu()


entry_dict = {}

#def load_save():
        #...
 #def search_entry():
    #...
#def modify_entry():
    #...
#def overwrite_save():
    #...
def stop_bestiary():
    exit()

def create_callback(): #Calls create_entry()
    print('''From there, you will be asked a name for your entry.
After that, you will be asked the name of a category (for example, life expectancy),
Then the description fit for that category (for example, 10 years).
You will finally be asked whether or not you want to make another category.
              
I recommend starting with the most important, as they will be ordered by which
one you decided to input first.

If you make a mistake somewhere, you will be able to modify the entry's category or description later.
              
              
              ''')
    create_entry()
        





pr_menu_acts = {'1':'load_save',      '2': create_callback, #int:func, int:func
                '3':'search_entry',   '4':'modify_entry', #int:func, int:func
                '5':'save',           '6': stop_bestiary}  #int:func, int:func

def main_menu():
        print('''Welcome to the Ad Infinitum Bestiary.



Press "1" if you want to LOAD a save.                                       [Pas encore implémenté]
Press "2" if you want to CREATE an entry.                                   
Press "3" if you want to LOOK UP all entries that have been written.        [Pas encore implémenté]
Press "4" if you want to MODIFY an already existing entry.                  [Pas encore implémenté]
Press "5" if you want to SAVE your current Bestiary.                        [Pas encore implémenté]
Press "6" if you want to EXIT the Bestiary.                                 
''')
        while True :
            ac_choice = pr_menu_acts.get(input('Your choice -> '))
            if ac_choice is not None:                   
                break
            print('''Your answer is not valid.
                  ''')
        ac_choice()