from environment import GridWorld
from agent import Agent
import numpy as np

env = GridWorld()
agent = Agent()

episodes = 100

for episode in range(episodes):

    state = env.reset()
    done = False

    max_steps = 100
    steps = 0

    while not done and steps < max_steps:

        action = agent.choose_action(state)

        next_state, reward, done = env.step(action)

        agent.update_q_table(
            state,
            action,
            reward,
            next_state
        )

        state = next_state
        steps += 1

    agent.decay_epsilon()

print("Training Finished!")

np.save("q_table.npy", agent.q_table)

print("Q-table Saved!")