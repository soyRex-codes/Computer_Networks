NOTE: Names and descriptions of all files, with Detailed instructions for compiling and running the client and server
programs are given below.




//////////////////////
TCP
////////////////////////
1. TCPClient.py
/////////////////////////////
This client will Take input from the user (loan amount, loan term, and interest rate).
Send this data to the server using TCP sockets.
Receive the monthly payment and total payment from the server.
Display the results to the user.

/////////////////////////////
2. TCPServer.py
/////////////////////////////
This server will Listen for connections from clients.
For each connection, receive the loan data, compute the monthly and total payments, and send the result back to the client.

////////////////////////////////////////////////
HOW TO RUN TCP:
///////////////////////////////////
Start the server:
On your terminal, run: python TCPServer.py
On another terminal, Run the client, run:
python TCPClient.py <LOCALHOST> <loan_amount> <years> <interest_rate>

//COMMENT:  I ran both client and server on same machine so, i used localhost: python TCPClient.py 127.0.0.1 1000 30 4.0
//COMMENT:  Note: if you ran both client and server on same machine, use YOUR localhost
where as 127.0.0.1 is localhost/loopback IP address FOR MY MACHINE.

////////////////////////////////////////////////////
If client and server running on different machines:
////////////////////////////////////////////////////
Start the server:
On your terminal, run: python TCPServer.py
Run the client:
On another terminal, run:
python TCPClient.py <server_ip> <loan_amount> <years> <interest_rate>
For example: python TCPClient.py server_ip 150000 30 4.69
///////////////////////////////////////////////////


##########################
/////////////////////////
UDP
/////////////////////
The UDP version works similarly, but with a few key differences:

/////////////////////////////
1. UDPClient.py will send the loan information using UDP sockets.
/////////////////////////////
2. UDPServer.py will process this request and return the results.
/////////////////////////////

////////////////////////////////////////////////
HOW TO RUN UDP
////////////////////////////////////////////////
Start the UDP server:
On your terminal, run: python UDPServer.py
Run the UDP client, On another terminal, run:
//COMMENT: Note: I ran both client and server on same machine so, i used localhost: python UDPClient.py 127.0.0.1 15000 30 4.69
python UDPClient.py <LOCALHOST> <loan_amount> <years> <interest_rate>

////////////////////////////////////////////////////
If client and server running on different machines:
////////////////////////////////////////////////////
Start the UDP server:
On your terminal, run: python UDPServer.py
Run the UDP client, On another terminal, run:
python UDPClient.py <server_ip> <loan_amount> <years> <interest_rate>
Example: python UDPClient.py server_ip 150000 30 4.69
