# app.py
from flask import Flask
import os
import threading
import time
import main  # Import your main module

app = Flask(__name__)

def run_main():
     try:
        main.main()  # Call the main function from main.py
     except Exception as e:
        print(f"Error in main: {e}")

@app.route('/')
def home():
    return "Welcome to the main app!"

if __name__ == '__main__':
    # Start the main function in a separate thread
    threading.Thread(target=run_main, daemon=True).start()

    # Bind to the PORT environment variable for deployment
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
