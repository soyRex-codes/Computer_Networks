# Import socket module
#from socket import *  #modifying this piece of code since it is causing issue with when i try to get my host ipaddress
import socket
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

#socket defined#
#serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## Creating a TCP server socket

# Get the hostname of the machine
hostname = socket.gethostname()
# Get the IP address associated with the hostname
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port

#Fill in start
serverSocket.bind(("", serverPort)) # Binded the socket to server address and server port
#Fill in end

# Listen to at most 1 connection at a time
serverSocket.listen(1)
print("listening for connection")

# Server should be up and running and listening to the incoming connections

while True:
    print('The server is ready to receive: \n')
    
    #Fill in start 
	# Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    
        #The accept() method waits for an incoming connection from a client
        # When a client connects, it returns a tuple containing: connectionSocket: A new socket object specifically for this connection 
        # addr: The address of the client, containing (host, port)
    print(f"Connection established with {addr}")
        #Fill in end

	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
    try:  
        # Receives the request message from the client
        message = connectionSocket.recv(1024).decode() #Decode the bytes using the codec registered for encoding.
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
        #Fill in start
        first_line = message.split('\n')[0] # Split the message into lines and get the first line (request line)
        path = first_line.split()[1] #our path contains the requested object's path
        print(f"Requested path: {path}")  # Log the requested path
                #Fill in end
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		#Fill in start 
        file_name = path[1:] # Get the file name by stripping the leading '/'
                #Fill in end
		# Store the entire contenet of the requested file in a temporary buffer
        #Fill in start
        with open(file_name, 'rb') as f: #HelloWorld.html is file name to be accessed
            buffer = f.read() 
        print(f"Serving file: {file_name}")
                #Fill in end
		# Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 
 
		# Send the content of the requested file to the connection socket: a communication link established between two computer systems over a network, allowing data to be exchanged.
        #Fill in start
        connectionSocket.send(buffer)
        print("File sent successfully.") 
                #Fill in end
		
		# Close the client connection socket
        connectionSocket.close()
    except IOError:
        #Fill in start 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) #Sends a proper HTTP response to the client 404 error
        #\r\n\r\n separates the header from the body
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode()) # Send HTTP response message for file not found
                        #Fill in end
			# Close the client connection socket
        connectionSocket.close()

#Indefinite Loop:
#The while True: loop means that the server will keep running and accepting new connections.
# The only way to reach the serverSocket.close() and sys.exit() lines is if the loop is
# exited,which does not happen in the normal operation of a server.
serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
