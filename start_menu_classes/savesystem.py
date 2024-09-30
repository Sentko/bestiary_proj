import json
import config



class SaveManagement():
    
    def save_bestiary(menu):
        newjson = input('plz name the savefile - ')
        with open(f'{newjson}.json' , "w") as idk:
            json.dump(config.entry_dict, idk)
        menu()
        
    
    def load_save(menu):                    #load function broken ?
        newjson = input('plz gib name of savefile - ')
        with open(f'{newjson}.json', "r") as George:
            config.entry_dict = json.load(George)
        print('what is happening???')
        menu()