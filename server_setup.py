#!flask/bin/python
from flask import Flask, jsonify, request
import sys, sh, timeit, time
from editState import getState, updateState
from remove_nodes import removeNodes
from ssc_instance_userdata import deployInstances
from editHosts import updateHostFiles

app = Flask(__name__)

worker_image = "IMPORTANT_ACC4_SparkWorker"
master_image = "IMPORTANT_ACC4_SparkMaster_New"

runAns = sh.Command("/usr/bin/ansible-playbook")
runAns = runAns.bake("-s")

@app.route('/nodes', methods=['GET'])
def serverOption():
	option = request.args.get('option', default = 1, type = int)
	workerAmount = request.args.get('N', default = 1, type = int)
	processAlt = ["creating network", "deploying new workers", "removing worker(s)"]
	state =  processAlt[option-1]
	currState, Nmax, IP, tokens = getState()
	updateState(state, workerChange=0)
	if(option == 1):
		deployInstances([worker_image, master_image], 1)
	elif(option == 2):
		deployInstances([worker_image], workerAmount)
	elif(option == 3):
		#start time
		time_start = timeit.default_timer()
		removeNodes(workerAmount)
		time_end = timeit.default_timer()
		#wait for deleting nodes to be synced
		print("About to sleep for ", 5*workerAmount - (time_end-time_start))
		time.sleep(5*workerAmount - (time_end-time_start))
		workerAmount = int(workerAmount)*-1

	state = "Finished " + processAlt[option-1]
	updateState(state, workerChange=workerAmount)
	updateHostFiles()
	if(Nmax + workerAmount > 0):
		print("Sleeping 10s, then deploying anisble  playbook")
		time.sleep(10)
		print(runAns("spark_deployment.yml"))
	else:
		state="Too few workers!"
	return state

@app.route('/state')
def state():
	state, count, IP, tokens = getState(path="")
	output = "State = " + state + "\n" + "Woker count = " + str(count) + "\n" + IP + "Tokens = " + tokens + "\n"
	return output

@app.route('/shutdown')
def shutdown():
	removeNodes(-1)
	state, n, IP, tokens = getState()
	updateState("YOU BURNED IT TO THE GROUND!", workerChange=-n)
	return "It's all gone! \_( T _ T )_/"

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
