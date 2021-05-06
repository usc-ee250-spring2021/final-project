import requests
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import socket

"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""

api_key = '2CGM6KNUEZ0KQUSL'  # AlphaVantage API Key

#from .alphavantage import AlphaVantage as av






def main():
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
 HOST = '20.64.240.125'  # The server's hostname or IP address
 PORT = 8080      # The port used by the server

 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    
    # TODO: Get user input and send it to the server using your TCP socket
    user_input = input("Name of stock (ie AAPL, MSFT, BTC): ")
    s.sendall(user_input.encode())
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=user_input,interval='1min', outputsize='full')
    print(data)
    data['4. close'].plot()
    plt.title('Intraday Times Series for the ' + user_input +' stock (1 min)')
    plt.show()
    # TODO: Receive a response from the server and close the TCP connection
    response = s.recv(1024)
    print(repr(response.decode()))
    s.close()
    

if __name__ == '__main__':
    main()

# OpenWeatherMap API: https://openweathermap.org/current

# TODO: Sign up for an API key


