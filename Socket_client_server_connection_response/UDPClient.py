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
        # Create a UDP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Send the loan details to the server
        message = f"{loan_amount} {years} {interest_rate}"
        client_socket.sendto(message.encode(), (server_host, 13000))

        # Receive the result from the server
        data, server = client_socket.recvfrom(1024)
        print("Received from server:", data.decode())

        # Close the socket
        client_socket.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
