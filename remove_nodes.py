import sys, sh
from editState import getState

def removeNodes(N):
	stringReturn = None
	state, amountWorkers = getState()
	Nmax = amountWorkers

	if(N >= -1 and N <= Nmax):
		if(N == -1):
			N = Nmax
			item = sh.nova("delete","ACC4_master1")
			stringReturn = "You deleted the entire network"
			state = "shutdown"
			N = Nmax
		else:
			stringReturn = "You deleted "+ str(N) + "workers"
		for i in range(Nmax, Nmax-N, -1):
			item = sh.nova("delete","ACC4_worker_"+str(i))
		amountWorkers -= N

	return stringReturn, amountWorkers


if __name__ == '__main__':

        if(len(sys.argv) < 1):
		print("Too few args in removeNodes.py")
		exit(1)

	N    = int(sys.argv[1])

	print(removeNodes(N))
