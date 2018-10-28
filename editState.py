from sys import argv
import os
# Updates the state and worker count
def updateState(newStatus="", workerChange=0, path=""):
	absPath = os.path.abspath(path+"state.txt")
	f = open(absPath, "r")
	lines = f.readlines()
	n_workers = lines[1][-2]

	if(newStatus):
		lines[0] = ["state="+newStatus+"\n"]

	if(workerChange):
		lines[1] = ["workers="+str(int(n_workers) + int(workerChange)) +"\n"]

	f = open("state.txt", "w")
	for line in lines:
		f.writelines( line )
# Returns the states
def getState(path=""):
	absPath = os.path.abspath(path+"state.txt")
	f = open(absPath, "r")
	lines = f.readlines()
        n_workers = lines[1][-2]
	return(lines[0][6:-1], n_workers)

# Can run from cmd if needed
if __name__ == '__main__':

	if(len(argv) < 2):
        	print("Too few args!")
        	exit(1)

	newStatus, workerChange = argv[1], argv[2]
	updateState(newStatus, workerChange)
