#!flask/bin/python
from flask import Flask, jsonify, request
import sys, sh
from editState import getState
from remove_nodes import removeNodes
from ssc_instance_userdata import deployInstances

app = Flask(__name__)

#@app.route('/cowsay/api/v1.0/saysomething', methods=['GET'])
#def cow_say():
#    data=subprocess.check_output(["cowsay","Hello student"])
#    return data

"""
To run use:
curl -i "http://130.238.29.80:5000/init_nodes?option=5&N=1"
where option  = 1-4, N>=0

If 1 = setup new network
If 2 = add worker
If 3 = rm worker
If 4 = rm network
"""
worker_image = "IMPORTANT_ACC4_SparkWorker"
master_image = "IMPORTANT_ACC4_SparkMaster_New"

@app.route('/nodes', methods=['GET'])
def serverOption():
	option = request.args.get('option', default = 1, type = int)
	workerAmount = request.args.get('N', default = 1, type = int)

	state = "Your request is being processed, reuse with option 5 to see the curre state"
	if(option == 1):
		deployInstances([worker_image, master_image], 1)
	elif(option == 2):
		deployInstances([worker_image], workerAmount)
	elif(option == 3):
		removeNodes(workerAmount)
	else:
		state = "oh noes, something went terribly wrong (wrong option code)"

	return state

@app.route('/state')
def state():
	state, count = getState(path="")
	output = "State = "+state+"\n" + "Worker count = "+ str(count) +"\n"
	return output

@app.route('/shutdown')
def shutdown():
	removeNodes(-1)
	return "It's all gone! \_( T _ T )_/"

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
