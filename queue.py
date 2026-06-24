class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def peekfront(self):
        return self.queue[0]
    def peekrear(self):
        return self.queue[-1]
    def isempty(self):
        return len(self.queue) == 0
    def clear(self):
        self.queue = []

d = Queue()
d.enqueue(1)
d.enqueue(2)
d.enqueue(3)
print(d.dequeue())
print(d.peekfront())
print(d.peekrear())
print(d.isempty())
d.clear()
print(d.isempty())