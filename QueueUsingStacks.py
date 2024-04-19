class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enQueue(self, element):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(element)
        while self.s2:
            self.s1.append(self.s2.pop())
    def deQueue(self):
        if not self.s1:
            return None
        return self.s1.pop()
# Example usage
queue = QueueUsingStacks()
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
print(queue.deQueue())
queue.enQueue(4)
print(queue.deQueue())