from agent import Agent

print("Import successful!")

agent = Agent()

print("Alpha:", agent.alpha)
print("Gamma:", agent.gamma)
print("Epsilon:", agent.epsilon)
print("Q-table Shape:", agent.q_table.shape)