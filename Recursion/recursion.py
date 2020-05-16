def recursive_factorial(x):
	# Maximum depth is 1000 after this an error will appear.
	# The base condition, it's a must to stop recursion in one point(1).
	if x == 1:
		return 1
	else:
		# The function calls itselfrecuursively.
		return (x*recursive_factorial(x-1))

print(recursive_factorial(5))