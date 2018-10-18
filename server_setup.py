#!flask/bin/python
from flask import Flask, jsonify, request
import subprocess
import sys

app = Flask(__name__)


#@app.route('/cowsay/api/v1.0/saysomething', methods=['GET'])
#def cow_say():
#    data=subprocess.check_output(["cowsay","Hello student"])
#    return data


def helloWorld():
    return 'Hello, QTLaaS is almost running!'

def helloWorld2():
    return 'Hello, you are AMAZING at this!'

#If 1 = seyup new netowork
#If 2 = addd worker
#If 3 = rm worker
#if 4 = rm netowork

@app.route('/', methods=['GET'])
def serverOption():
	option = request.form['option']

	if(option == "1"):
		return 'Hello, QTLaaS is almost running!'#setup server
	else:
		return 'Hello, you are AMAZING at this!'



if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)