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

