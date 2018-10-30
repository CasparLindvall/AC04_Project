import sys
import sh


# Get the IP of node type master, worker or server
# getIP()
def getIP(name=""):

	node_name = "ACC4_"+name

	item = sh.nova("list")
	item_row = sh.grep(item, node_name)
	sh.grep = sh.grep.bake("-Eo")
	ip_adr = sh.grep(item_row, '\<Network=.*\>')
	ip_adr = ip_adr.replace("Network=", "")
	ip_adr_list = str(ip_adr).splitlines()
	print(type(ip_adr_list), len(ip_adr_list))
	return ip_adr_list

# Updates /etc/ansible/hosts
#updateHostAns(nameList, ipList, path):
def updateHostAns(nameList, ipList, path):
    i = 0
    f = open(path, "r+")
    lines = f.readlines()
    # For each IP define new values (hard reset)
    for IP in ipList:
        if("," in IP):
            IP = IP.split(",")[0]
        name = nameList[i] if i < len(nameList)-1 else nameList[-1]+str(i-1)
        lines[i] = name + " ansible_ssh_host="+IP+"\n"
        i += 1
    lines[i-1] += "\n"
    lines[-1] = "sparkworker[1:" + str(i-2) + "] ansible_connection=ssh ansible_user=ubuntu \n"
    f.close()

    f = open(path, "w")
    for line in lines:
        f.writelines(line)
    f.close()

#updateHost(nameList, ipList, OFFSET, path)
def updateHost(nameList, ipList, OFFSET, path):
    i = 0
    f = open(path, "r+")
    lines = f.readlines()
    # For each IP define new values (hard reset)
    for IP in ipList:
        if("," in IP):
            IP = IP.split(",")[0]
        name = nameList[i] if i < len(nameList)-1 else nameList[-1]+str(i-1)
        if(i+OFFSET >= len(lines)):
            lines.append(IP + " " + name + "\n")
        lines[i+OFFSET] = IP + " " + name + "\n"
        i += 1
    f.close()
    f = open(path, "w")
    for line in lines:
        f.writelines(line)
    f.close()

#updateHostFiles()
def updateHostFiles():
    nameList = ["ansible-node", "sparkmaster","sparkworker"]
    ipList = getIP()
    OFFSET = 7
    print("UPDATING HOSTS")
    updateHost(nameList, ipList, OFFSET, "/etc/hosts")
    updateHostAns(nameList, ipList, "/etc/ansible/hosts")

if __name__ == '__main__':
	updateHostFiles()
