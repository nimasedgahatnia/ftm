import random
from faker import Faker
fake=Faker()
class Person:

    def __init__(self, newplayer=False, **kwargs):
        self.number = kwargs.get('number', None)
        if newplayer:
            self.generatenewplayer()
        else:
            # Set default values for attributes
            defaults = {
                'first_name': '', 'last_name': '', 'age': 0, 'position': '',
                'number': 0, 'speed': 0, 'stamina': 0, 'strength': 0,
                'agility': 0, 'dribbling': 0, 'shooting': 0, 'passing': 0,
                'defending': 0, 'goals_scored': 0, 'assists': 0,
                'matches_played': 0, 'height': 0, 'weight': 0,
                'nationality': '', 'preferred_foot': '', 'injuries': [],'overall_power':0
            }
            # Update the defaults with any arguments provided
            defaults.update(kwargs)
            # Assign to self
            for key, value in defaults.items():
                setattr(self, key, value)
            self.name = f"{self.first_name} {self.last_name}"

    def generatenewplayer(self):
        # Generate random data for the new player using PDFs
        self.first_name = fake.first_name_male()
        self.last_name = fake.last_name()
        self.name = f"{self.first_name} {self.last_name}"
        self.age = random.randint(18, 40)
        
        # Define positions and their attribute ranges
        positions = {
            'GK': {'shooting': (1, 20), 'defending': (50, 100)},
            'RB': {'shooting': (1, 40), 'defending': (50, 100)},
            'LB': {'shooting': (1, 40), 'defending': (50, 100)},
            'CB': {'shooting': (1, 40), 'defending': (60, 100)},
            'DM': {'shooting': (10, 60), 'defending': (40, 90)},
            'AM': {'shooting': (30, 70), 'defending': (30, 80)},
            'RW': {'shooting': (40, 80), 'defending': (20, 70)},
            'LW': {'shooting': (40, 80), 'defending': (20, 70)},
            'CF': {'shooting': (60, 100), 'defending': (10, 60)},
            'ST': {'shooting': (60, 100), 'defending': (10, 60)}
        }
        
        # Randomly select a position for the player
        self.position = random.choice(list(positions.keys()))
        
        # Assign random attributes based on position
        for attribute, (min_val, max_val) in positions[self.position].items():
            setattr(self, attribute, random.randint(min_val, max_val))
        
        # Assign other attributes with general random values
        self.speed = random.randint(1, 100)
        self.stamina = random.randint(1, 100)
        self.strength = random.randint(1, 100)
        self.agility = random.randint(1, 100)
        self.dribbling = random.randint(1, 100)
        self.passing = random.randint(1, 100)
        
        # Height and weight using normal distribution
        average_height = 175  # Average height in centimeters
        height_std_dev = 10   # Standard deviation
        self.height = round(random.gauss(average_height, height_std_dev))
        average_weight = 70   # Average weight in kilograms
        weight_std_dev = 15   # Standard deviation
        self.weight = round(random.gauss(average_weight, weight_std_dev))
        #calculate overall rating
        position_weightings = {
            'GK': {'speed': 0.1, 'stamina': 0.1, 'strength': 0.1, 'agility': 0.2, 'dribbling': 0.05, 'shooting': 0.05, 'passing': 0.1, 'defending': 0.3},
            'RB': {'speed': 0.2, 'stamina': 0.2, 'strength': 0.1, 'agility': 0.15, 'dribbling': 0.1, 'shooting': 0.05, 'passing': 0.1, 'defending': 0.2},
            'LB': {'speed': 0.2, 'stamina': 0.2, 'strength': 0.1, 'agility': 0.15, 'dribbling': 0.1, 'shooting': 0.05, 'passing': 0.1, 'defending': 0.2},
            'CB': {'speed': 0.15, 'stamina': 0.2, 'strength': 0.2, 'agility': 0.1, 'dribbling': 0.05, 'shooting': 0.05, 'passing': 0.1, 'defending': 0.3},
            'DM': {'speed': 0.15, 'stamina': 0.25, 'strength': 0.15, 'agility': 0.1, 'dribbling': 0.1, 'shooting': 0.1, 'passing': 0.15, 'defending': 0.2},
            'AM': {'speed': 0.15, 'stamina': 0.2, 'strength': 0.1, 'agility': 0.15, 'dribbling': 0.15, 'shooting': 0.1, 'passing': 0.2, 'defending': 0.05},
            'RW': {'speed': 0.2, 'stamina': 0.15, 'strength': 0.1, 'agility': 0.2, 'dribbling': 0.2, 'shooting': 0.1, 'passing': 0.15, 'defending': 0.05},
            'LW': {'speed': 0.2, 'stamina': 0.15, 'strength': 0.1, 'agility': 0.2, 'dribbling': 0.2, 'shooting': 0.1, 'passing': 0.15, 'defending': 0.05},
            'CF': {'speed': 0.15, 'stamina': 0.1, 'strength': 0.1, 'agility': 0.15, 'dribbling': 0.2, 'shooting': 0.25, 'passing': 0.05, 'defending': 0.1},
            'ST': {'speed': 0.15, 'stamina': 0.1, 'strength': 0.1, 'agility': 0.15, 'dribbling': 0.2, 'shooting': 0.25, 'passing': 0.05, 'defending': 0.1}
        }

        weights = position_weightings[self.position]
        self.overall_power = round(
            (self.speed * weights['speed']) +
            (self.stamina * weights['stamina']) +
            (self.strength * weights['strength']) +
            (self.agility * weights['agility']) +
            (self.dribbling * weights['dribbling']) +
            (self.shooting * weights['shooting']) +
            (self.passing * weights['passing']) +
            (self.defending * weights['defending'])
        )
        self.goals_scored = 0
        self.assists = 0
        self.matches_played = 0
        self.nationality = fake.country()
        self.preferred_foot = random.choice(['Left', 'Right', 'Both'])
        self.injuries = []
        

    def __repr__(self):
        return f"**{self.position}** {self.first_name}({self.age})  }}"

    def __str__(self):
        return f"{self.name}({self.age})"
