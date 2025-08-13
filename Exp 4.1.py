class Queue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
        return len(self.queue)==0
    def enqueue (self,iteam):
        self.queue.append(iteam)
    def dequeue (self):
        if self.is_empty():
            raise IndexError ("Queue is empty")
        return self.queue.pop(0)
    def peek (self):
        if self.is_empty():
            raise IndexError ("Queue is empty")
        return self.queue[0]
    def size(self):
        return len(self.queue)
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue aftet enqeuing elements:",q.queue)
print("Dequeue element:",q.dequeue())
print("Queue after deqeuing an element:",q.queue)
print("Front element:",q.peek())
print("Queue size:",q.size())
