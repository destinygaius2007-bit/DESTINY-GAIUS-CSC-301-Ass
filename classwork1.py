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


class ArrayStack:
    def __init__(self): self.data = []
    def push(self, x): self.data.append(x)
    def pop(self): return None if not self.data else self.data.pop()
    def peek(self): return None if not self.data else self.data[-1]
    def is_empty(self): return len(self.data) == 0
# Sample
s = ArrayStack()
s.push(10)
s.push(20)
print(s.pop())   # -> 20
print(s.peek())  # -> 10