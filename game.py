from team import Team
from players import Person
import random

class Game:
    def __init__(self):
        self.Home=Team()
        self.Away=Team()
        self.initialize_game()
    def initialize_game(self):
        print(f"The {self.Home.name} are playing at home against the {self.Away.name} at the {random.choice(['Stadium', 'Arena', 'Field'])}")
        starting_lineup = self.Home.choose_starting_eleven()
        for player in starting_lineup:
            print(player.name, player.position, player.number)    
        
game1=Game()

