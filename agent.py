import random
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

    # -----------------------------
    # Choose Action
    # -----------------------------
    def choose_action(self, state):

        if random.random() < self.epsilon:
            return random.randint(0, 3)

        row, col = state
        return np.argmax(self.q_table[row, col])

       # -----------------------------
    # Update Q-Table
    # -----------------------------
    def update_q_table(self, state, action, reward, next_state):

        row, col = state
        next_row, next_col = next_state

        current_q = self.q_table[row, col, action]

        max_future_q = np.max(self.q_table[next_row, next_col])

        new_q = current_q + self.alpha * (
            reward + self.gamma * max_future_q - current_q
        )

        self.q_table[row, col, action] = new_q

    # -----------------------------
    # Decay Epsilon
    # -----------------------------
    def decay_epsilon(self):

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay