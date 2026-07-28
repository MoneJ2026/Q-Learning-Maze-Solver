from environment import GridWorld
from agent import Agent
from visualize import draw_grid
import numpy as np

# Create Environment
env = GridWorld()

# Create Agent
agent = Agent()

# Load trained Q-table
agent.q_table = np.load("q_table.npy")

# Disable exploration
agent.epsilon = 0

# Reset environment
state = env.reset()

# Save visited path
path = [state]

done = False

max_steps = 100
steps = 0

print("Start:", state)

while not done and steps < max_steps:

    # Choose best action
    action = agent.choose_action(state)

    # Move in environment
    next_state, reward, done = env.step(action)

    print(f"Action: {action} -> State: {next_state}")

    # Move to next state
    state = next_state

    # Save path
    path.append(state)

    steps += 1

# Result
if done:
    print("🎉 Goal Reached!")
else:
    print("❌ Maximum steps reached.")

# Draw Maze
draw_grid(path)