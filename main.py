from agent import Agent

agent = Agent()

state = (0, 0)
action = 3
reward = -1
next_state = (0, 1)

print("Before:")
print(agent.q_table[0, 0])

agent.update_q_table(state, action, reward, next_state)

print("After:")
print(agent.q_table[0, 0])