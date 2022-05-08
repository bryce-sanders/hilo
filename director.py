from card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card_1: The first card drawn in a round.
        card_2: The second card drawn in a round.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card_1 = Card()
        self.card_2 = Card() 
        self.is_playing = True
        self.score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.draw_cards()
            self.make_guess()

    def get_inputs(self):
        """Ask the user if they want to start a new round.

        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score is {self.score}")
        next_round = input("Play a round? [y/n] ")
        self.is_playing = (next_round == "y")
        if self.score <= 0:
            self.is_playing = False

    def draw_cards(self):
        """Draw two new cards for the round.

        Args:
            self (Director): An instance of Director.
        """
        self.card_1.draw()
        self.card_2.draw()
       
    def make_guess(self):
        """Have the player make a guess

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        print(f"The first card drawn has a value of {self.card_1.value}.")
        guess = input("Is the second card higher or lower? [h/l]")

        if self.card_1.value < self.card_2.value:
            answer = "h"
        else:
            answer = "l"

        if answer == guess:
            self.score += 100
        else:
            self.score -= 75