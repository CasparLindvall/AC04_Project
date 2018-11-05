# ACC04_Project
Group 04 in Cloud Computing.

QTL as a Service (QTLaaS), a cloud service for genetic analysis
The below steps are based on the user having access to SUPR - SNIC User and Project Repository.

To run:
A) pip install requests 
B) python interface.py (with correct IP)

If the flask server isn't responding then:
I) Create a new server node with the snapshot named: "ACC4_Server_Final
II) As "ubuntu" (user) write "source ~/SNIC.sh" (or replace with your own)
III) As "ubuntu" (user) write "python server_setup.py"

If the above is not working then:
1) make a fresh 16.04 ubuntu installation.
2) Follow https://github.com/QTLaaQTLaaS 0-4 (make sure you install python-novaclient==9.1.1) 
3) SCP your SNIC.sh file.
4) git clone this repo.
5) pip install sh, Flask
6) Give the user "ubuntu" write permisson to /etc/hosts, /etc/ansible/hosts, state.txt and token.txt
7) Finally, do steps I-III 

Sources:
https://github.com/QTLaaQTLaaS
https://www.overleaf.com/2564895817jbnqryznhgrn
