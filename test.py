from flask import Flask
app = Flask(__name__)

@app.route('/lulu')
def hello_1():
	return 'Hello lulu!'
	
@app.route('/hudi')
def hello_2():
	return 'Hello hudi!'
	
if __name__ == '__main__':
	app.run()