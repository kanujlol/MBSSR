from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Hardcoded credentials
USERNAME = "sherlock"
PASSWORD = "sherlock123"
FLAG = "flag{the_game_is_afoot}"

@app.route("/", methods=["GET", "POST"])
def terminal():
    # Check if POST request is made for validation
    if request.method == "POST":
        username = request.json.get("username")
        password = request.json.get("password")
        
        # Validate username and password
        if username == USERNAME and password == PASSWORD:
            return jsonify({"status": "success", "flag": FLAG})
        elif username != USERNAME:
            return jsonify({"status": "error", "message": "Invalid username"})
        else:
            return jsonify({"status": "error", "message": "Invalid password"})
    
    # If not a POST request, show the terminal
    return render_template_string("""
        <html>
            <head>
                <style>
                    body {
                        background-color: black;
                        color: green;
                        font-family: 'Cousine', monospace;
                        padding: 20px;
                    }
                    .terminal {
                        white-space: pre-wrap;
                    }
                    input {
                        background-color: black;
                        color: green;
                        border: none;
                        border-bottom: 1px solid green;
                        font-family: 'Cousine', monospace;
                        font-size: 18px;
                    }
                    input:focus {
                        outline: none;
                    }
                    button {
                        background-color: green;
                        color: black;
                        border: none;
                        padding: 10px 20px;
                        font-family: 'Cousine', monospace;
                        font-size: 18px;
                        cursor: pointer;
                    }
                    button:hover {
                        background-color: #4CAF50;
                    }
                </style>
            </head>
            <body>
                <div class="terminal">
                    Welcome to the Interactive Terminal<br><br>
                    <div id="output"></div>
                    <input id="username" type="text" placeholder="Username" autofocus /><br>
                    <input id="password" type="password" placeholder="Password" /><br>
                    <button id="submitBtn" onclick="submitCredentials()">Submit</button>
                </div>
                <script>
                    function submitCredentials() {
                        var username = document.getElementById('username').value;
                        var password = document.getElementById('password').value;
                        
                        // Display the entered credentials
                        var outputDiv = document.getElementById('output');
                        outputDiv.innerHTML += '$ Username: ' + username + '<br>';
                        outputDiv.innerHTML += '$ Password: ' + password + '<br>';
                        
                        // Send username and password to Flask for validation
                        fetch('/', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({username: username, password: password})
                        })
                        .then(response => response.json())
                        .then(data => {
                            if (data.status === "success") {
                                outputDiv.innerHTML += 'Correct! Flag: ' + data.flag + '<br>';
                            } else {
                                outputDiv.innerHTML += data.message + '<br>';
                            }
                        });
                    }
                </script>
            </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
