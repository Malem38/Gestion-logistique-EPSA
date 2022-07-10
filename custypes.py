from enum import Enum

class Departement(str, Enum):
    BASTIE = "BASTIE"
    CHAIPE = "CHAIPE"
    CHASEA = "CHASEA"
    LASMECA = "LASMECA"

    def __str__(self):
        return f"{self.name}<{self.value}>"

class LieuStock(str, Enum):
    ISYRUN_Chaud = "ISYRUN Chaud"
    ISYRUN_Froid = "ISYRUN Froid"
    ISYRUN_Bron = "ISYRUN Bron"

    def __str__(self):
        return f"{self.name}<{self.value}>"

class EtatVerif(str, Enum):
    commande_lancee = "Commande lancée"
    bon_envoye = "Bon de commande envoyé"

    def __str__(self):
        return f"{self.name}<{self.value}>"

class Action(str, Enum):
    action1="action1"
    action2="action2"

    def __str__(self):
        return f"{self.name}<{self.value}>"

class Budget(str, Enum):
    ISYRUN_Central = "ISYRUN Central"
    Association_EPSA = "Association EPSA"

    def __str__(self):
        return f"{self.name}<{self.value}>"