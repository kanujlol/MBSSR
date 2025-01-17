from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sample username and password
USERNAME = "sherlock"
PASSWORD = "sherlock123"
FLAG = "flag{the_game_is_afoot}"

@app.route("/", methods=["GET", "POST"])
def terminal():
    # Initialize variables to keep track of input
    if 'username' not in request.cookies:
        session_data = {
            'username': None,
            'password': None,
            'error_message': ""
        }
    else:
        session_data = {
            'username': request.cookies.get('username'),
            'password': request.cookies.get('password'),
            'error_message': ""
        }

    if request.method == "POST":
        input_text = request.form.get("input_text")

        if session_data['username'] is None:
            # Check username
            if input_text == USERNAME:
                session_data['username'] = input_text
            else:
                session_data['error_message'] = "Invalid username. Try again."
        elif session_data['password'] is None:
            # Check password
            if input_text == PASSWORD:
                session_data['password'] = input_text
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
$ Correct! Here's the flag:
{{ flag }}
                            </div>
                        </body>
                    </html>
                """, flag=FLAG)

            else:
                session_data['error_message'] = "Invalid password. Try again."

    # Determine which prompt to show
    if session_data['username'] is None:
        prompt = "Enter username: "
    elif session_data['password'] is None:
        prompt = "Enter password: "
    else:
        prompt = ""

    response = render_template_string("""
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
    """, error_message=session_data['error_message'], prompt=prompt)

    # Save the session data in cookies
    response.set_cookie('username', session_data['username'])
    response.set_cookie('password', session_data['password'])

    return response

if __name__ == "__main__":
    app.run(debug=True)
