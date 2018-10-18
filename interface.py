#create entire system
#create worker
#remove worker
#destroy network


def alternatives():
	alt = input("What do you want to do: 1-create system, 2-create worker, 3-remove worker and 4-destroy network: ")
	if alt == "1":
		print("Creating system")
	elif alt == "2":
		print("Creating worker")
	elif alt == "3":
		print("Removing worker")
	else:
		print("Destroy network")

alternatives()
 

