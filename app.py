from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize, sent_tokenize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    text = request.form['input_text']

    # Example: Tokenize the text
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    return render_template('result.html', words=words, sentences=sentences)

if __name__ == '__main__':
    app.run(debug=True)
