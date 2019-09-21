from flask import *
#import gtts
#from pygame import mixer


app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome to our API" 

@app.route('/texttospeech/' , methods = ['PUT'])
def texttospeech():
	if request.method == 'PUT':
		return jsonify({"dowloaded" : request.files['img1']}

if __name__ == '__main__':
	app.run()
