from stock_trajectories import StockTrajectories
from payoff import Payoff
from valuate import Valuate


# input model parameters
print("Please choose the parameters for the simulation")
S = float(input("Initial stock price: "))
K = float(input("Strike price: "))
T = float(input("Time to expiration in years: "))
r = float(input("Risk free annualized interest rate: "))
sigma = float(input("Annualized volatility: "))
q = float(input("Dividend yield: "))
steps = 100  # time steps
N = 1000000  # number of trials

# implementation
path = StockTrajectories(S, T, r, q, sigma, steps, N)  # generate a path
payoff = Payoff(K, path.geometric_brownian_motion())  # Obtain payoff info
price = Valuate(payoff.European_call(), T, r)  # Valuate a derivative of choice

# outputs
print("The cost of the option is: ", price.price())
price.confidence_interval(alpha=0.01)

payoff.plot_trajectory(1000)
payoff.plot_histogram('Terminal')
price.plot_payoff()
