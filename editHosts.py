import sys
import sh

#only for worker chamges
def updateHosts (N=0):
	print("todo updateHosts")

def initHosts():
	print("todo init hosts files")

# Get the IP of node type master, worker or server
def getIP(name):

	node_name = "ACC4_"+name

	item = sh.nova("list")
	item_row = sh.grep(item, node_name)
	sh.grep = sh.grep.bake("-Eo")
	ip_adr = sh.grep(item_row, '\<Network=.*\>')
	ip_adr = ip_adr.replace("Network=", "")
	ip_adr_list = str(ip_adr).splitlines()
	print(type(ip_adr_list), len(ip_adr_list))
	return ip_adr_list


""" ETC/HOSTS  """

#the filepath is missing sudo permissions
# index 0-6 should never be edited!
# addNode(IP, name)
def addNode(IP, name):
    """
    last_no_worker = lastWorker()
    with open("/etc/hosts", "a") as myfile:
        myfile.write(IP + " sparkworker" + str(int(last_no_worker) + 1) + "\n")
        print("wrote to file")
    """
    f = open("/etc/hosts", "r")
    lines = f.readlines()
    for line in lines:
        print(line,)

#the filepath is missing sudo permissions
# lastworker()
def lastWorker():
    with open('/etc/hosts', 'r') as myfile:
        lines = myfile.read().splitlines()
        last_line = lines[-1]
        last_no_worker = last_line[-1]
    return(last_no_worker)

#the filepath is missing sudo permissions
# removeWorker()
def removeWorker():
    with open("/etc/hosts", "r+") as infile:
        lines = infile.read().splitlines()
        last_worker = lines[-1]

    # havent succeeded removing it but i have identified the last worker :)


""" ETC/ANSIBLE/HOSTS  """

# Adding into the second place in etc/ansible/hosts

# addworkerAns()
def addWorkerAns():
    last_no_worker = lastWorkerAns()
    with open("/etc/ansible/hosts", "a") as myfile:
        myfile.write("sparkworker" + str(int(last_no_worker) + 1) +
                     " ansible_connection=ssh ansible_user=ubuntu" + "\n")

# lastWorkerAns()
def lastWorkerAns():
    with open('/etc/ansible/hosts', 'r') as myfile:
        lines = myfile.read().splitlines()
        last_line = lines[-1].split()
        first_word = last_line[0]
        no_worker = first_word[-1]
    return(no_worker)

# Adding into the first place in etc/ansible/hosts


#AddWorkerAns()
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

#updateHostFiles()
def updateHostFiles(name=""):
    nameList = ["ansible-node", "sparkmaster","sparkworker"]
    OFFSET = 7
    ip_list = getIP("")
    i = 0
    f = open("/etc/hosts", "r")
    lines = f.readlines()
    for(IP in ip_list):
        if("192.168." in IP):
            name = nameList[i] if i < len(nameList) else nameList[-1]+str(i)
            addNode(IP, name)
            lines[i+OFFSET] = IP + " " name
            i += 1
    for line in lines:
        f.writelines(line)

if __name__ == '__main__':
	# image names to be used
#	if(len(sys.argv) < 2):
#		print("Too few args in editHosts")
#		exit(1)
#	x = getIp(sys.argv[1])
#	print(x)
	#addWorker("IP")
	updateHostFiles()
