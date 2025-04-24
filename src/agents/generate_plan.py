import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from fetchai.communication import send_message_to_agent, parse_message_from_agent
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

client_identity = None
agent_response = None

load_dotenv()

def init_client():
    """Initialize and register the client agent."""
    global client_identity



@app.route('/request', methods=['POST'])
def send_data():
    """Send payload to the selected agent based on provided address."""
    global agent_response
    agent_response = None

    



if __name__ == "__main__":
    load_dotenv()
    init_client()
    app.run(host="0.0.0.0", port=8001)