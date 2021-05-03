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


class RMagent:
    def __init__(self, n_actions, mu):
        self.num_actions = n_actions
        self.weights = np.ones(n_actions)
        # diagonal will be null
        self.regrets = np.ones((n_actions, n_actions)) * -100000
        self.mu = mu
        self.action_space = np.array(range(self.num_actions))
        self.T = 0

    def get_action(self):
        probs = self.weights / np.sum(self.weights)
        print(probs)
        return np.random.choice(self.action_space, p=probs)

    def update_weights(self, action, scores):
        for swap in range(self.num_actions):
            if swap == action:
                continue
            self.regrets[action, swap] = self.T / (self.T + 1) * self.regrets[action, swap] + 1 / (self.T + 1) * (scores[swap] - scores[action])
        
        for a in range(self.num_actions):
            if a == action:
                # element-wise max to account for 'positive' requirement
                self.weights[a] = 1 - np.nansum(np.fmax(self.regrets[action, :], 0))
            else:
                self.weights[a] = np.max(self.regrets[action, a], 0) / self.mu
        self.T += 1
