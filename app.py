from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    return send_file(os.path.join(os.getcwd(), 'web.html'))  

if __name__ == '__main__':
    app.run(debug=True)


