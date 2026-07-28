from environment import GridWorld
from agent import Agent
import numpy as np

env = GridWorld()
agent = Agent()

# Load trained Q-table
agent.q_table = np.load("q_table.npy")

# Disable exploration
agent.epsilon = 0

state = env.reset()

done = False

max_steps = 100
steps = 0

print("Start:", state)

while not done and steps < max_steps:

    action = agent.choose_action(state)

    next_state, reward, done = env.step(action)

    print(f"Action: {action} -> State: {next_state}")

    state = next_state

    steps += 1

if done:
    print("🎉 Goal Reached!")
else:
    print("❌ Maximum steps reached.")