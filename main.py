'''
But :
        0) Vérifier si la personne a une sauvegarde
        1) Créer des fiches pour des bêtes/plantes vivantes.
            1.1) Si doublon, prévenir la personne en question
        2) Pouvoir faire une recherche de toutes les espèces déjà existantes
        3) Pouvoir modifier une fiche déjà existante
        
        

    ENTRY : 
        - Nom commun = STR
        - Nom officiel = STR
        - Race = STR
        - Habitat naturel = STR
        - Description physique = STR
        - Espérance de vie estimée = INT
        - Régime = STR 
            - Si carnivore : Techniques de chasse emblématiques STR
        - Comportement social = STR
''' 

def __main__():
    entry_dict = {}
    print('''Bonjour ! Bienvenue dans le Bestiaire Ad Infinitum.



Tapez "1" si vous avez une SAUVEGARDE.                                      [Pas encore implémenté]
Tapez "2" si vous voulez CRÉER une fiche.                                   [Pas encore implémenté]
Tapez "3" si vous voulez faire une RECHERCHE dans les fiches déjà créées.   [Pas encore implémenté]
Tapez "4" si vous voulez MODIFIER une fiche déjà existante.                 [Pas encore implémenté]
Tapez "5" si vous voulez SAUVEGARDER votre Bestiaire.                       [Pas encore implémenté]
Tapez "6" si vous voulez QUITTER le Bestiaire.                              [Pas encore implémenté]
''')
    
    #def load_save():
        #...
        
    def create_entry():
        print('''A partir d'ici, le programme va vous demander de lui dire le nom d'une catégorie
              puis vous demander la description correspondante. Il est recommandé de commencer par
              les plus importantes, dans leur ordre d'importance. Je recommande Nom, espérance de vie,
              habitat naturel, puis description physique au minimum.    
              Dans l'ordre, par exemple : "Nom", "Loup" pour donner le nom "Loup" à votre entrée.
              
              Si vous faites une erreur, vous pourrez modifier l'entrée de bestiaire par la suite.
              ''')
        entry_creator_dict = {}
        category = ""
        desc = ""
        while True:
            category = input('Quel est le nom de votre première catégorie ? - ')
            desc = input('Quelle description voulez-vous donner à cette catégorie ? - ')
            entry_creator_dict[category] = desc
            print(entry_creator_dict)
            continuer = input('Entrez 1 si vous voulez ajouter une catégorie. - ')
            if continuer == "1":
                continue
            else:
                break
    create_entry()

    #def search_entry():
        #...
    #def modify_entry():
        #...
    #def overwrite_save():
        #...
    #def stop_bestiary():
        #...
    
    def lister(num):               #Used to store multiple inputs in a list for entry creation
        il_iterator = 1
        final_list = []
        while il_iterator <= num:
            final_list.append(input(f'Quel est le nom du n°{il_iterator} ? - ').strip())
            il_iterator += 1
        return final_list
        
    pr_menu_acts = {1:'load_save',      2:'create_entry', #int:func, int:func
                    3:'search_entry',   4:'modify_entry', #int:func, int:func
                    5:'Sauvegarder',    6:'stop_program'}  #int:func, int:func
    
    while True :
        ac_choice = pr_menu_acts.get(input('Votre choix -> '))
        if ac_choice is not None:                   
            return False                            #Casse la boucle
        print('''Votre réponse ne correspond à aucune des options.
                  ''')
    ac_choice()
            
            
            
if __name__ == __main__():
    __main__()