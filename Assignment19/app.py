
# from flask import Flask, render_template, request
# import socket

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/submitdata', methods=['POST'])
# def submitdata():
#     if request.method == "POST":
#         name = request.form['Name']
#         email = request.form['Email']
#         subject = request.form['Subject']
#         message = request.form['Message']
        
#         data = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        
        
#         send_to_udp_server(data)
        
#         return "Form data sent successfully."

# def send_to_udp_server(data):
    
#     udp_ip = "192.168.1.55"
#     udp_port = 9999
    
    
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
#     udp_socket.sendto(data.encode(), (udp_ip, udp_port))
  
#     udp_socket.close()

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submitdata', methods=['POST'])
def submitdata():
    if request.method == "POST":
        name = request.form['Name']
        email = request.form['Email']
        subject = request.form['Subject']
        message = request.form['Message']
        
        # Prepare the data to send to the UDP server
        data = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
        
        # Send the data to the UDP server
        send_to_udp_server(data)
        
        # Send email to specific address
        send_email(name, email, subject, message)
        
        return "Form data sent successfully."

def send_to_udp_server(data):
    # UDP server details
    udp_ip = "192.168.1.55"
    udp_port = 9999
    
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Send the data to the UDP server
    udp_socket.sendto(data.encode(), (udp_ip, udp_port))
    
    # Close the socket
    udp_socket.close()

def send_email(name, email, subject, message):
    # Email server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Change to your SMTP port
    receiver_email = 'patiadarhimank004@gmail.com'  # Change to your recipient's email address
    password = ""
    
    # Create a message
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    # Add message body
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(send_email, password)
        server.message(msg)

if __name__ == '__main__':
    app.run(debug=True)
