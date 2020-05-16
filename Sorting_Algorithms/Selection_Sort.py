# [1] Selection Sort implementation
def selection_sort(listt):
	for i in range(len(listt)-1):
	    # [i:] to bgin everytime with the next index.
	    min_val = min(listt[i:])
	    # ,i is for handling the doublications sorting in the list.
	    min_index = listt.index(min_val,i)
	    # A condition to cut the steps down.
	    if listt[i] != listt[min_index]:
	        listt[i],listt[min_index] = listt[min_index],listt[i]
	return listt

listt = [4,3,2,1,0,0]
print("first implementation:    ",selection_sort(listt))

#........................................................

# [2] Selection Sort implementation | geeksforgheeks .
 
def selection_sort2(A):
	# Traverse through all array elements 
	for i in range(len(A)): 
	
	# Find the minimum element in remaining 
	# unsorted array 
		min_idx = i 
		for j in range(i+1, len(A)): 
			if A[min_idx] > A[j]: 
				min_idx = j 
			
		# Swap the found minimum element with 
		# the first element		 
		A[i], A[min_idx] = A[min_idx], A[i] 
	return A
A = [64, 25, 12, 22,64, 11]
print("second implementation:   ",selection_sort2(A))


# [3] Smallest and simplest approach.
x = [9,9,7,7,4,3,2,11,1,1]
for i in range(len(x)):
	min_ = i
	for j in range(i+1,len(x)):
		if x[i] > x[j]:
			min_ = j
	x[i],x[min_] = x[min_],x[i]
print("third implementation     ",x)
