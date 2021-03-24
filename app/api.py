from flask import Flask,jsonify,request,render_template, make_response
from flask_cors import CORS, cross_origin
from predict import prediction


app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def index():
   return("welcome to love letter generation pytorch model")

@app.route("/ririlyric", methods = ['GET', 'POST'])
def textgen():
    text_g = request.form['content']
    lyric = prediction(text_g)
    return lyric



if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 8080, debug=True)