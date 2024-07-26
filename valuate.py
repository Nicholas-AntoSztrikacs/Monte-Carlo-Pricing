import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


class Valuate:
    def __init__(self, payoff, T, r):
        self.payoff = payoff
        self.payoff = self.safe_mean()
        self.T = T
        self.r = r

    def price(self):
        return np.exp(-self.r * self.T) * np.mean(self.payoff)

    def standard_error(self):
        mean = np.mean(self.payoff)
        M = len(self.payoff)
        sig = np.exp(-self.r * self.T) * \
            np.sqrt(np.sum((self.payoff - mean)**2) / (M - 1))
        return sig / np.sqrt(M)

    # pass alpha as a decimal. default is 95% confidence interval
    def confidence_interval(self, alpha=0.05):
        mean = self.price()
        std = self.standard_error()
        z_score = norm.ppf(1 - alpha / 2)
        return print(f"{100 *(1-alpha)}% confidence interval: ",
                     (mean - std * z_score, mean + std * z_score))

    # Function to take average of multiindex array
    def safe_mean(self):
        try:
            return np.mean(self.payoff, axis=1)
        except IndexError:
            return self.payoff

    # plot a histogram of the payoffs
    def plot_payoff(self):
        plt.figure()
        plt.hist(self.payoff[self.payoff != 0], bins=200,
                 density=True, fill=True, color='green')
        plt.axvline(
            self.price(),
            color='black',
            linestyle='--',
            linewidth=2.5,
            label='Average Price')
        plt.xlabel('Payoff')
        plt.ylabel('Count')
        plt.title('Hisogram of the payoffs')
        plt.legend()
        return
