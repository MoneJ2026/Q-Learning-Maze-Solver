import matplotlib.pyplot as plt
import numpy as np


def draw_grid(path=None):

    grid = np.zeros((5, 5))

    plt.figure(figsize=(6, 6))

    plt.imshow(grid, cmap="Greys")

    # Grid Lines
    plt.xticks(np.arange(-0.5, 5, 1))
    plt.yticks(np.arange(-0.5, 5, 1))
    plt.grid(color="black")

    # Start
    plt.text(
        0,
        0,
        "S",
        ha="center",
        va="center",
        fontsize=16,
        color="green",
        weight="bold"
    )

    # Goal
    plt.text(
        4,
        4,
        "G",
        ha="center",
        va="center",
        fontsize=16,
        color="red",
        weight="bold"
    )

    # Agent Path
    if path:

        for row, col in path:

            plt.scatter(
                col,
                row,
                s=120,
                c="blue"
            )

    plt.title("Q-Learning Maze Solver")

    plt.show()