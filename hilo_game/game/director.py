from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card: An instance of Card.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.is_playing = True
        self.score = 0
        self.total_score = 0
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to guess.

        Args:
            self (Director): An instance of Director.
        """
        print (f'The card is: {self.card.current_card()} ')
        self.card.guess = input("higher or lower [h/l] ")
        print (f'Next card is: {self.card.second_current_card()}')
        # self.is_playing = (show_card == "h")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        self.card.high()
        self.card.low()
        print (f'Your score is : {self.card.points}')

        # for i in range(len(self.dice)):
        #     die = self.dice[i]
        #     die.roll()
        #     self.score += die.points 
        # self.total_score += self.score

    def do_outputs(self):
        """Asks the user id they would like to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        self.play_again = input('Play again? [y/n] ')
        if self.play_again.lower() == 'n':
            self.is_playing = False
        
        print ('')

        
        # values = ""
        # for i in range(len(self.dice)):
        #     die = self.dice[i]
        #     values += f"{die.value} "

        # print(f"You rolled: {values}")
        # print(f"Your score is: {self.total_score}\n")
        # self.is_playing == (self.score > 0)
        