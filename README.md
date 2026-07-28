# 🧠 Q-Learning Maze Solver

A Reinforcement Learning project built in Python that teaches an intelligent agent how to solve a 5×5 maze using the **Q-Learning** algorithm.

---

## 📌 Project Overview

This project demonstrates the fundamentals of Reinforcement Learning by training an agent to move from a start position to a goal position while maximizing rewards.

The agent learns through trial and error using the Q-Learning algorithm and stores its knowledge in a Q-Table.

---

## ✨ Features

- ✅ 5×5 GridWorld Environment
- ✅ Q-Learning Algorithm
- ✅ Bellman Equation
- ✅ Epsilon-Greedy Exploration
- ✅ Q-Table Training
- ✅ Save and Load Q-Table
- ✅ Maze Visualization
- ✅ Agent Path Animation
- ✅ Reward Graph
- ✅ Git Version Control

---

## 🧠 Reinforcement Learning Concepts

This project covers:

- Agent
- Environment
- State
- Action
- Reward
- Episode
- Policy
- Exploration vs Exploitation
- Bellman Equation
- Q-Learning

---

## 📂 Project Structure

```
Q-Learning-Maze-Solver/
│
├── agent.py
├── environment.py
├── train.py
├── test.py
├── visualize.py
├── main.py
├── q_table.npy
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/MoneJ2026/Q-Learning-Maze-Solver.git
```

Go into the project:

```bash
cd Q-Learning-Maze-Solver
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Agent

```bash
python train.py
```

This will:

- Train the agent
- Save the learned Q-Table
- Display the reward graph

---

## 🧪 Test the Agent

```bash
python test.py
```

The trained agent will solve the maze and display:

- Learned path
- Maze visualization
- Agent animation

---

## 📊 Algorithm

Q-value update:

```
Q(s,a) = Q(s,a) + α[r + γ max(Q(s',a')) − Q(s,a)]
```

Where:

- α = Learning Rate
- γ = Discount Factor
- r = Reward

---

## 📚 Libraries Used

- Python
- NumPy
- Matplotlib

---

## 🚀 Future Improvements

- Random Maze Generation
- Larger Grid Sizes
- Deep Q-Network (DQN)
- OpenAI Gymnasium Integration
- Multiple Goal States

---

## 👨‍💻 Author

**Monet Girma**

Computer Science Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Reinforcement Learning
- Python Development

GitHub:

https://github.com/MoneJ2026

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.