# ==============================================================================
#                  DATA STRUCTURES LABORATORY REPORT
#          IMPLEMENTATION OF SINGLY LINKED LIST & THEORY ANSWERS
# ==============================================================================
# Submitted by: [OGUNTADE MICHEAL OLUWASEGUN]
# Matric No:    [230502129]
# Department:   Computer Science
# course code:        CSC 301
# course title:      Data Structures
# ==============================================================================



class QueueNode:
    def __init__(self, v):
        self.v = v
        self.next = None
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, x):
        node = QueueNode(x)
        if not self.rear:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node
    def dequeue(self):
        if not self.front:
            raise IndexError("dequeue from empty")
        val = self.front.v
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val