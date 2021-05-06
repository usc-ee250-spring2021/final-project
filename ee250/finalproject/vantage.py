import requests

# OpenWeatherMap API: https://openweathermap.org/current

# TODO: Sign up for an API key
api_key = '2CGM6KNUEZ0KQUSL'  # AlphaVantage API Key

#from .alphavantage import AlphaVantage as av

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key=api_key, output_format='json')
data = ts.get_intraday(symbol='AAPL',interval='1min', outputsize='full')
#print(data)
data['4. close'].plot()
plt.title('Intraday Times Series for the AAPL stock (1 min)')
plt.show()
