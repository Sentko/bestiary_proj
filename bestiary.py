import json
from start_menu_classes.entry import        ECreator
from start_menu_classes.savesystem import   SaveManagement


def menu_getinput(menu_choice): #Checks validity of menu input and executes corresponding functions
    while True:
        ac_choice = menu_choice.get(input('Your choice -> '))
        if ac_choice is not None:
            break
        print('''Your answer is not valid.
            ''')
    ac_choice()

def load_save_callback():
    SaveManagement.load_save(main_menu)
    
def save_callback():
    SaveManagement.save_bestiary(main_menu)
    

#def search_entry():
    #list_all_entries()             NEEDS DEFINITION
    #show_entry()                   NEEDS DEFINITION

#def modify_entry():
    #list_all_entries()             NEEDS DEFINITION
    #show_entry()                   NEEDS DEFINITION
    #choose_category_to_modify()    NEEDS DEFINITION
    
def stop_bestiary():
    emergency_save = input('Type 1 if you want to save before you leave the Bestiary. - ')
    if emergency_save == '1':
        SaveManagement.save_bestiary(main_menu)
    emergency_save = input('''\nYou didn't type 1. You have a second chance if needed.\nType 1 to save your Bestiary before exiting. - ''')
    if emergency_save == '1':
        SaveManagement.save_bestiary(main_menu)
    exit()

def create_callback(): #Calls create_entry() after an explanation message
    print('''\n\n----------------------------------------------------


From there, you will be asked a name for your entry.
After that, you will be asked the name of a category (for example, life expectancy),
Then the description fit for that category (for example, 10 years).
You will finally be asked whether or not you want to make another category.
              
I recommend starting with the most important, as they will be ordered by which
one you decided to input first.

If you make a mistake somewhere, you will be able to modify the entry's category or description later.
              
              
              ''')
    ECreator.create_entry(main_menu)

#def settings():
    #


def main_menu():
    print('''Welcome to the Ad Infinitum Bestiary.



Press "1" if you want to LOAD a save.                                       
Press "2" if you want to CREATE an entry.                                   
Press "3" if you want to LOOK UP all entries that have been written.        [W.I.P]
Press "4" if you want to MODIFY an already existing entry.                  [W.I.P]
Press "5" if you want to SAVE your current Bestiary.                        
Press "6" if you want to EXIT the Bestiary.                                 
''')
    menu_getinput(pr_menu_acts)


pr_menu_acts = {'1': load_save_callback,              '2': create_callback, #int:func, int:func
                '3':'search_entry',                   '4':'modify_entry',   #int:func, int:func
                '5': save_callback,                   '6': stop_bestiary,   #int:func, int:func
                '7':'settings'}                             #int:func