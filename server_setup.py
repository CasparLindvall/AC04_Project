#!flask/bin/python
from flask import Flask, jsonify, request
import sys, sh
from editState import getState, updateState
from remove_nodes import removeNodes
from ssc_instance_userdata import deployInstances
from editHosts import updateHostFiles

app = Flask(__name__)

worker_image = "IMPORTANT_ACC4_SparkWorker"
master_image = "IMPORTANT_ACC4_SparkMaster_New"

@app.route('/nodes', methods=['GET'])
def serverOption():
	option = request.args.get('option', default = 1, type = int)
	workerAmount = request.args.get('N', default = 1, type = int)
	processAlt = ["creating network", "deploying new workers", "removing worker(s)"]
	state = ""
	if(option == 1):
		deployInstances([worker_image, master_image], 1)
	elif(option == 2):
		deployInstances([worker_image], workerAmount)
	elif(option == 3):
		removeNodes(workerAmount)
		workerAmount = int(workerAmount)*-1
	else:
		state = "oh noes, something went terribly wrong (wrong option code)"
	state = "Finished " + processAlt[option-1]
	updateState(state, workerChange=workerAmount)
	updateHostFiles()
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
