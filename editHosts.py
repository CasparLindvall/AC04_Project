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
	ip_adr_list = str(ip_adr).splitlines()
	print(type(ip_adr_list), len(ip_adr_list))
	return ip_adr_list

if __name__ == '__main__':
	# image names to be used
	if(len(sys.argv) < 2):
		print("Too few args in editHosts")
		exit(1)
	x = getIp(sys.argv[1])
	print(x)
