import numpy as np

class MWagent:
    def __init__(self, n_actions, gamma):
        self.num_actions = n_actions
        self.weights = np.ones(n_actions)
        self.gamma = gamma
        self.action_space = np.array(range(self.num_actions))

    def get_action(self):
        probs = (1 - self.gamma) * self.weights / np.sum(self.weights) + self.gamma / self.num_actions
        return np.random.choice(self.action_space, p=probs)

    def update_weights(self, action, score):
        x_hat = np.zeros(self.num_actions)
        probs = (1 - self.gamma) * self.weights / np.sum(self.weights) + self.gamma / self.num_actions
        x_hat[action] = score / probs[action]
        self.weights *= np.exp(self.gamma * x_hat / self.num_actions)
        self.weights /= np.sum(self.weights)
