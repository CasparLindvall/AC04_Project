#create entire system
#create worker
#remove worker
#destroy network
import requests

def alternatives():
	alt = input("What do you want to do: \n
			 1-create system, 2-create worker, \n
			3-remove worker, 4-status and 9-destroy network: \n")
	if alt == "1":
		requests.get(http://130.238.29.80:5000/init_nodes?option=1&N=1")
	elif alt == "2":
		workerChange = input("How many workers would you like to add? [0, 10] \n")
		requests.get(http://130.238.29.80:5000/init_nodes?option=2&N=1")
		print("Creating worker")
	elif alt == "3":
		workerChange = input("How many workers would you like to remove? [0, 10] \n")
		requests.get(http://130.238.29.80:5000/init_nodes?option=5&N=1")
		print("Removing worker")
	elif alt == 4:
		r = requests.get("http://130.238.29.80:5000/state")
		print r.text
	elif alt == 9:
		ans = input("Do you really want to remove the entire network?[y/n] \n")
		if(ans.lower() == y or ans.lower() == yes):
			requests.get("http://130.238.29.80:5000/shutdown")
		else:
			print("Phew, close one! Why don't you retry?")


if __name__ == '__main__':
	alternatives()

