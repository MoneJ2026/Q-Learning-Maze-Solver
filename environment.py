class GridWorld:

    def __init__(self):
        self.rows = 5
        self.cols = 5

        self.start = (0, 0)
        self.goal = (4, 4)

        self.state = self.start

    def reset(self):
        self.state = self.start
        return self.state

    def step(self, action):

        row, col = self.state

        if action == 0:
            row -= 1

        elif action == 1:
            row += 1

        elif action == 2:
            col -= 1

        elif action == 3:
            col += 1

        row = max(0, min(row, self.rows - 1))
        col = max(0, min(col, self.cols - 1))

        self.state = (row, col)

        reward = -1
        done = False

        if self.state == self.goal:
            reward = 100
            done = True

        return self.state, reward, done