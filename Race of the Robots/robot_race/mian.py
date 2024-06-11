import robot_race_functions as rr
from collections import deque, Counter, namedtuple
from time import time, sleep

maze_file_name = 'data/maze_data_1.csv'
seconds_between_turns = 0.3
max_turns = 35

# Initialize the robot race
maze_data = rr.read_maze(maze_file_name)
rr.print_maze(maze_data)
walls, goal, bots = rr.process_maze_init(maze_data)

# Populate a deque of all robot commands for the provided maze
robot_moves = deque()
num_of_turns = 0
while not rr.is_race_over(bots) and num_of_turns < max_turns:
  
  # For every bot in the list of bots, if the bot has not reached the end, add a new move to the robot_moves deque
  for bot in bots:
    if not bot.has_finished:
      robot_moves.append(rr.compute_robot_logic(walls, goal, bot))

  num_of_turns += 1

# Count the number of moves based on the robot names
num_moves = Counter(move[0] for move in robot_moves)

# Count the number of collisions by robot name
num_collisions = Counter(move[0] for move in robot_moves if move[2] == True)

# Create a namedtuple to keep track of our robots' points
BotScoreData = namedtuple('BotScoreData', ['name', 'num_moves', 'num_collisions', 'score'])

# Calculate the scores (moves + collisions) for each robot and append it to bot_scores 
bot_scores = []

for bot in bots:
  bot_scores.append(namedtuple('BotScoreData', [bot.name, num_moves, num_collisions, num_moves + num_collisions]))

# Populate a dict to keep track of the robot movements
bot_data = {}

for bot in bots:
  bot_data.update({bot.name: bot})

# Move the robots and update the map based on the moves deque
while len(robot_moves) > 0:
  # Make sure to pop moves from the front of the deque
  bot_name, direction, has_collided = robot_moves.popleft()
  bot_data[bot_name].process_move(direction)

  # Update the maze characters based on the robot positions and print it to the console
  rr.update_maze_characters(maze_data, bots)
  rr.print_maze(maze_data)
  sleep(seconds_between_turns - time() % seconds_between_turns) # sleep until next turn by subtracting the time since the last turn

rr.print_results(bot_scores)