import json
import config

entry_cat_desc = {}
category = ""
desc = ""
           

def dict_checker(last_entry): #DEBUGGING
    print(f'This is the current full dictionary :\n{json.dumps(config.entry_dict, indent=4)}')
    print(f'This is the last entry that was added to it :\n{last_entry}')




class ECreator():                 
    def create_entry(): #ISSUE SOMEWHERE, RETAINS CATEGORY AND DESC
        global category
        global desc
        entry_name = input("What is your entry's name ? - ").lower()
        if entry_name in config.entry_dict or entry_name == '':
            entry_name = ECreator.duped_name_denier(entry_name)
            if not entry_name:
                return
        
        ECreator.get_catdesc()                                          #Gets the names of categories and descriptions used in the Entry
        config.entry_dict[entry_name] = entry_cat_desc
        dict_checker(f'{entry_name}, {config.entry_dict[entry_name]}')         #DEBUGGING, Checks state of entry_dict
        ECreator.restart_create_entry()

    def get_catdesc():
        loop_counter = 0
        while True:
            loop_counter += 1
            category = input(f'What is the name of category n°{loop_counter} ? - ')
            desc = input(f'What is the description fit for the category called "{category}" ? - ')
            entry_cat_desc[category] = desc
            continuer = input('Input 1 if you want to add more categories. - ')
            if continuer != "1":
                break
    
    def duped_name_denier(name):
        while True:
            name = input('''
This name already exists within the dictionary, or you did not input a name.
If you do not want to create a new entry, please do not input anything. 
New name : - ''').lower()
            if name not in config.entry_dict:
                return name
                
                
    def restart_create_entry():
        global entry_cat_desc 
        entry_cat_desc = {}
        ecreator_recursor = input('Input 1 to create another different entry. - ')
        if ecreator_recursor == "1":
            ECreator.create_entry()