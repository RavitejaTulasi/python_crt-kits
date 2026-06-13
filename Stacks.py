class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,value):
        self.stack.append(value)
        print(f"pushed: {value} | Stack: {self.stack}")

    def pop(self):
        if self.isEmpty():
            return "stack underflow!"
        val = self.stack.pop()
        print(f"popped: {val} | stack: {self.stack}")
        return val
    
    def peek(self):
        if self.isEmpty():
            return "stack is Empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        if self.isEmpty():
            print("stack is empty.")
        else:
            print("TOP->", self.stack[::-1])

s=Stack()
s.push(10);s.push(20);s.push(30)
print("Peek: ",s.peek)
s.pop()
print("size: ", s.size())
s.display()
z=Stack()
print(z.pop())