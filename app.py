from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sample username and password
USERNAME = "sherlock"
PASSWORD = "sherlock123"
FLAG = "flag{the_game_is_afoot}"

@app.route("/", methods=["GET", "POST"])
def terminal():
    username = None
    password = None
    error_message = ""
    
    if request.method == "POST":
        # First check for username
        if not username:
            entered_username = request.form.get("username")
            if entered_username == USERNAME:
                username = entered_username
            else:
                error_message = "Invalid username. Try again."
        # Then check for password if username is correct
        elif not password:
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

                            $ Enter username: {{ username }}
                            $ Enter password: {{ password }}
                            $ Correct! Here's the flag:
                            {{ flag }}
                        </div>
                    </body>
                </html>
            """, username=username, password=password, flag=FLAG)

    # If no username or password entered, ask for them
    if not username:
        prompt = "Enter username: "
    elif not password:
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
