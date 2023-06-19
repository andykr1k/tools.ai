from flask import Flask
from flask import render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def home():
    return 'hello world'

@app.route('/chat')
@cross_origin()
def chat():
    return 'chat'

@app.route('/text')
@cross_origin()
def text():
    return 'text'

@app.route('/video')
@cross_origin()
def video():
    return 'video'