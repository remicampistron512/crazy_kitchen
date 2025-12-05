import threading
from dataclasses import dataclass

from ingredient import Ingredient


@dataclass
class Oeuf(threading.Thread, Ingredient):
    pass
