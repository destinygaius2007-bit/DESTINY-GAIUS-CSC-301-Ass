
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

class Node:
    def __init__(self, v):
        self.v = v
        self.next = None
class LinkedStack:
    def __init__(self): self.top = None
    def push(self, x):
        n = Node(x); n.next = self.top; self.top = n
    def pop(self):
        if not self.top: return None
        v = self.top.v; self.top = self.top.next; return v
    def peek(self): return None if not self.top else self.top.v
# Sample
ls = LinkedStack()
ls.push('a')
ls.push('b')
print(ls.pop())  # -> b
print(ls.peek()) # -> a