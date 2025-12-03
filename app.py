from flask import Flask
import socket
import os
import redis

app = Flask(__name__)

# CONFIGURATION:
# If 'REDIS_HOST' is set in the environment, use it. Otherwise, assume 'localhost'.
redis_host = os.getenv('REDIS_HOST', 'localhost')

# Connect to the Database
# (If the DB isn't running, this checks connection but won't crash immediately)
db = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    container_id = socket.gethostname()
    
    try:
        # Ask Database to increment the "visits" counter
        visits = db.incr('counter')
    except redis.exceptions.ConnectionError:
        visits = "<i>[Cannot connect to Database]</i>"

    return (
        f"👋 Hello! Running inside ID: {container_id}<br>"
        f"📈 Visitor Number: <b>{visits}</b>\n"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)