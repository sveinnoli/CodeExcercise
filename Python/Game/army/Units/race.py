from faction.faction import Omen, Khiles, Deities

class Stats: 
    """Entities shared stats"""
    def __init__(self, stats:dict):
        self.stats = stats
        
        # Attack
        self.max_attack = stats.get("max_attack")
        self.min_attack = stats.get("min_attack")
        self.crit_increment = stats.get("crit_increment")
        self.crit_chance = stats.get("crit_chance")
        self.magic_defence_break = stats.get("magic_defence_break")
        self.physical_defence_break = stats.get("physical_defence_break")
        
        # Defence
        self.health = stats.get("health")
        self.physical_defence = stats.get("physical_defence")
        self.magic_defence = stats.get("magic_defence")

        # Utility
        self.movement_speed = stats.get("movement_speed")

    def get_stats(self) -> dict:
        return self.stats


class Human(Stats):
    """Good race"""
    def __init__(self, stats):
        super().__init__(stats)
        self.race_info = {
            "faction" : Omen.__name__
        }
        

class Undead(Stats):
    """Evil race"""
    def __init__(self, stats):
        super().__init__(stats)
        self.race_info = {
            "faction" : Khiles.__name__
        }

class Deity(Stats):
    "Godly race"
    def __init__(self, stats):
        super().__init__(stats)
        self.race_info = {
            "faction" : Deities.__name__
        }