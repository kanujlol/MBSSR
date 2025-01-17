from flask import Flask, render_template_string, request

app = Flask(__name__)

# Hardcoded credentials
USERNAME = "sherlock"
PASSWORD = "sherlock123"
FLAG = "flag{the_game_is_afoot}"

@app.route("/", methods=["GET", "POST"])
def terminal():
    # Initialize variables for username and password
    username = None
    password = None
    error_message = ""

    # Check if the form is submitted
    if request.method == "POST":
        if username is None:  # Check username first
            entered_username = request.form.get("username")
            if entered_username == USERNAME:
                username = entered_username
            else:
                error_message = "Invalid username. Try again."
        elif password is None:  # Then check password
            entered_password = request.form.get("password")
            if entered_password == PASSWORD:
                password = entered_password
            else:
                error_message = "Invalid password. Try again."

    # If both username and password are correct, show the flag
    if username and password:
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
                    </style>
                </head>
                <body>
                    <div class="terminal">
                        Welcome to the Interactive Terminal

                        $ Username: {{ username }}
                        $ Password: {{ password }}
                        $ Correct! Here's the flag:
                        {{ flag }}
                    </div>
                </body>
            </html>
        """, username=username, password=password, flag=FLAG)

    # If no username or password entered, ask for them
    if username is None:
        prompt = "Enter username: "
    elif password is None:
        prompt = "Enter password: "
    else:
        prompt = ""

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
                    Welcome to the Interactive Terminal

                    $ {{ error_message }}
                    $ {{ prompt }}
                    <form method="POST" action="/">
                        <input type="text" name="username" placeholder="Enter username" style="display: {{ 'none' if username else 'inline' }};" required autofocus><br>
                        <input type="password" name="password" placeholder="Enter password" style="display: {{ 'inline' if username else 'none' }};" required><br>
                    </form>
                </div>
            </body>
        </html>
    """, error_message=error_message, prompt=prompt, username=username)

if __name__ == "__main__":
    app.run(debug=True)
