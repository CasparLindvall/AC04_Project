import sys
import sh

#only for worker chamges
def updateHosts (N=0):
	print("todo updateHosts")

def initHosts():
	print("todo init hosts files")

# Get the IP of node type master, worker or server
def getIp(name):

	node_name = "ACC4_"+name

	item = sh.nova("list")
	item_row = sh.grep(item, node_name)
	sh.grep = sh.grep.bake("-Eo")
	ip_adr = sh.grep(item_row, '\<Network=.*\>')
	print(ip_adr)
	#return ip_adr


getIp(sys.argv[1])
