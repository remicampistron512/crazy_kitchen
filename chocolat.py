import threading
from dataclasses import dataclass

from ingredient import Ingredient


@dataclass
class Chocolat(threading.Thread, Ingredient):
    pass
