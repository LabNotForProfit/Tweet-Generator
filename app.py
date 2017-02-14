from flask import Flask
import sentence

app = Flask(__name__)

@app.route('/')
def hello_world():
    dict = sentence.open_file()
    return sentence.create(10, dict)
if __name__ == "__main__":
    app.run()
