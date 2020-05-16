# Dequeue in python or Doubly Ended Queue.
# Time comp is O(1) and not O(n) as in the Queue.
# We can make operations in Deques in left and right.
import collections

de = collections.deque([1,2,3])

de. append(4)                # append([1,2,3,4])
de.appendleft(6)             # appendleft([6,1,2,3,4])
de.pop()                     # append([6,1,2,3,])
de.popleft()                 # append([1,2,3])

de2 = collections.deque([1,2,3,3,4,2,4])

de2.index(1,0,2)      # index of {1} between(0,2) is 0
de2.insert(4,3)       #[1,2,3,3,{3},2,4]
de2.count(3)          # 3 , 3 times occurences.
de2.remove(3)         #[1,2,3,3,2,4] 1st occu removed.

de3 = collections.deque([1,2,3])

de3.extend(4,5,6)           # [1,2,3,4,5,6]
de3.extendleft(7,8,9)       # [9,8,7,1,2,3,4,5,6]
de3.rotate(-3)              # [1,2,3,4,5,6,9,8,7]
de3.revers()                # [7,8,9,6,5,4,3,2,1]
