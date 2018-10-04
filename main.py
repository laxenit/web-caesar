from flask import Flask, requeat
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            p.error {{
                color: red:
            }}
        </style>
    </head>
    <body>
    <form method="post"
        <div>
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0">
            <p class="error"></p>
        </div>
        <textarea name="text" placeholder="enter message to encrypt:">{0}</textarea>
        <br>
        <input type="submit">
       </form?
    </body>
</html>"""

    @app.route("/")
    def index():
        return form.format("")

@app.route ("/", method=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    rot_text = str(request.form['text'])
    encrypt_text = rotate_string(rot_text, rot)
    return form.format(encrypt_text)

app.run()