from flask import Flask, request, jsonify, render_template
import urllib.parse

app = Flask(__name__)

# Store the username and password for authentication
valid_username = "sherlock"
valid_password = "sherlock-ed"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == valid_username and password == valid_password:
        return jsonify({"message": "Success", "flag": "IET{$$MB}"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
