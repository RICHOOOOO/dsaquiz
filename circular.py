class circular():
    def __init__(self, k):
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1
    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print ('is full')
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail=(self.tail + 1)% self.k
            self.queue[self.tail] = data
    def dequeue(self):
        if (self.head == 1):
            print('is empty')
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head =-1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp
    def printCQueue (self):
        if (self.head == -1):
            print('no element in the cirular')
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print ( self.queue[i], end = " ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i],end = " ")
            for i in range(0, self.tail + 1):
                print ( self.queue[i], end = " ")
            print()
obj = circular(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print('initial queue')
obj.printCQueue()
obj.dequeue()
print('after removing an element from the queue')
obj.printCQueue()