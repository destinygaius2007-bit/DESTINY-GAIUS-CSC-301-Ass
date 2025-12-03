# ==============================================================================
#                  DATA STRUCTURES LABORATORY REPORT
#          IMPLEMENTATION OF SINGLY LINKED LIST & THEORY ANSWERS
# ==============================================================================
# Submitted by: [GAIUS DESTINY DIVINE]
# Matric No:    [230502094]
# Department:   Computer Science
# course code:        CSC 301
# course title:      Data Structures
# ==============================================================================



# ============================= 1. LINKED LIST IMPLEMENTATION =============================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning → O(1)
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end → O(n)
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete first occurrence of key
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Node with data {key} not found.")
            return

        prev.next = temp.next

    # Display list
    def display_list(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next


# ============================= 2. TESTING THE IMPLEMENTATION =============================
print("="*60)
print("           TESTING LINKED LIST OPERATIONS")
print("="*60)

llist = LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_beginning(5)
llist.insert_at_end(30)
llist.insert_at_beginning(1)

print("After inserting 5 values:")
llist.display_list()               # Output: 1 -> 5 -> 10 -> 20 -> 30

print("\nDeleting node with value 10...")
llist.delete_node(10)

print("After deletion:")
llist.display_list()               # Output: 1 -> 5 -> 20 -> 30

print("\nTrying to delete non-existing value 999...")
llist.delete_node(999)


# ============================= 3. THEORY ANSWERS (Well-Arranged) =============================

theory_answers = """
# ==============================================================================
#                            THEORY ANSWERS
# ==============================================================================

1. Difference between Arrays and Linked Lists
Feature              | Array                          | Linked List
---------------------|--------------------------------|---------------------------------
Memory storage       | Contiguous                     | Non-contiguous
Size                 | Fixed (static)                 | Dynamic (grows/shrinks at runtime)
Access time          | O(1) - random access           | O(n) - sequential access only
Insertion/Deletion   | O(n) (shifting required)       | O(1) if pointer known, else O(n)
Memory overhead      | Low                            | High (stores next pointer)


2. Time Complexity of Insertion in a Linked List
Operation                     | Time Complexity | Reason
------------------------------|-----------------|----------------------------------
Insert at beginning           | O(1)            | Just update head pointer
Insert at end (no tail ptr)   | O(n)            | Must traverse to last node
Insert at end (with tail)     | O(1)            | Direct access using tail pointer
Insert after a given node     | O(1)            | Pointer to node is already known


# ==============================================================================
#                            DISCUSSION QUESTIONS
# ==============================================================================
9
1. Key differences between Primitive Data Types and Abstract Data Types (ADTs)
Aspect         | Primitive Data Types           | Abstract Data Types (ADTs)
---------------|--------------------------------|------------------------------------
Definition     | Built-in (int, float, char)    | User/programmer-defined
Operations     | Fixed by language              | Defined by designer (e.g., push/pop)
 Implementation | Directly by hardware/language  | Hidden (can use array, linked list, etc.)
Focus          | How data is stored             | What operations are possible
Example        | int, boolean                   | Stack, Queue, List, Set


2. Why are arrays considered static and linked lists dynamic?
• Arrays are static → Size fixed at creation. Resizing needs new array + copying → O(n)
• Linked lists are dynamic → Nodes allocated individually at runtime. Can grow/shrink easily without reallocation.


3. When would you prefer a Linked List over an Array?
• Frequent insertions/deletions at beginning or middle
• Size is unknown or changes very frequently
• Memory is fragmented (hard to get large contiguous block)
• Need stable references/pointers to elements
• Implementing queues, adjacency lists in graphs, etc.


4. Real-World Examples
Data Structure | Real-World Example                            | Why it fits
---------------|-----------------------------------------------|----------------------------------
Stack          | Undo/Redo (Ctrl+Z)                            | Last In, First Out (LIFO)
               | Function call stack                           | Return to most recent call
               | Browser back button                           | Go to most recent page
Queue          | Printer job queue                             | First-come, first-served (FIFO)
               | CPU task scheduling (round-robin)             | Fair processing order
               | Message queues (Kafka, RabbitMQ)              | Process messages in arrival order
Linked List    | Music playlist (insert/delete songs anywhere) | Easy insertion/deletion anywhere
               | Blockchain (each block points to previous)    | Dynamic chain growth
               | Memory management free-list                   | Dynamic allocation & merging
               | Sparse matrix / polynomial representation     | Store only non-zero terms
"""

print(theory_answers)

