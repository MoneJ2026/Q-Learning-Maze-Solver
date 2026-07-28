from environment import GridWorld
from agent import Agent
import numpy as np
import matplotlib.pyplot as plt

env = GridWorld()
agent = Agent()

episodes = 100

# Reward history
reward_history = []

for episode in range(episodes):

    state = env.reset()

    done = False

    max_steps = 100
    steps = 0

    # Total reward for one episode
    total_reward = 0

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

        # Add reward
        total_reward += reward

        steps += 1

    reward_history.append(total_reward)

    agent.decay_epsilon()

print("Training Finished!")

np.save("q_table.npy", agent.q_table)

print("Q-table Saved!")

# Reward Graph
plt.figure(figsize=(8,5))

plt.plot(reward_history)

plt.title("Training Reward")

plt.xlabel("Episode")

plt.ylabel("Total Reward")

plt.grid(True)

plt.show()