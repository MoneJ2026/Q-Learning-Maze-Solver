from environment import GridWorld
from agent import Agent

env = GridWorld()
agent = Agent()

episodes = 100

for episode in range(episodes):

    state = env.reset()

    done = False

    while not done:

        action = agent.choose_action(state)

        next_state, reward, done = env.step(action)

        agent.update_q_table(
            state,
            action,
            reward,
            next_state
        )

        state = next_state

print("Training Finished!")