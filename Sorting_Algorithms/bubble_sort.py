# Bubble sort implementation.
# first approach.
def bubble_sort(my_list):
	for j in range(len(my_list)-1,0,-1):
		for i in range(j):
			if my_list[i] > my_list[i+1]:
				my_list[i], my_list[i+1] = my_list[i+1],my_list[i]
	return my_list

print(bubble_sort([9,8,7,6,5,4,3]))
# second approach.
def bubble_sort2(mylist2):
	# difference 1 from up.
	for k in range(len(mylist2)-1):
		#difference 2 from up.
		for l in range(len(mylist2)-1-k):
			if mylist2[l] > mylist2[l+1]:
				mylist2[l], mylist2[l+1] = mylist2[l+1], mylist2[l]
	return mylist2

print(bubble_sort2([22,77,99,88,32]))