from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# Correct username and password
correct_username = "sherlock"
correct_password = "sherlock-ed"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == correct_username and password == correct_password:
        return jsonify({"success": True, "flag": "IET{$$MB}"})
    elif username != correct_username:
        return jsonify({"success": False, "message": "Incorrect username. Try again."})
    elif password != correct_password:
        return jsonify({"success": False, "message": "Incorrect password. Try again."})

if __name__ == '__main__':
    app.run(debug=True)
