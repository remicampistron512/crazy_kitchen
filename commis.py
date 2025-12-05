from abc import ABC


class Commis(ABC):
    def __init__(self, nom):
        self.nom = nom
