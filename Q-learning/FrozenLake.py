import numpy as np
import gym
import json


class QLearningAgent:
    def __init__(self, state_space_size, action_space_size, learning_rate=0.1, discount_factor=0.9,
                 exploration_rate=1.0, exploration_decay=0.995, min_exploration_rate=0.01):
        self.state_space_size = state_space_size
        self.action_space_size = action_space_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.min_exploration_rate = min_exploration_rate

        # 初始化Q值表
        self.q_table = np.zeros((state_space_size, action_space_size))

    def state_to_hash(self, state):
        # 将状态转换为哈希值，支持元组和字典
        return hash(json.dumps(state, sort_keys=True))

    def select_action(self, state):
        # 以epsilon-greedy策略选择动作
        state_hash = self.state_to_hash(state)
        state_index = int(state_hash) % self.state_space_size
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.action_space_size)
        else:
            return np.argmax(self.q_table[state_index, :])

    def update_q_table(self, state, action, reward, next_state, done):
        # Q-learning更新规则
        state_hash = self.state_to_hash(state)
        state_index = int(state_hash) % self.state_space_size

        next_state_hash = self.state_to_hash(next_state)
        next_state_index = int(next_state_hash) % self.state_space_size

        if not done:
            max_q_next = np.max(self.q_table[next_state_index, :])
            new_q_value = (1 - self.learning_rate) * self.q_table[state_index, action] + \
                          self.learning_rate * (reward + self.discount_factor * max_q_next)
        else:
            # 对于终止状态，Q值的更新更简单
            new_q_value = (1 - self.learning_rate) * self.q_table[state_index, action] + \
                          self.learning_rate * reward

        # 更新Q值表
        self.q_table[state_index, action] = new_q_value

    def decay_exploration_rate(self):
        # 衰减探索率
        self.exploration_rate = max(self.min_exploration_rate, self.exploration_rate * self.exploration_decay)


class QLearningAgent:
    def __init__(self, state_space_size, action_space_size, learning_rate=0.1, discount_factor=0.9,
                 exploration_rate=1.0, exploration_decay=0.995, min_exploration_rate=0.01):
        self.state_space_size = state_space_size
        self.action_space_size = action_space_size
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.min_exploration_rate = min_exploration_rate

        # 初始化Q值表
        self.q_table = np.zeros((state_space_size, action_space_size))

    def select_action(self, state):
        # 以epsilon-greedy策略选择动作
        state_hash = hash(state)
        state_index = int(state_hash) % self.state_space_size
        if np.random.rand() < self.exploration_rate:
            return np.random.choice(self.action_space_size)
        else:
            return np.argmax(self.q_table[state_index, :])

    def update_q_table(self, state, action, reward, next_state, done):
        # Q-learning更新规则
        state_hash = hash(state)
        state_index = int(state_hash) % self.state_space_size

        next_state_hash = hash(next_state)
        next_state_index = int(next_state_hash) % self.state_space_size

        if not done:
            max_q_next = np.max(self.q_table[next_state_index, :])
            new_q_value = (1 - self.learning_rate) * self.q_table[state_index, action] + \
                          self.learning_rate * (reward + self.discount_factor * max_q_next)
        else:
            # 对于终止状态，Q值的更新更简单
            new_q_value = (1 - self.learning_rate) * self.q_table[state_index, action] + \
                          self.learning_rate * reward

        # 更新Q值表
        self.q_table[state_index, action] = new_q_value

    def decay_exploration_rate(self):
        # 衰减探索率
        self.exploration_rate = max(self.min_exploration_rate, self.exploration_rate * self.exploration_decay)


if __name__ == "__main__":
    # 创建一个包含字典状态的环境（示例环境）

    # 创建FrozenLake环境
    env = gym.make('FrozenLake-v1', render_mode="rgb_array")

    # 创建Q-learning代理
    agent = QLearningAgent(state_space_size=env.observation_space.n, action_space_size=env.action_space.n)

    num_episodes = 1000

    for episode in range(num_episodes):
        state = env.reset()
        total_reward = 0

        while True:
            # 代理选择动作
            action = agent.select_action(state)

            # 环境执行动作，得到奖励和下一个状态
            next_state, reward, done, _,_ = env.step(action)

            # 更新Q值
            agent.update_q_table(state, action, reward, next_state, done)

            # 更新当前状态
            state = next_state

            # 累积奖励
            total_reward += reward

            if done:
                break

        # 衰减探索率
        agent.decay_exploration_rate()

        print(f"Episode {episode + 1}, Total Reward: {total_reward}")

    # 关闭环境
    env.close()
