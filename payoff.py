import numpy as np
import matplotlib.pyplot as plt


class Payoff:
    def __init__(self, K, path):
        self.K = K
        self.path = path

    # Vanilla payoffs
    def European_call(self):
        return np.maximum(self.path[-1] - self.K, 0)

    def European_put(self):
        return np.maximum(self.K - self.path[-1], 0)

    def Cash_call(self):
        return 1 * (self.path[-1] >= self.K)

    def Cash_put(self):
        return 1 * (self.path[-1] <= self.K)

    def Asset_call(self):
        return self.path[-1] * (self.path[-1] >= self.K)

    def Asset_put(self):
        return self.path[-1] * (self.path[-1] <= self.K)

    # Add exotic/path-dependent payoffs
    def Lookback_call(self):
        return np.maximum(np.max(self.path, axis=0) - self.K, 0)

    def Lookback_put(self):
        return np.maximum(self.K - np.max(self.path, axis=0), 0)

    def Asian_arithmatic_call(self):
        return np.maximum(np.mean(self.path, axis=0) - self.K, 0)

    def Asian_arithmatic_put(self):
        return np.maximum(self.K - np.mean(self.path, axis=0), 0)

    # Plotting functions

    def plot_trajectory(self, N=20):
        plt.figure()
        plt.plot(self.path[:, 0:N])
        plt.xlabel('Time Increments')
        plt.ylabel('$S_t$')
        plt.title('Geometric Borownian Motion Path')
        plt.plot(
            np.mean(
                self.path,
                axis=1),
            linewidth=3,
            color='k',
            label='Average')
        return

    def plot_histogram(self, Style):
        plt.figure()
        if Style == "Terminal":
            n, bins, patches = plt.hist(self.path[-1], bins=250, density=True)
            plt.xlabel('$S_T$')
            plt.title('Distribution of $S_{T}$')

        if Style == "Max":
            n, bins, patches = plt.hist(
                np.max(self.path, axis=0), bins=250, density=True)
            plt.xlabel('$S_max$')
            plt.title('Distribution of $S_{max}$')

        if Style == "Asian":
            n, bins, patches = plt.hist(
                np.mean(self.path, axis=0), bins=250, density=True)
            plt.xlabel('$S_mean$')
            plt.title('Distribution of $S_{mean}$')

        plt.axvline(
            self.K,
            color='black',
            linestyle='--',
            linewidth=2.5,
            label='Strike Price')
        plt.ylabel('Count')
        plt.legend()
        for c, p in zip(bins, patches):
            if c > self.K:
                plt.setp(p, 'facecolor', 'green')
            else:
                plt.setp(p, 'facecolor', 'red')
        return
