from flask import Flask, request, render_template_string, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session management

# Sample username and password
USERNAME = "sherlock"
PASSWORD = "sherlock123"
FLAG = "flag{the_game_is_afoot}"

@app.route("/", methods=["GET", "POST"])
def terminal():
    # Initialize session variables if not already set
    if 'username' not in session:
        session['username'] = None
    if 'password' not in session:
        session['password'] = None
    error_message = ""

    if request.method == "POST":
        input_text = request.form.get("input_text")

        if session['username'] is None:
            # Check username
            if input_text == USERNAME:
                session['username'] = input_text
            else:
                error_message = "Invalid username. Try again."
        elif session['password'] is None:
            # Check password
            if input_text == PASSWORD:
                session['password'] = input_text
                return render_template_string("""
                    <html>
                        <head>
                            <style>
                                body {
                                    background-color: black;
                                    color: lightgreen;
                                    font-family: 'Courier New', monospace;
                                    padding: 20px;
                                }
                                .terminal {
                                    white-space: pre-wrap;
                                }
                            </style>
                        </head>
                        <body>
                            <div class="terminal">
$ Enter username: {{ username }}
$ Enter password: {{ password }}
$ Correct! Here's the flag:
{{ flag }}
                            </div>
                        </body>
                    </html>
                """, username=session['username'], password=session['password'], flag=FLAG)

            else:
                error_message = "Invalid password. Try again."

    # Determine which prompt to show
    if session['username'] is None:
        prompt = "Enter username: "
    elif session['password'] is None:
        prompt = "Enter password: "
    else:
        prompt = ""

    return render_template_string("""
        <html>
            <head>
                <style>
                    body {
                        background-color: black;
                        color: lightgreen;
                        font-family: 'Courier New', monospace;
                        padding: 20px;
                    }
                    .terminal {
                        white-space: pre-wrap;
                    }
                </style>
            </head>
            <body>
                <div class="terminal">
$ {{ error_message }}
$ {{ prompt }}
<form method="POST">
    <input type="text" name="input_text" placeholder="Enter text" style="background: black; color: lightgreen; border: none; outline: none; font-family: 'Courier New', monospace; font-size: 16px; width: 100%;" autofocus required><br>
</form>
                </div>
            </body>
        </html>
    """, error_message=error_message, prompt=prompt)

if __name__ == "__main__":
    app.run(debug=True)
