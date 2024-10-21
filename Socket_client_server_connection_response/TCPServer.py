import socket
import math

# Function to calculate the monthly payment using the formula
def calculate_payments(loan_amount, years, annual_rate):
    monthly_rate = (annual_rate / 100) / 12
    total_payments = years * 12
    # formula
    monthly_payment = (loan_amount * monthly_rate) / (1 - math.pow((1 / (1 + monthly_rate)), total_payments))
    total_payment = monthly_payment * total_payments
    return round(monthly_payment, 2), round(total_payment, 2)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 13000))
    server_socket.listen(5)
    print("TCP Server listening on port 13000...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        try:
            # Receive the client's request
            data = conn.recv(1024).decode()
            if not data:
                break

            # Parse the client's request (loan_amount, years, interest_rate)
            loan_amount, years, interest_rate = map(float, data.split())
            
            # Calculate the monthly and total payments using the corrected formula
            monthly_payment, total_payment = calculate_payments(loan_amount, int(years), float(interest_rate))

            # Send the results back to the client
            response = f"Monthly payment: ${monthly_payment}, Total payment: ${total_payment}"
            conn.sendall(response.encode())
        except Exception as e:
            conn.sendall(f"Error: {str(e)}".encode())
        finally:
            # Close the client connection and continue listening for new requests
            conn.close()

if __name__ == "__main__":
    main()
