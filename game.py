import numpy as np

# Create a 10x5 football field (you can adjust the size as needed)
field = np.zeros((10, 5))

# Define the positions of players and the ball using (row, column) format
# Let's say '1' represents players of team A, '2' represents team B, and '9' is the ball
players_team_a = [(1, 1), (1, 3)]
players_team_b = [(8, 1), (8, 3)]
ball_position = (5, 2)

# Place the players and the ball on the field
for position in players_team_a:
    field[position] = 1

for position in players_team_b:
    field[position] = 2

field[ball_position] = 9

# Print the field
print(field)
