import numpy as np


class StockTrajectories:
    def __init__(self, S, T, r, q, sigma, steps, N):
        self.S = S
        self.T = T
        self.r = r
        self.q = q
        self.sigma = sigma
        self.steps = steps
        self.N = N

    def geometric_brownian_motion(self):
        dt = self.T / self.steps
        St = np.log(self.S) + np.cumsum(((self.r - self.q - self.sigma**2 / 2) * dt +
                                         self.sigma * np.sqrt(dt) * np.random.normal(size=(self.steps, self.N))), axis=0)
        return np.exp(St)

    def geometric_brownian_motion_antithetic_variables(self):
        dt = self.T / self.steps
        Z = np.random.normal(size=(self.steps, self.N))
        St = np.zeros((self.steps, self.N, 2))

        St[:, :, 0] = np.log(self.S) + np.cumsum(((self.r - self.q - \
                             self.sigma**2 / 2) * dt + self.sigma * np.sqrt(dt) * Z), axis=0)
        St[:, :, 1] = np.log(self.S) + np.cumsum(((self.r - self.q - \
                             self.sigma**2 / 2) * dt - self.sigma * np.sqrt(dt) * Z), axis=0)
        return np.exp(St)
