from environment import GridWorld

env = GridWorld()

state = env.reset()

print("Start:", state)

state, reward, done = env.step(3)

print(state)
print(reward)
print(done)