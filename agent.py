import numpy as np


class Agent:

    def __init__(self):

        # Learning Rate
        self.alpha = 0.1

        # Discount Factor
        self.gamma = 0.9

        # Exploration Rate
        self.epsilon = 1.0

        # Minimum Exploration
        self.epsilon_min = 0.01

        # Epsilon Decay
        self.epsilon_decay = 0.995

        # Q-Table
        self.q_table = np.zeros((5, 5, 4))