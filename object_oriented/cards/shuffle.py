import random
from carddeck import Carddeck

class Shuffle(Carddeck):
    def __init__(self):
        super().__init__()

    def shuffle(self):
        random.shuffle(self.deck)

