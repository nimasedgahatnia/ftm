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
    
a=Team()
print(a.name)
print(a.shortname)
print(a.players)
