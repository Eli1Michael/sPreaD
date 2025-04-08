from flask import Flask
import os  # Add this import statement for os module

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"



if __name__ == "__main__":
    # Use the port from the environment variable (default to 5000 if not set)
    port = int(os.environ.get("PORT", 5000))
    # Set host to 0.0.0.0 for Heroku compatibility
    app.run(host="0.0.0.0", port=port, debug=True)