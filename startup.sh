#!/bin/bash
apt update
apt install -y python3-pip
pip3 install flask
mkdir -p /opt/flaskapp
cd /opt/flaskapp
echo "from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef hello(): return 'Hello from GCP! :)'\napp.run(host='0.0.0.0', port=5000)" > app.py
nohup python3 app.py &