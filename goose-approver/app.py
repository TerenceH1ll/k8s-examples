from flask import Flask
import os
import random

app = Flask(__name__)

@app.route("/")
def home():
    wisdom = os.environ.get("GOOSE_WISDOM", "")
    messages = [m.strip() for m in wisdom.split("|") if m.strip()]

    if not messages:
        messages = [
            "APPROVED: The goose said yes."
        ]

    choice = random.choice(messages)

    html = f"""
    <html>
    <head>
        <title>Corporate Goose Approval Service</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 50px;
                background: #f8f9fa;
            }}
            h1 {{
                font-size: 3em;
            }}
            .box {{
                background: white;
                width: 600px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🪿 Corporate Goose</h1>
            <h2>{choice}</h2>
            <p>Refresh for another executive decision.</p>
        </div>
    </body>
    </html>
    """

    return html

@app.route("/healthz")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)