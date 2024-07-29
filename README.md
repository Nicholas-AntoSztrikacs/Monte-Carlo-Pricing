# Monte-Carlo-Pricing
This repository contains a Python program for option pricing via Monte Carlo methods. This repository is not meant as a serious option pricer, but rather was created as a tool to learn the theory of option pricing models, and as a testbed to write better software. 

The Monte-Carlo-Pricing repository is used to price vanilla, exotic, and path-dependent options and is written within a flexible OOP framework such that adding new functionalities to the model is straightforward.  

## Getting Started 
If you would like to use or add to this repository you can either clone or download it

```
git clone https://github.com/Nicholas-AntoSztrikacs/Monte-Carlo-Pricing
```

The main file in this repository is `monte_carlo_pricing.py` which when run, prompts the user to input values for the financial derivative such as the stock price `S0`, the strike price `K`, the time to expiration `T`, the annualized risk free interest rate `r`, the annualized volatility `sigma`, and the dividend yield `q`. Following this, an instance of the `StockTrajectories` class is created, from which a collection of sample paths of the geometric Brownian motion is created, at which point, an instance of the `Payoff` class is generated from which a wide variety of payoff functions can be computed, and priced via an instance of the `Valuate` class. The program then outputs the price of the option, the 99% confidence interval, as well a series of plots describing the contract. 

## Prerequisites
This repository makes use of external packages: `numpy`, `scipy`, and `matplotlib`. You can install them using `pip` with the following code:
```
pip install numpy scipy matplotlib
```

## To-Do
1) Implement market models beyond the geometric Brownian motion
    * Price derivatives via stochastic volatility models

2) Add a new class to deal with other random number generators beyond the Mersenne-Twister
    * Implement quasi random number generation to perform quasi Monte Carlo

3) Add futher variance reduction tools in the Monte Carlo simulations
    * Control variates
    * Importance sampling
