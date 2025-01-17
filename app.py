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
        if username == USERNAME:
            if password == PASSWORD:
                return jsonify({"status": "success", "flag": FLAG})
            else:
                return jsonify({"status": "error", "message": "Invalid password"})
        else:
            return jsonify({"status": "error", "message": "Invalid username"})
    
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
                </style>
            </head>
            <body>
                <div class="terminal">
                    Welcome to the Interactive Terminal<br><br>
                    <div id="output"></div>
                    <input id="input" type="text" autofocus />
                </div>
                <script>
                    let stage = 0; // 0 for username, 1 for password
                    let username = '';
                    let password = '';
                    
                    document.getElementById('input').addEventListener('keydown', function(e) {
                        if (e.key === 'Enter') {
                            let inputText = document.getElementById('input').value;
                            let outputDiv = document.getElementById('output');
                            
                            if (stage === 0) {
                                // Handle username
                                username = inputText;
                                outputDiv.innerHTML += '$ Username: ' + username + '<br>';
                                outputDiv.innerHTML += '$ Enter password: <input id="input" type="password" autofocus /><br>';
                                stage = 1;
                            } else if (stage === 1) {
                                // Handle password
                                password = inputText;
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
                                        stage = 0;
                                        outputDiv.innerHTML += '$ Enter username: <input id="input" type="text" autofocus /><br>';
                                    }
                                });
                            }
                            
                            // Clear input field
                            document.getElementById('input').value = '';
                        }
                    });
                </script>
            </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
