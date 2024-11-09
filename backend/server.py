# backend/server.py

from flask import Flask, request, Response
from flask_cors import CORS
import threading
import time
import json
from main import run_simulation

app = Flask(__name__)
CORS(app)

# Shared message list
messages = []

@app.route('/start', methods=['POST'])
def start():
    data = request.get_json()
    theme = data.get('theme')
    participant_pool = data.get('participant_pool')
    threading.Thread(target=run_simulation, args=(theme, participant_pool)).start()
    return {'status': 'Simulation started'}, 200

@app.route('/stream')
def stream():
    def event_stream():
        last_index = 0
        while True:
            if last_index < len(messages):
                msg = messages[last_index]
                last_index += 1
                yield f'data: {json.dumps(msg)}\n\n'
            time.sleep(0.1)
    return Response(event_stream(), mimetype="text/event-stream")

def add_message(sender, content):
    messages.append({'sender': sender, 'content': content})

# Modify main.py to call add_message when messages are generated
