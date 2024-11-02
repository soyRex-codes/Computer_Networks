a.	Name: Rajkumar Kushwaha and email address: rk33s@missouristate.edu
b.	Class name: Computer Network(CSC565), date: 11/1/2024 and assignment title: Progassignment2
c.	Names and descriptions of all files submitted:
    1. Webserver.py  : contains the well documented code
    2. README.txt file with all the descritpion of codes, files and compiling instructions
    3. screenshots of host showing sucessfully receiving contents
    4. HelloWorld.html file : for our Webserver to be requested by host

d.	Detailed instructions for compiling and running my client and server programs.
    INSTRUCTIONS : Download the zip file, unzip it, open all file in the same directory and compile Webserver.py, 
    you should see: 
                   Hostname: yourDevicehostname eg: Rajkumar Laptop
                   IP Address: yourDeviceIPaddress eg: 192.168.4.23
                   listening for connection
                   The server is ready to receive:

   This ensures that server is running and is connected and ready to receive file request from host,
   then use another device to access the server, From another host, open a browser and provide the corresponding URL. 
   InMYCASE MY URL: http://192.168.4.23:6789/HelloWorld.html  
    where ‘HelloWorld.html’ is the name of the file I placed in my same server directory where Webserver.py is located. 
     and 6789 is the port number used, where  192.168.4.23 is the Ip address of my device where server is running.
      Once you enter the url on another hostdevice browser, you should sucessfully see the contents of the requested file.
      other case, user wrong file name to get the 404 file not found error.    

e. Modifications to the Code:
 -->   from socket import *  modifying to import socket  #modifying this piece of code since it is causing issue with when i try to get my host ipaddress

       --> while #Creating a TCP server socket
           modified #serverSocket = socket(AF_INET, SOCK_STREAM) to serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #as import was changed
      

