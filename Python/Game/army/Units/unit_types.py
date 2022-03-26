from Units.race import *
from Units.stats import stats

class ArchKnight(Deity):
    "Guard unit type for Deities"
    def __init__(self):
        super().__init__(stats["ArchKnight"])


class ArchLord(Deity):
    """Insanely strong Deity unit type"""
    def __init__(self):
        super().__init__(stats["ArchLord"])