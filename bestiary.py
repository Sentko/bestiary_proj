import config
import utilities
from start_menu_classes.entry import        ECreator
from start_menu_classes.savesystem import   SaveManagement
import utilities.printstatements


def menu_getinput(menu_choice): #Checks validity of menu input and executes corresponding functions
    while True:
        ac_choice = menu_choice.get(input('Your choice -> '))
        if ac_choice is not None:
            break
        print('''Your answer is not valid.
            ''')
    ac_choice()

def load_save_callback():
    SaveManagement.load_save()
    
def save_callback():
    SaveManagement.save_bestiary()
    

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
        SaveManagement.save_bestiary()
        return
    emergency_save = input('''\nYou didn't type 1. You have a second chance if needed.\nType 1 to save your Bestiary before exiting. - ''')
    if emergency_save == '1':
        SaveManagement.save_bestiary()
        return
    exit()

def create_callback(): #Calls create_entry() after an explanation message
    print(utilities.printstatements.entry_creation_explanation)
    ECreator.create_entry()

#def settings():
    #...


def main_menu():
    print(utilities.printstatements.mainmenu_print)
    menu_getinput(pr_menu_acts)
    
def bestiary_printer():
    for i in sorted(config.entry_dict):
        print(f'- {i}'.title())
    #entryvar: str = input("What entry do you want to view ? (press enter without typing to leave to main menu)")
    #entry_printer(entryvar) #should print the entry with its name, category and description
        



pr_menu_acts = {
                '1': load_save_callback,              '2': create_callback, #int:func, int:func
                '3': 'bestiary_printer',              '4':'modify_entry',   #int:func, int:func
                '5': save_callback,                   '6': stop_bestiary,   #int:func, int:func
                '7': 'settings'                                             #int: func
                }