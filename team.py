from faker import Faker
from players import Person
import random
fake = Faker()
positions = ['GK', 'RB', 'LB', 'CB', 'DM', 'AM', 'RW', 'LW', 'CF', 'ST']

class Team:
    def __init__(self):
        team_suffixes = ['Club', 'Squad', 'Team', 'Boys', 'Girls']
        locations = ['Springfield', 'Riverdale', 'Gotham', 'Metropolis', 'Star City', 'Central City']
        football_terms =  ['United', 'City', 'Rovers', 'FC', 'Athletic', 'Rangers', 'Sporting']
        self.name =f"{random.choice(locations)} {random.choice(football_terms)} {random.choice(team_suffixes)}"
        self.shortname=self.create_acronym(self.name)
        self.players = self.CreateTeam()
    def create_acronym(self,name):
    # Split the name into words and take the first letter of each
        return ''.join(word[0] for word in name.split()[:3]).upper()
    def CreateTeam(self):
        newplayers = []
        t_shirt_numbers = random.sample(range(1, 100), 23)
        for i in range(1, 24):
            newplayers.append(Person(fake.first_name_male(),fake.last_name(),random.randint(15, 30),random.choice(positions),t_shirt_numbers[i-1]))
        return newplayers
    def choose_starting_eleven(self):
        desired_positions = {
            'GK': 1, 'RB': 1, 'LB': 1, 'CB': 2, 'DM': 2,
            'AM': 1, 'RW': 1, 'LW': 1, 'CF': 0, 'ST': 1
        }
        
        starting_eleven = []
        available_players = self.players.copy()  # Make a copy of the players list
        
        for position, count in desired_positions.items():
            # Filter players by position
            players_in_position = [player for player in available_players if player.position == position]
            
            # Check if enough players are available in the position
            if len(players_in_position) >= count:
                # Randomly select the required number of players for the position
                selected_players = random.sample(players_in_position, count)
            else:
                # Not enough players in position, select random players
                selected_players = random.sample(available_players, count)
            
            # Add the selected players to the starting eleven
            starting_eleven.extend(selected_players)
            
            # Remove the selected players from the available pool
            available_players = [player for player in available_players if player not in selected_players]

        # If there are still positions to fill, add random players
        while len(starting_eleven) < 11:
            if available_players:
                starting_eleven.append(random.choice(available_players))
                available_players.remove(starting_eleven[-1])
            else:
                print("Not enough players to form a starting eleven")
                break
        
        return starting_eleven
    

