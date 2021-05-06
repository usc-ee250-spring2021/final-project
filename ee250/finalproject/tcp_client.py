"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
 #HOST = '10.211.55.4'  # The server's hostname or IP address
 #PORT = 49552      # The port used by the server
 HOST = '20.64.240.125'  # The server's hostname or IP address
 PORT = 8080

 with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    
    # TODO: Get user input and send it to the server using your TCP socket
    user_input = input("Message to send to server: ")
    s.sendall(user_input.encode())
    # TODO: Receive a response from the server and close the TCP connection
    data = s.recv(1024)
    print(repr(data.decode()))
    s.close()
    

if __name__ == '__main__':
    main()
