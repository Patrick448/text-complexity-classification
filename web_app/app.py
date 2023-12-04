from flask import Flask, render_template, request
from model.text_classifier import classify
from model.text_generator import generate_text

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/send_text_form", methods=['POST'])
def send_text_form():
    text = request.form['text']
    category = classify(text)
    gen_texts = generate_text(text)
    return render_template('index.html',
                           category=category,
                           text=text,
                           gen_texts=gen_texts)