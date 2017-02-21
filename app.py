from flask import Flask
import tokenize
from histogram import Histogram
import sample
import sentence

app = Flask(__name__)
# histogram = Histogram()

@app.route('/')
def hello_world():
    tokens = tokenize.generate_tokens("sample-text.txt")
    histogram = Histogram(tokens)
    return sentence.create(30, histogram)

if __name__ == "__main__":
    app.run()
