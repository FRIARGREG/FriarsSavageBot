
"""
attributes min d4
AGILITY
SMARTS
SPIRIT
STRENGTH
VIGOR

given skills min d4
Athletics (Agility)
Common Knowledge (Smarts)
Notice (Smarts)
Persuasion (Spirit)
Stealth (Agility)

all other skills are untrained
UNTRAINED 1d4-2

Thievery (Agility) untrained = 1d4-2
Thievery (Agility) trained = 1d4



"""



class Trait:
    """
    Traits are the base measures of a character. All characters both wildcards
    and extras will have 5 ATTRIBUTE traits and a minimum of 5 SKILL traits.
    """
    def __init__(self):
        self.id # INT
        self.name # text
        self.trained # bool
        self.value # INT 0, 4, 6, 8, 10, 12
        






##
