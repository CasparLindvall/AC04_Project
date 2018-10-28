import sys
from init_nodes.editHosts import updateHosts
from init_nodes.editState import updateState

def removeNodes(N, Nmax):
	stringReturn = None
	amountWorkers = Nmax

	if(N > 0 and N <= Nmax):
		if(N == -1):
			N = Nmax
			item = sh.nova("delete","ACC4_master1")
			stringReturn = "You deleted the entire network"
		else:
			stringReturn = "You delete "+ N + " workers"
		for i in range(Nmax-N, Nmax):
			item = sh.nova("delete","ACC4_worker_"+str(i))
		amountWorkers -= N

	updateState(workerChange=Nmax-N)
	updateHosts(N) # TODO!

	return stringReturn, amountWorkers


if __name__ == '__main__':

        if(len(argv) < 2):
		print("Too few args in removeNodes.py")
		exit(1)

	N    = sys.argv[1] +1
	Nmax = sys.argv[2]

	print(removeNodes(N, Nmax))
