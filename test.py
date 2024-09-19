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