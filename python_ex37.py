class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
stack = Stack()

for c in range(1, 6):
    stack.push(str(c))
    
reverse = []

for i in range(len(stack.items)):
    reverse += stack.pop()
    
print(reverse)