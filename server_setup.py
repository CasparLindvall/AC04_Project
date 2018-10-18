#!flask/bin/python
from flask import Flask, jsonify, request
import subprocess
import sys

app = Flask(__name__)

#@app.route('/cowsay/api/v1.0/saysomething', methods=['GET'])
#def cow_say():
#    data=subprocess.check_output(["cowsay","Hello student"])
#    return data

def helloWorld(option):
    return ('Should do something with', option, '\n')

def helloWorld2(option):
    return ('And something else with with', option, '\n')
"""
To run use:
curl -i http://130.238.29.7:5000/?option=X
where option = X (e.g 1-4)

If 1 = setup new netowork
If 2 = add worker
If 3 = rm worker
if 4 = rm network
"""

@app.route('/', methods=['HEAD', 'OPTIONS', 'GET'])
def serverOption():
	option = request.args.get('option', default = 1, type = int)
	if(option == 1):
		return helloWorld(option)
	else:
		return helloWorld2(option)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)