import matplotlib.pyplot as plt
import numpy as np


# -----------------------------
# Draw Complete Path
# -----------------------------
def draw_grid(path=None):

    grid = np.zeros((5, 5))

    plt.figure(figsize=(6, 6))
    plt.imshow(grid, cmap="Greys", origin="upper")

    plt.xticks(np.arange(-0.5, 5, 1))
    plt.yticks(np.arange(-0.5, 5, 1))
    plt.grid(color="black", linewidth=2)

    plt.xticks([])
    plt.yticks([])

    # Start
    plt.text(
        0, 0, "S",
        ha="center",
        va="center",
        fontsize=18,
        color="green",
        weight="bold"
    )

    # Goal
    plt.text(
        4, 4, "G",
        ha="center",
        va="center",
        fontsize=18,
        color="red",
        weight="bold"
    )

    # Walls
    walls = [
        (1, 1),
        (2, 3),
        (3, 1)
    ]

    for row, col in walls:
        plt.scatter(
            col,
            row,
            s=400,
            marker="s",
            color="black"
        )

    # Draw Path
    if path:
        rows = [p[0] for p in path]
        cols = [p[1] for p in path]
        plt.plot(cols, rows, marker="o", linewidth=3, color="blue")

    plt.title("Q-Learning Maze Solver")
    plt.show()


# -----------------------------
# Animate Agent Movement
# -----------------------------
def animate_path(path):

    grid = np.zeros((5, 5))

    plt.figure(figsize=(6, 6))

    walls = [
        (1, 1),
        (2, 3),
        (3, 1)
    ]

    for position in path:

        plt.clf()

        plt.imshow(grid, cmap="Greys", origin="upper")

        plt.xticks(np.arange(-0.5, 5, 1))
        plt.yticks(np.arange(-0.5, 5, 1))
        plt.grid(color="black", linewidth=2)

        plt.xticks([])
        plt.yticks([])

        # Start
        plt.text(
            0, 0, "S",
            ha="center",
            va="center",
            fontsize=18,
            color="green",
            weight="bold"
        )

        # Goal
        plt.text(
            4, 4, "G",
            ha="center",
            va="center",
            fontsize=18,
            color="red",
            weight="bold"
        )

        # Walls
        for wall_row, wall_col in walls:
            plt.scatter(
                wall_col,
                wall_row,
                s=400,
                marker="s",
                color="black"
            )

        # Agent
        row, col = position

        plt.scatter(
            col,
            row,
            s=300,
            color="blue"
        )

        plt.title("Agent Moving")

        plt.pause(0.5)

    plt.show()