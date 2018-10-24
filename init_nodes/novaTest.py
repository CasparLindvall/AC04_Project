# http://docs.openstack.org/developer/python-novaclient/ref/v2/servers.html
import time, os, sys, subprocess
import inspect, re
import sh
from os import environ as env

from  novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session


nameList = sys.argv[1:-1]
N = sys.argv[-1]

print(nameList, N)

"""
flavor = "ACCHT18.normal"
private_net = 'SNIC 2018/10-30 Internal IPv4 Network'
floating_ip_pool_name = None
floating_ip = None
#image_name = '5e963610-1bee-49a6-afb6-fe8463acf122'
image_name = "IMPORTANT_ACC4_SparkWorker"

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

# READ HERE!
# Print the worker ip address
item = sh.nova("list")
sh.grep = sh.grep.bake("-E")
item_row = sh.grep(item, '\<ACC4_test.*\>')

print(item_row)

"""
