import random


class Card:
    """A card from a deck of playing cards.
   
    Attributes:
        value (int): The value on the face of the card.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def draw(self):
        """Generates a new random value and calculates the points for the Card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
