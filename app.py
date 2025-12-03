# app.py
from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # This gets the name of the Container (or Laptop)
    container_id = socket.gethostname()
    return f"👋 Hello from Python! Running inside ID: {container_id}\n"

if __name__ == "__main__":
    # host='0.0.0.0' is CRITICAL for Docker
    # It means "Listen to connections from outside this computer"
    app.run(host='0.0.0.0', port=5000)