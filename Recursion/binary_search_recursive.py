# Recursive Binary search in ordered list O(log n).
# in case of sequencial search,UNORDERED, then O(n) linear.
def binary_search(data,target,low,high):
    # low = 0
    # high = len(data)-1
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if (target == data[mid]):
            return True
        elif target < data[mid]:
            return binary_search(data,target,low,mid-1)
        else:
            return binary_search(data,target,mid+1,high)

my_list = [3,5,77,89,100,240]
target = 89
result1 = binary_search(my_list,target,0,len(my_list)-1)
print(result1)
mylist2 = [4,7,9,15,9]
target = 100
result2 = binary_search(mylist2,target,0,len(mylist2)-1)
print(result2)
