from flask import Flask , request , Response
#import gtts
#from pygame import mixer


app = Flask(__name__)

@app.route('/')
def index():
	return "Welcome to our API" 
"""
@app.route('/texttospeech/' , methods = ['POST'])
def texttospeech():
	if request.method == 'POST':
		return Response(response={"apple" : "iphone 11"} ,status = 200)
"""
if __name__ == '__main__':
	app.run()
