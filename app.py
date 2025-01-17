from flask import Flask, request, render_template_string

app = Flask(__name__)

# Sample username and password
USERNAME = "sherlock"
PASSWORD = "sherlock123"
FLAG = "flag{the_game_is_afoot}"

@app.route("/", methods=["GET", "POST"])
def terminal():
    error_message = ""
    if request.method == "POST":
        # Get the username and password from the form
        entered_username = request.form.get("username")
        entered_password = request.form.get("password")

        # Check if the username and password are correct
        if entered_username == USERNAME and entered_password == PASSWORD:
            return render_template_string("""
                <html>
                    <body>
                        <pre>
Welcome to the Interactive Terminal

$ Enter username: {{ username }}
$ Enter password: {{ password }}
$ Correct! Here's the flag:
{{ flag }}
                        </pre>
                    </body>
                </html>
            """, username=entered_username, password=entered_password, flag=FLAG)
        else:
            error_message = "Invalid username or password. Try again."

    return render_template_string("""
        <html>
            <body>
                <pre>
Welcome to the Interactive Terminal

$ {{ error_message }}

$ Enter username: <form method="POST"><input type="text" name="username" placeholder="Enter username" required><br>
$ Enter password: <input type="password" name="password" placeholder="Enter password" required><br>
$ <button type="submit">Submit</button></form>
                </pre>
            </body>
        </html>
    """, error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)
