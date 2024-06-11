from team import Team
from players import Person
import random
import sys
from termcolor import colored, cprint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors
class Game:
    def __init__(self):
        self.Home=Team()
        self.Away=Team()
        self.initialize_game()
    def initialize_game(self):
        print(f"The {self.Home.shortname}'s are playing at home against the {self.Away.shortname}'s")
        starting_lineup_home = self.Home.choose_starting_eleven()
        for player in starting_lineup_home:
            print(player.position,player.name, player.overall_power)   
        starting_lineup_away = self.Away.choose_starting_eleven()
        cprint("VS", "black","on_red", attrs=["bold"], file=sys.stderr)
        for player in starting_lineup_away:
            print(player.position,player.name, player.overall_power)   
        
#game1=Game()
field = np.zeros((70, 100))

# Set the stadium boundaries
field[0, :] = 1
field[-1, :] = 1
field[:, 0] = 1
field[:, -1] = 1

# Set the midline
field[:, field.shape[1]//2] = 2

# Initialize the ball position
ball_y, ball_x = field.shape[0]//2, field.shape[1]//2

# Add football goals
goal_width = 10  # You can adjust this
field[field.shape[0]//2 - goal_width//2 : field.shape[0]//2 + goal_width//2, 0] = 3
field[field.shape[0]//2 - goal_width//2 : field.shape[0]//2 + goal_width//2, -1] = 3

def update_frame(i):
    global ball_y, ball_x

    # Clear the previous ball position
    field[ball_y, ball_x] = 0

    # Update the ball position
    ball_y += random.randint(-1, 1)
    ball_x += random.randint(-1, 1)

    # Make sure the ball doesn't go out of the field
    ball_y = max(min(ball_y, field.shape[0]-1), 0)
    ball_x = max(min(ball_x, field.shape[1]-1), 0)

    # Draw the ball
    field[ball_y, ball_x] = 4

    # Redraw the goals
    field[field.shape[0]//2 - goal_width//2 : field.shape[0]//2 + goal_width//2, 0] = 3
    field[field.shape[0]//2 - goal_width//2 : field.shape[0]//2 + goal_width//2, -1] = 3

    # Redraw the midline
    field[:, field.shape[1]//2] = 2

    # Update the plot
    plt.clf()
    plt.imshow(field, cmap='viridis')

# Create the animation
ani = animation.FuncAnimation(plt.gcf(), update_frame, interval=50)

plt.show()