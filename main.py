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
        name_desc, sc_name_desc, race_choice, phys_desc, diet_desc, nat_hab_desc, life_ex_desc, sc_bhvr_desc, preds_desc, preys_desc = None
        print('''Vous allez être emmenés dans le processus de création de fiches.
              Lorsque votre entrée n'a pas la chose qui vous est demandé, appuyez simplement
              sur Entréee sans donner de réponse. ''')
        name_desc   = input('Quel est le nom à attribuer à votre entrée ? -').strip()
        sc_name_desc= input("Quel est le nom scientifique de votre entrée ? -").strip()
        race_choice = input('Quelle est la race de votre entrée ? -').strip()
        phys_desc   = input('A quoi ressemble physiquement votre entrée ? -').strip()
        diet_desc   = input('Quel est le régime de votre entrée ? -').strip()    #CLASSES ?
        nat_hab_desc= input("Quel est l'habitat naturel de votre entrée ? -").strip()
        life_ex_desc= input("Quelle est l'espérance de vie de votre entrée ? -").strip()
        sc_bhvr_desc= input("Comment se comporte votre entrée auprès des siens ? -").strip()
        preds_desc  = input("Votre entrée a-t-elle plusieurs prédateurs ? -").strip() #NEEDS FOLLOW UP
        preys_desc  = input("Votre entrée a-t-elle plusieurs proies ? -").strip() #NEEDS FOLLOW UP

    #def search_entry():
        #...
    #def modify_entry():
        #...
    #def overwrite_save():
        #...
    #def stop_bestiary():
        #...
        
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