# Recursive Python function to solve tower of hanoi
# {tail recursion}, which occurs when a function includes a
# single recursive call as the last statement of the function. In this case, a stack is
# not needed to store values to be used upon the return of the recursive call and thus
# a solution can be implemented using an iterative loop instead.
def TowerOfHanoi(n , A, B, C):
	if n==1:
		print ("Move disk 1 from source",A,"to destination",B)
		return
	TowerOfHanoi(n-1, A, C, B)
	print ("Move disk",n,"from source",A,"to destination",B)
	TowerOfHanoi(n-1, C, B, A)


n = 3
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods
