

import socket

def send_file(file_path, receiver_ip, receiver_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target_ip = (receiver_ip, receiver_port)

<<<<<<< HEAD
    s.sendto(b"START_FILE_TRANSMISSION", target_ip)

=======
   
    s.sendto(b"START_FILE_TRANSMISSION", target_ip)

  
>>>>>>> 2ebf04d17a679b8d3b77d7e7c921abab9f8d4eac
    with open(file_path, "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            s.sendto(data, target_ip)

<<<<<<< HEAD
=======
 
>>>>>>> 2ebf04d17a679b8d3b77d7e7c921abab9f8d4eac
    s.sendto(b"END_FILE_TRANSMISSION", target_ip)
    s.close()
    print("File sent successfully.")


file_path = "./send/Assignment 3rd_DCN.pdf"
receiver_ip = "192.168.1.55"
receiver_port = 4343
send_file(file_path, receiver_ip, receiver_port)
