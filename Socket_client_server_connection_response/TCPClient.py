import socket
import sys

def main():
    if len(sys.argv) != 5:
        print("Usage: Cal <server> <loan_amount> <years> <interest_rate>")
        sys.exit(1)

    server_host = sys.argv[1]
    loan_amount = sys.argv[2]
    years = sys.argv[3]
    interest_rate = sys.argv[4]

    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        client_socket.connect((server_host, 13000))

        # Send the loan details
        message = f"{loan_amount} {years} {interest_rate}"
        client_socket.sendall(message.encode())

        # Receive the result from the server
        data = client_socket.recv(1024)
        print("Received from server:", data.decode())

        # Close the socket
        client_socket.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
