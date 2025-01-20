# Q-Learning with Epsilon-Greedy Algorithm

This repository demonstrates the implementation of a reinforcement learning agent using the Q-Learning algorithm with an epsilon-greedy strategy. The agent is designed to learn optimal actions in various environments, including **Taxi-v3** and **Acrobot**, by balancing exploration and exploitation.

## Overview

### What is Q-Learning?
Q-Learning is a model-free, off-policy reinforcement learning algorithm that allows an agent to learn the value of an action in a particular state. It works by iteratively updating a Q-table, which estimates the expected future rewards for state-action pairs.

### Epsilon-Greedy Strategy
To balance exploration (trying new actions to discover their effects) and exploitation (using the best-known actions to maximize rewards), the epsilon-greedy strategy is used:
- With probability `epsilon`, the agent selects a random action (exploration).
- With probability `1 - epsilon`, the agent selects the action with the highest Q-value (exploitation).
- Over time, epsilon is decayed to focus more on exploitation as the agent gains knowledge about the environment.

## Key Features

- **Learning Mechanism**: The agent updates the Q-value for a state-action pair using the Bellman equation:
  \[ Q(s, a) \leftarrow Q(s, a) + \alpha \big[ r + \gamma \max_a Q(s', a) - Q(s, a) \big] \]
  where:
  - \( \alpha \) is the learning rate.
  - \( \gamma \) is the discount factor.
  - \( r \) is the immediate reward.
  - \( s' \) is the next state.

- **Exploration and Exploitation**: The epsilon-greedy approach ensures the agent explores initially and gradually shifts to exploitation as it learns the optimal policy.

- **Adaptability**: The algorithm is implemented to work across various environments with configurable parameters such as learning rate, discount factor, and epsilon decay rate.

## Demonstrations

### Taxi-v3
The agent learns to pick up and drop off passengers in an optimal way using the Taxi-v3 environment.

<img src="https://github.com/user-attachments/assets/5584792d-7223-4500-b7c3-6e34bb92cf18" width="200"> 
 
### Acrobot
The agent learns to control a two-link robot arm to swing up and reach a target using the Acrobot environment.

<img src="https://github.com/user-attachments/assets/022dc269-fe88-46d4-9049-1cbd4c3bfd31" width="200"> 

## How It Works

### Training Phase
1. **Initialization**:
   - The Q-table is initialized to zeros (or small random values).
   - Parameters such as learning rate (\( \alpha \)), discount factor (\( \gamma \)), and epsilon are set.

2. **Action Selection**:
   - The agent observes the current state.
   - It chooses an action based on the epsilon-greedy strategy.

3. **Update Rule**:
   - After taking the action, the agent observes the reward and the next state.
   - The Q-value for the state-action pair is updated using the Bellman equation.

4. **Epsilon Decay**:
   - Epsilon is reduced gradually after each episode to focus more on exploitation as the training progresses.

### Testing Phase
- In the testing phase, the agent uses the learned Q-table to select the optimal actions without further updates.
- The epsilon is typically set to 0 to ensure purely greedy action selection.

## Advantages of Q-Learning with Epsilon-Greedy
- **Simple and Effective**: Q-Learning is straightforward to implement and works well in discrete action spaces.
- **Exploration-Exploitation Balance**: The epsilon-greedy strategy ensures the agent explores sufficiently before converging to an optimal policy.
- **Model-Free**: The agent does not require a model of the environment, making it versatile.

## Use Cases
Q-Learning with epsilon-greedy is widely used in applications such as:
- Game playing (e.g., solving grid-world problems, learning to play simple games).
- Pathfinding tasks (e.g., navigating mazes).
- Decision-making problems where the state and action spaces are discrete.

## How to Run

1. **Set Environment**:
   - Configure the environment parameters, including state and action space sizes.

2. **Train the Agent**:
   - Run the training phase where the Q-table is iteratively updated.

3. **Test the Agent**:
   - Use the learned Q-table to evaluate the agent's performance in the environment.

## Dependencies
- `numpy`
- Python 3.x

## Contributing
Feel free to contribute by improving the algorithm, adding new features, or testing it in different environments.

## License
This project is open-sourced under the MIT License. See the LICENSE file for details.


### What is Q-Learning?
Q-Learning is a model-free, off-policy reinforcement learning algorithm that allows an agent to learn the value of an action in a particular state. It works by iteratively updating a Q-table, which estimates the expected future rewards for state-action pairs.

### Epsilon-Greedy Strategy
To balance exploration (trying new actions to discover their effects) and exploitation (using the best-known actions to maximize rewards), the epsilon-greedy strategy is used:
- With probability `epsilon`, the agent selects a random action (exploration).
- With probability `1 - epsilon`, the agent selects the action with the highest Q-value (exploitation).
- Over time, epsilon is decayed to focus more on exploitation as the agent gains knowledge about the environment.

## Key Features

- **Learning Mechanism**: The agent updates the Q-value for a state-action pair using the Bellman equation:
  \[ Q(s, a) \leftarrow Q(s, a) + \alpha \big[ r + \gamma \max_a Q(s', a) - Q(s, a) \big] \]
  where:
  - \( \alpha \) is the learning rate.
  - \( \gamma \) is the discount factor.
  - \( r \) is the immediate reward.
  - \( s' \) is the next state.

- **Exploration and Exploitation**: The epsilon-greedy approach ensures the agent explores initially and gradually shifts to exploitation as it learns the optimal policy.

- **Adaptability**: The algorithm is implemented to work across various environments with configurable parameters such as learning rate, discount factor, and epsilon decay rate.

## How It Works

### Training Phase
1. **Initialization**:
   - The Q-table is initialized to zeros (or small random values).
   - Parameters such as learning rate (\( \alpha \)), discount factor (\( \gamma \)), and epsilon are set.

2. **Action Selection**:
   - The agent observes the current state.
   - It chooses an action based on the epsilon-greedy strategy.

3. **Update Rule**:
   - After taking the action, the agent observes the reward and the next state.
   - The Q-value for the state-action pair is updated using the Bellman equation.

4. **Epsilon Decay**:
   - Epsilon is reduced gradually after each episode to focus more on exploitation as the training progresses.

### Testing Phase
- In the testing phase, the agent uses the learned Q-table to select the optimal actions without further updates.
- The epsilon is typically set to 0 to ensure purely greedy action selection.

## Advantages of Q-Learning with Epsilon-Greedy
- **Simple and Effective**: Q-Learning is straightforward to implement and works well in discrete action spaces.
- **Exploration-Exploitation Balance**: The epsilon-greedy strategy ensures the agent explores sufficiently before converging to an optimal policy.
- **Model-Free**: The agent does not require a model of the environment, making it versatile.

## Use Cases
Q-Learning with epsilon-greedy is widely used in applications such as:
- Game playing (e.g., solving grid-world problems, learning to play simple games).
- Pathfinding tasks (e.g., navigating mazes).
- Decision-making problems where the state and action spaces are discrete.

## How to Run

1. **Set Environment**:
   - Configure the environment parameters, including state and action space sizes.

2. **Train the Agent**:
   - Run the training phase where the Q-table is iteratively updated.

3. **Test the Agent**:
   - Use the learned Q-table to evaluate the agent's performance in the environment.

## Dependencies
- `numpy`
- Python 3.x

## Contributing
Feel free to contribute by improving the algorithm, adding new features, or testing it in different environments.

## License
This project is open-sourced under the MIT License. See the LICENSE file for details.
