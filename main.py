import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

data = yf.download('TSLA')
returns = np.log(1+data['Adj Close'].pct_change())
mu, sigma = returns.mean(), returns.std()
for i in range(50):
    sim = np.random.normal(mu, sigma, 252)
    initial = data['Adj Close'].iloc[-1]
    sim_prices = initial * (sim+1).cumprod()
    plt.plot(sim_prices)
plt.show()