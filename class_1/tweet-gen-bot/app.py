from flask import Flask
import sentence

app = Flask(__name__)

@app.route('/')
def hello_world():
    return sentence.create(10)
