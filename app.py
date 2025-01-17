from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sample username and password
USERNAME = "sherlock"
PASSWORD = "sherlock-ed"
FLAG = "IET{$$MB}"

@app.route("/", methods=["GET", "POST"])
def terminal():
    # Variables to store the state of input prompts
    username = None
    password = None
    error_message = ""
    
    if request.method == "POST":
        if not username:
            # If username is not yet entered, check the entered username
            entered_username = request.form.get("input_text")
            if entered_username == USERNAME:
                username = entered_username
            else:
                error_message = "Invalid username. Try again."
        elif not password:
            # If username is correct, check the entered password
            entered_password = request.form.get("input_text")
            if entered_password == PASSWORD:
                password = entered_password
            else:
                error_message = "Invalid password. Try again."
        
        if username and password:
            return render_template_string("""
                <html>
                    <head>
                        <style>
                            body {
                                background-color: black;
                                color: green;
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
Welcome to the Interactive Terminal

$ {{ error_message }}
$ {{ prompt }}
<form method="POST">
    <input type="text" name="input_text" placeholder="Enter text" style="background: black; color: green; border: none; outline: none; font-family: 'Courier New', monospace; font-size: 16px; width: 100%;" autofocus required><br>
</form>
                </div>
            </body>
        </html>
    """, error_message=error_message, prompt=prompt, username=username)

if __name__ == "__main__":
    app.run(debug=True)
