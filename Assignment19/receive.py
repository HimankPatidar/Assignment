import socket

def main():
    # UDP server details
    udp_ip = "192.168.1.55"
    udp_port = 9999
    
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the socket to the address
    udp_socket.bind((udp_ip, udp_port))
    
    print("UDP server started. Waiting for messages...")
    
    while True:
        # Receive data from the client
        data, addr = udp_socket.recvfrom(1024)
        
        # Decode and print the received data
        decoded_data = data.decode()
        print("Received data from {}: {}".format(addr, decoded_data))
        
        # Save the received data to a file
        save_to_file(decoded_data, addr[0])

def save_to_file(data, sender_ip):
    filename = f"{sender_ip}_messages.txt"
    with open(filename, "a") as file:
        file.write(data)
        file.write("\n\n")

if __name__ == "__main__":
    main()
