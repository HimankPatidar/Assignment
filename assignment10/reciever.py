

import socket

def receive_file(save_path, local_ip, local_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    complete_address = (local_ip, local_port)
    s.bind(complete_address)
    print("Waiting for file...")

    # Receive the start signal to begin file reception
    data, addr = s.recvfrom(1024)
    if data == b'START_FILE_TRANSMISSION':
        with open(save_path, "wb") as file:
            while True:
                data, addr = s.recvfrom(1024)
                if data == b"END_FILE_TRANSMISSION":
                    break
                file.write(data)
        print("File received successfully.")

# Example usage
save_path = "./recieved/1.pdf"
local_ip = "192.168.1.55"
local_port = 4343
receive_file(save_path, local_ip, local_port)
