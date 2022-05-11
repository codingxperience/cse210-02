import random


class Card:
    """A card with a random value between 1-13.

    The responsibility of Crd  is to keep track of the current value fd the card and calculate the points associated with it .
   
    Attributes:
        first_value (int): The number of the previous card.
        second_value (int): The number of the second card.

    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Die): An instance of Card.
        """
        self.first_value = 0
        self.second_value = 0
        self.points = 300
        self.guess = ''
        

    def current_card(self):
        """Generates a new random value for the card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.first_value = random.randint(1,13)
        return self.first_value

    def second_current_card(self):
        self.second_value = random.randint(1,13)
        return self.second_value
    
    def high(self):

        """checks to see if the guess is higher than the current card .
        
        Args:
            self (Card): An instance of Card.
        """
        if self.second_value > self.first_value and self.guess.lower() == 'h':
            self.points += 100
        elif self.second_value < self.first_value and self.guess.lower() == 'h':
            self.points -= 75

    def low(self):
        """checks to see if the guess is higher than the current card .
        
        Args:
            self (Card): An instance of Card.
        """
        if self.second_value < self.first_value and self.guess.lower() == 'l':
            self.points += 100
        elif self.second_value > self.first_value and self.guess.lower() == 'l':
            self.points -= 75


        # if self.guess.lower() == 'h' and self.guess.lower() > self.first_value:
        #     self.points += 100
        # elif self.guess.lower() != 'h' and self.guess.lower() < self.first_value:
        #     self.points -= 75
        




        # self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0