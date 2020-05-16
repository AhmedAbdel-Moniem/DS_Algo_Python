# Stack implementation.
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        # append at the end.
        #if at the begining:  {more time}
        # return self.items.insert(0,item)
        return self.items.append(item)
    
    def pop(self):
        # pop from the end
        # if from the begining:  {more time}
        # return self.items.pop(0)
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

def divid_by_two(decimal_nums):
    # empty stack to append the binary numbers 
    s = Stack()
    while decimal_nums > 0:
        remainder = decimal_nums % 2   # Mod of numbers
        s.push(remainder)              # append result (0)or(1)  
        decimal_nums = decimal_nums //2 # continue div the num
    
    binary_string = ""
    while not s.is_empty():
        binary_string = binary_string + str(s.pop())
    return binary_string

print(divid_by_two(42))
