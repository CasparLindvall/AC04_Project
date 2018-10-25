""" ETC/HOSTS  """


def addWorker():
    last_no_worker = lastWorker()
    with open("etc-hosts.txt", "a") as myfile:
        myfile.write("XXXXX" + " sparkworker" + str(int(last_no_worker) + 1) + "\n")


def lastWorker():
    with open('etc-hosts.txt', 'r') as myfile:
        lines = myfile.read().splitlines()
        last_line = lines[-1]
        last_no_worker = last_line[-1]
    return(last_no_worker)


def removeWorker():
    with open("etc-hosts.txt", "r+") as infile:
        lines = infile.read().splitlines()
        last_worker = lines[-1]

    # havent succeeded removing it but i have identified the last worker :)


""" ETC/ANSIBLE/HOSTS  """

# Adding into the second place in etc/ansible/hosts


def addWorkerAns():
    last_no_worker = lastWorkerAns()
    with open("etc-ansible-hosts.txt", "a") as myfile:
        myfile.write("sparkworker" + str(int(last_no_worker) + 1) +
                     " ansible_connection=ssh ansible_user=ubuntu" + "\n")


def lastWorkerAns():
    with open('etc-ansible-hosts.txt', 'r') as myfile:
        lines = myfile.read().splitlines()
        last_line = lines[-1].split()
        first_word = last_line[0]
        no_worker = first_word[-1]
    return(no_worker)

# Adding into the first place in etc/ansible/hosts


def addWorkerAns2():
    last_no_worker = lastWorkerAns()
    f = open("etc-ansible-hosts.txt", "r")
    contents = f.readlines()
    f.close()

    contents.insert(48, "sparkworker"+str(int(last_no_worker)) +
                    " ansible_ssh_host="+"XXXXXXX" + "\n")

    f = open("etc-ansible-hosts.txt", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


addWorkerAns()
addWorkerAns2()
