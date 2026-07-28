from environment import GridWorld
from agent import Agent

env = GridWorld()
agent = Agent()

agent.epsilon = 0

state = env.reset()

done = False

print("Start:", state)

# ------------------------
# Kana dabali
# ------------------------
max_steps = 100
steps = 0

while not done and steps < max_steps:

    action = agent.choose_action(state)

    next_state, reward, done = env.step(action)

    print("Action:", action)
    print("State:", next_state)

    state = next_state
    steps += 1

if done:
    print("Goal Reached!")
else:
    print("Maximum steps reached.")