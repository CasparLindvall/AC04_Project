import sys

N = sys.argv[1]+1
Nmax = sys.argv[2]

def removeNodes(N, Nmax):
	stringReturn = None
	if N > 0 and N <= Nmax:
		if N=-1:
			N=Nmax
			item = sh.nova("delete","ACC4_master")
			stringReturn = "You deleted the entire network"
		else:
			stringReturn = "You deleted the workers"
		for i in range(Nmax-N, Nmax):
			item = sh.nova("delete","ACC4_worker_"+str(i))
	return stringReturn
		

			
		

output = removeNodes(N, Nmax)
return output
