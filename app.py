from flask import *
import gtts
#from pygame import mixer


app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome to our API" 
"""
@app.route('/texttospeech/' , methods = ['PUT'])
def texttospeech():
	if request.method == 'PUT':
		filename = images.save(request.file['img1'])
		return filename
"""

if __name__ == '__main__':
	app.run(port =  7000 , debug = True ,use_reloader = True)
