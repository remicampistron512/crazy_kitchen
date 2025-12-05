import threading
from abc import ABC


class Ingredient(threading.Thread, ABC):
    def __init__(self, nom, quantite, unite):
        super().__init__()
        self.nom = nom
        self.quantite = quantite
        self.unite = unite
