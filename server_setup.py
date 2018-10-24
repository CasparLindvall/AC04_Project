#!flask/bin/python
from flask import Flask, jsonify, request
import subprocess
import sys
#from mockDeployment import mockFunc

app = Flask(__name__)

#@app.route('/cowsay/api/v1.0/saysomething', methods=['GET'])
#def cow_say():
#    data=subprocess.check_output(["cowsay","Hello student"])
#    return data

def helloWorld():
    return ('Should do something with 1')

def helloWorld2():
    return ('And something else with with some else')
"""
To run use:
curl -i http://130.238.29.7:5000/?option=X
where option = X (e.g 1-4)

If 1 = setup new network
If 2 = add worker
If 3 = rm worker
if 4 = rm network
"""
worker_image = "IMPORTANT_ACC4_SparkWorker"
master_image = "IMPORTANT_ACC4_SparkMaster_New"

@app.route('/init_nodes/', methods=['GET'])
def serverOption():
	option = request.args.get('option', default = 1, type = int)
        workerAmount = request.args.get('N', default = 1, type = int)

	data = None
	if(option == 1):
		data = subprocess.check_output(["python", "ssc-instance-userdata.py", "worker_image","master_image", 1])
	elif(option == 2):
		data = subprocess.check_output(["python", "ssc-instance-userdata.py","worker_image", N])
	elif(option >= 3):
		data = subprocess.check_output(["python", "remove-nodes.py","worker_image", N])
	else:
		data = "something went wrong"
	return data



if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)
