from flask import Flask
import tokenize
import cleanup
from histogram import Histogram
import sample
import sentence

app = Flask(__name__)
# histogram = Histogram()

@app.route('/')
def hello_world():
    tokens = tokenize.generate_tokens("sample-text.txt")
    clean_tokens = cleanup.clean_text(tokens)
    histogram = Histogram(clean_tokens)
    return sentence.create(10, histogram)

if __name__ == "__main__":
    app.run()
