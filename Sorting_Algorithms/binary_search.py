# binary search elementation.
def binary_search(list_items, item):
	first = 0
	last = len(list_items) - 1
	found = False
	while first <= last and not found:
		mid = (first + last) // 2
		if list_items[mid] == item:
			found = True
		else:
			if mid < item:
				first = mid + 1
			else:
				last = mid - 1
	return found

print(binary_search([1,2,3,4], 3))
print(binary_search([22,33,44,55], 99))