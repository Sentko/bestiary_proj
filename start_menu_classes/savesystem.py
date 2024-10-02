import json
import config



class SaveManagement():
    
    def save_bestiary():
        newjson = input('plz name the savefile - ')
        with open(f'{newjson}.json' , "w") as file:
            json.dump(config.entry_dict, file)
        
    
    def load_save():
        newjson = input('plz gib name of savefile - ')
        with open(f'{newjson}.json', "r") as file:
            config.entry_dict = json.load(file)