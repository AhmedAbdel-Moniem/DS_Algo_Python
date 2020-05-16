def insertion_sort(list_ins):
	# begine with index 1 to compare it with index 0.
	for index in range(1, len(list_ins)):
		# assign curr element to the 1st index in the arr.
		current_element = list_ins[index]
		#set pos = index
		position = index
		# loop to exchange index with index -1 or pos-1. 
		while position > 0 and current_element < list_ins[position-1]:
			# swap.
			list_ins[position] = list_ins[position-1]
			# set position to index 0
			position = position-1

		list_ins[position] = current_element
	return list_ins

print(insertion_sort([14,46,43,27,57,41,45,21,70]))
