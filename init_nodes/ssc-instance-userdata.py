# http://docs.openstack.org/developer/python-novaclient/ref/v2/servers.html
import time, os, sys, subprocess
import inspect, re, sh
from os import environ as env

from  novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session

# image names to be used
nameList = sys.argv[1:-1]
N = sys.argv[-1]

returnString = "This is a noice return string"
worker_string = "ACC4_worker_"
master_string = "ACC_master"

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

floating_ip_pool_name = nova.floating_ip_pools.list()
#floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name)

def createInstance(image_name, node_name):

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

    secgroups = ['default', ]

    print "Creating instance ... "
    instance = nova.servers.create(name=nodeName, image=image, flavor=flavor, userdata=userdata, nics=nics,security_groups=secgroups)
    inst_status = instance.status
    print "waiting for 10 seconds.. "
    time.sleep(10)

    while inst_status == 'BUILD':
        print "Instance: "+instance.name+" is in "+inst_status+" state, sleeping for 5 seconds more..."
        time.sleep(5)
        instance = nova.servers.get(instance.id)
        inst_status = instance.status

    if master in node_name:
        floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name)
        instance.add_floating_ip(floating_ip)

    print "Instance: "+ instance.name +" is in " + inst_status + " state"

    #Get nova list as str
    item = sh.nova("list")
    #Get substring containing "ACC4...
    item_row = sh.grep(item, nodeName)
    #Set grep flags , E = pattern, o = only
    sh.grep = sh.grep.bake("-Eo")
    # From substring get subsubstring which matches "Network" then ip
    ip_adr = sh.grep(item_row, '\<Network.*\>')
    print(ip_adr)


# Create instanes
for image_name in nameList:
    n_times = 1
    node_name = "ACC_master"
   
    if "worker" in image_name:
        n_times = N_worker
        node_name = "ACC4_worker_"
   
    for i in range(N_worker):
        createInstance(image_name+str(i), node_name+str(i))
# The following command can grep the IP adress for ACC4_test_worker
# the above but for bash
# nova list | grep ACC4_test_worker | grep -Eo '\<Network.*\>'

print(returnString, -1)
