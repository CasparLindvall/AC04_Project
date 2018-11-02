import sys
import sh


# Get the IP of node type master, worker or server
# The following command can grep the IP adresses for ACC4_*
# nova list | grep ACC4_ | grep -Eo '\<Network.*\>'
def getIP(name=""):

	node_name = "ACC4_"+name

	item = sh.nova("list")
	item_row = sh.grep(item, node_name)
	sh.grep = sh.grep.bake("-Eo")
	ip_adr = sh.grep(item_row, '\<Network=.*\>')
	ip_adr = ip_adr.replace("Network=", "")
	ip_adr_list = str(ip_adr).splitlines()
	return ip_adr_list

# Updates /etc/ansible/hosts
def updateHostAns(nameList, ipList, OFFSET, path):
    i = 0
    f = open(path, "r+")
    lines = f.readlines()
    # For each IP define new values (hard reset)
    for IP in ipList:
        if("," in IP):
            IP = IP.split(",")[0]
        name = nameList[i] if i < len(nameList)-1 else nameList[-1]+str(i-1)
        lines[i] = name + " ansible_ssh_host=" + IP + "\n"
        i += 1
    lines[i-1] += "\n"
    lines[-1] = "sparkworker[1:" + str(i-2) + "] ansible_connection=ssh ansible_user=ubuntu  ansible_ssh_common_args='-o StrictHostKeyChecking=no' \n"
    f.close()

    #remove potential old nodes
    lines = lines[:len(ipList)] + lines[-OFFSET:]

    f = open(path, "w")
    for line in lines:
        f.writelines(line)
    f.close()

# Update  /etc/hosts
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

    #remove potential old nodes
    lines = lines[:OFFSET+len(ipList)]

    f = open(path, "w")
    for line in lines:
        f.writelines(line)
    f.close()

#update both hosts files when called
def updateHostFiles():
    nameList = ["ansible-node", "sparkmaster","sparkworker"]
    ipList = getIP()
    OFFSET = 7
    OFFSET_ANS = 9
    updateHost(nameList, ipList, OFFSET, "/etc/hosts")
    updateHostAns(nameList, ipList, OFFSET_ANS, "/etc/ansible/hosts")

if __name__ == '__main__':
	updateHostFiles()
