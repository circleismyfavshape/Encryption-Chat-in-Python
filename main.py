import socket
import threading

import rsa 


choice = input("Do you want to host (1) or to connect (2): ")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.56.1",9999))
    server.listen()

    client, _ = server.accept()
    client.send(pub.save_pkcs1())
    partner_pub_pem = client.recv(1024)
    partner_pub = rsa.PublicKey.load_pkcs1(partner_pub_pem)
elif choice == "2":
    pub, priv = rsa.newkeys(512)
    ip = input("Enter server IP: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 9999))
    partner_pub_pem = client.recv(1024)
    partner_pub = rsa.PublicKey.load_pkcs1(partner_pub_pem)
    client.send(pub.save_pkcs1())
else: 
    exit()
 
def sending_messages(c):
    while True:
        message = input("")
        c.send (message.encode)
        print("You: "+message)

def receiving_messages(c):
    while True:
        print("Partner: "+c.recv(1024).decode())

threading.Thread(target=sending_messages, args=(client))
threading.Thread(target=receiving_messages, args=(client))