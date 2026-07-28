from agent import Agent

agent = Agent()

state = (0, 0)

for i in range(10):
    action = agent.choose_action(state)
    print(action)