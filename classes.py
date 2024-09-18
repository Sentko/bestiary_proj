class Entry():          #Basic Bestiary Entry
    def __init__(self, name, race, phys_desc, diet=None, nat_hab=None, life_expec=None, soc_bhviour=None, predators=None, preys=None, sc_name=None):
        self.name = name
        self.race = race
        self.nat_hab = nat_hab
        self.phys_desc = phys_desc
        self.life_expec = life_expec
        self.diet = diet                                            #All possible parts of entries
        self.soc_bhviour = soc_bhviour
        self.predators = predators
        self.preys = preys
        self.sc_name = sc_name
        
        
class Carnivore(Entry): #DIET=CARNIVORE
    def __init__(self, is_pred, hnting_tech=None):  #Hunting techniques should be unique to predators. There is still the case of scavengers like vultures and such. 
                                                    #In that case, hnting_tech should equal None, while preys should be f'Every animal found in {lower(self.nat_hab)}'
        self.is_pred = is_pred
        self.hnting_tech = hnting_tech
        super().__init__(self.name, self.race, self.nat_hab, self.phys_desc, self.life_expec, self.diet, self.soc_bhviour, self.predators, self.preys, self.sc_name)
        
class Herbivore(Entry): #DIET=HERBIVORE
    def __init__(self, favoured_nonmeat):              #Could add "is_pred". 
        self.favoured_nonmeat = favoured_nonmeat
        super().__init__(self.name, self.race, self.nat_hab, self.phys_desc, self.life_expec, self.diet, self.soc_bhviour, self.predators, self.sc_name)
        
class Omnivore(Entry):  #DIET=OMNIVORE
    def __init__(self, is_pred, favoured_nonmeat=None, hnting_tech=None):
        self.is_pred = is_pred
        self.favoured_nonmeat = favoured_nonmeat
        self.hnting_tech = hnting_tech
        super().__init__(self, self.name, self.race, self.phys_desc, self.diet, self.nat_hab, self.life_expec, self.soc_bhviour, self.predators, self.preys, self.sc_name)