# http://docs.openstack.org/developer/python-novaclient/ref/v2/servers.html
import time, os, sys, subprocess
import inspect, re, sh
from os import environ as env
from editState import getState

from  novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session


# Data to be used for the instance creation
def genInitData():
	flavor = "ACCHT18.normal"
	private_net = 'SNIC 2018/10-30 Internal IPv4 Network'
	loader = loading.get_plugin_loader('password')
	auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                	                username=env['OS_USERNAME'],
        	                        password=env['OS_PASSWORD'],
                        	        project_name=env['OS_PROJECT_NAME'],
                                	project_domain_name=env['OS_USER_DOMAIN_NAME'],
                                	project_id=env['OS_PROJECT_ID'],
                                	user_domain_name=env['OS_USER_DOMAIN_NAME'])

	sess = session.Session(auth=auth)
	nova = client.Client('2.1', session=sess)
    	print "user authorization completed."

	return(flavor, private_net, nova)

def createInstance(image_name, node_name, flavor, private_net, nova):
    print("Creating instance")
    image = nova.glance.find_image(image_name)
    flavor = nova.flavors.find(name=flavor)

    if private_net != None:
        net = nova.neutron.find_network(private_net)
        nics = [{'net-id': net.id}]
    else:
        sys.exit("private-net not defined.")

    #print("Path at terminal when executing this file")
    #print(os.getcwd() + "\n")
    cfg_file_path =  os.getcwd()+'/cloud-cfg.txt'
    if os.path.isfile(cfg_file_path):
        userdata = open(cfg_file_path)
    else:
        sys.exit("cloud-cfg.txt is not in current working directory")

    secgroups = ['default', "ACC04_masterspark"]

    print "Creating instance ... "
    instance = nova.servers.create(name=node_name, image=image, flavor=flavor, userdata=userdata, nics=nics,security_groups=secgroups)
    inst_status = instance.status
    print "waiting for 10 seconds.. "
    time.sleep(10)

    while inst_status == 'BUILD':
        print "Instance: "+instance.name+" is in "+inst_status+" state, sleeping for 5 seconds more..."
        time.sleep(5)
        instance = nova.servers.get(instance.id)
        inst_status = instance.status

    if "master" in node_name:
	floating_ip_pool_name = nova.floating_ip_pools.list()
        floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name)
        instance.add_floating_ip(floating_ip)

    print "Instance: "+ instance.name +" is in " + inst_status + " state"


# Create instanes of types in nanmeList
def deployInstances(nameList, N):
	flavor, private_net, nova = genInitData()
	_, workerCount = getState()
	for image_name in nameList:
        	print("current name = ", image_name)
        	n_times = 1
		node_name = "ACC4_master"

		if "worker" in image_name.lower():
        		n_times = int(N)
        		node_name = "ACC4_worker_"
			# Set this to range(1,2) to max deploy 1 worker
			for i in range(1+workerCount, n_times + 1 + workerCount):
        			print("about to worker node")
        			createInstance(image_name, node_name+str(i), flavor, private_net, nova)
		else:
			 createInstance(image_name, node_name+"1", flavor, private_net, nova)


if __name__ == '__main__':
	# image names to be used
	if(len(sys.argv) < 3):
		print("SSC had too few args, exit!")
		exit(1)
	nameList = sys.argv[1:-1]
	N = sys.argv[-1]
	deployInstances(nameList, N)
