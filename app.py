import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/current-time')
def current_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"The current time is {current_time}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
