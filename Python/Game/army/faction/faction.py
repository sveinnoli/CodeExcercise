import random

NAMES = ["Peter", "Dinklage", "Jon", "Snow", "Dingleberg", "Icky vicky", "Sveinn the super cool"]

class factionLogic:
    """Shared faction logic"""
    def __init__(self, faction_name):
        self.faction = {
            "members" : {},
            "faction_name" : faction_name
        }

    def add_member(self, member, rank):
        self.faction["members"][member] = {
            "name" : random.choice(NAMES),
            "ID" : member,
            "rank" : rank
        }

    def get_member(self, member):
        try:
            return self.faction["members"][member]["ID"].get_stats()
        except KeyError:
            print(f"Member: {member} does not exist")

    def remove_member(self, member):
        try:
            del self.faction["members"][member]
        except KeyError:
            print(f"Member {member} does not exist")

    def update_rank(self, member, rank):
        try: 
            self.faction["members"][member]["rank"] = rank
        except KeyError:
            print(f"No member found with ID: {member}")
    

class Omen(factionLogic):
    """Faction type"""
    def __init__(self, faction_name):
        super().__init__(faction_name)
        self.ranks = ["Paladin", "Apostle", "Enlightened", "Wizlar", "Arch Knight"]


class Khiles(factionLogic):
    """Faction type"""
    def __init__(self, faction_name):
        super().__init__(faction_name)
        self.ranks = ["Foul", "Corpse", "Mutant", "Death Knight", "Death"]


class Deities(factionLogic):
    """Faction type"""
    def __init__(self, faction_name):
        super().__init__(faction_name)
        self.ranks = ["Forbidden", "God", "Aphrodite", "Sin", "Godly Knight"]

