# About

This script projects the price of any stock for the next following year onto a graph. It uses the standard deviation and mean of the changes in price to predict what the stock price trend could appear to be be for x amount of times. It then shows the graph using matplot and gets stock data from yahoo finance. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install Stock-Price-Predictor
```

## Usage

```python
data = yf.download("TSLA")

```
You can put any stock ticker symbol into the quotations, it just has to be real and in all caps

```python
for i in range(50):
    sim = np.random.normal(mu, sigma, 252)
    initial = data['Adj Close'].iloc[-1]
    sim_prices = initial * (sim+1).cumprod()
    plt.plot(sim_prices)
```


## Screenshot
![Screenshot](https://github.com/DevJChen/Stock-Price-Predictor/edit/screenshot.png?raw=true)
## License

[MIT](https://choosealicense.com/licenses/mit/)
