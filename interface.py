#create entire system
#create worker
#remove worker
#destroy network
import requests

def alternatives(IP_ADDRESS):
	response = None
	alt = input("What do you want to do:\n" + 
				"\t 1: create system\n" +
				"\t 2: create worker\n" +
				"\t 3: remove worker\n" +
				"\t 4: status \n" +
				"\t 9: destroy the entire network: \n")

	if alt == 1:
		requests.get(IP_ADDRESS+"/nodes?option=1&N=1")
	elif alt == 2:
		workerChange = input("How many workers would you like to add? [0, 10] \n")
		response = requests.get(IP_ADDRESS+"/nodes?option=2&N="+str(workerChange))
		print("Creating worker")
	elif alt == 3:
		workerChange = input("How many workers would you like to remove? [0, 10] \n")
		response = requests.get(IP_ADDRESS+"/nodes?option=3&N="+str(workerChange))
		print("Removing worker")
	elif alt == 4:
		response =  requests.get(IP_ADDRESS+"/state?")
	elif alt == 9:
		ans = raw_input("Do you really want to remove the entire network? [y/n] \n")
		ans = str(ans)
		if(ans.lower() in "y" or ans.lower() in "yes"):
			response = requests.get(IP_ADDRESS+"/shutdown?")
		else:
			print("Phew, close one! Why don't you retry?")
	if(response):
		print(response.text)

if __name__ == '__main__':
	IP_ADDRESS  = "http://130.238.29.0:5000"
	alternatives(IP_ADDRESS)

