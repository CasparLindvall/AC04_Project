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


""" ETC/HOSTS  """

#the filepath is missing sudo permissions

def addWorker():
    last_no_worker = lastWorker()
    with open("/etc/hosts", "a") as myfile:
        myfile.write(x + " sparkworker" + str(int(last_no_worker) + 1) + "\n")

#the filepath is missing sudo permissions

def lastWorker():
    with open('/etc/hosts', 'r') as myfile:
        lines = myfile.read().splitlines()
        last_line = lines[-1]
        last_no_worker = last_line[-1]
    return(last_no_worker)

#the filepath is missing sudo permissions

def removeWorker():
    with open("/etc/hosts", "r+") as infile:
        lines = infile.read().splitlines()
        last_worker = lines[-1]

    # havent succeeded removing it but i have identified the last worker :)


""" ETC/ANSIBLE/HOSTS  """

# Adding into the second place in etc/ansible/hosts


def addWorkerAns():
    last_no_worker = lastWorkerAns()
    with open("/etc/ansible/hosts", "a") as myfile:
        myfile.write("sparkworker" + str(int(last_no_worker) + 1) +
                     " ansible_connection=ssh ansible_user=ubuntu" + "\n")


def lastWorkerAns():
    with open('/etc/ansible/hosts', 'r') as myfile:
        lines = myfile.read().splitlines()
        last_line = lines[-1].split()
        first_word = last_line[0]
        no_worker = first_word[-1]
    return(no_worker)

# Adding into the first place in etc/ansible/hosts


def addWorkerAns2():
    last_no_worker = lastWorkerAns()
    f = open("/etc/ansible/hosts", "r")
    contents = f.readlines()
    f.close()

    contents.insert(48, "sparkworker"+str(int(last_no_worker)) +
                    " ansible_ssh_host="+"XXXXXXX" + "\n")

    f = open("/etc/ansible/hosts", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

if __name__ == '__main__':
	# image names to be used
#	if(len(sys.argv) < 2):
#		print("Too few args in editHosts")
#		exit(1)
#	x = getIp(sys.argv[1])
#	print(x)
	addWorker()
