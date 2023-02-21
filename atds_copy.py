#!/usr/bin/env python3

"""
atds.py
Advanced Topics Data Structures: a library of Python implemenations of Abstract Data Structures
for the Advanced Topics in CS course.
"""

__author__ = "Alexandra Kim"
__version__ = "2023-02-10"

class Deque():
    """Uses lists to implement a Deqeue class.
    Defines a dequeue with methods add_front, add_rear, remove_front, remove_rear, size, is_empty.
    """
    def __init__(self):
        self.deque = []
        
    def add_front(self, item):
        self.deque.append(item)
        
    def add_rear(self, item):
        self.deque.insert(0,item)
        
    def remove_front(self):
        return self.deque.pop()
    
    def remove_rear(self):
        return self.deque.pop(0)
    
    def size(self):
        return len(self.deque)
    
    def is_empty(self):
        return (len(self.deque) == 0)
    
    def __repr__(self):
        return str([item for item in self.deque])

class Queue():
    """Uses lists to implement a Queue class.
    Defines a queue with methods enqueue, dequeue, peek, size, is_empty.
    """
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.insert(0,item)
    
    def dequeue(self):
        return self.queue.pop()
    
    def peek(self):
        return self.queue[-1]

    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return (len(self.queue) == 0)
    
    def __repr__(self):
        return str([item for item in self.queue])

class Stack():
    
    """Uses lists to implement a Stack class.
    Defines a stack with methods push, pop, peek, size, and is_empty.
    """
    
    def __init__(self):
        self.stack = []
    
    def push(self,item):
        """Adds an item to the stack"""
        self.stack.append(item)
        
    def pop(self):
        """Returns and removes the last item of the stack"""
        return self.stack.pop()
    
    def peek(self):
        """Returns the last item of the stack"""
        return self.stack[-1]
    
    def size(self):
        """Returns the number of items in the list"""
        return len(self.stack)
    
    def is_empty(self):
        """Returns true if the item is empty and false otherwise"""
        return (self.size() == 0)
    
    def __repr__(self):
        return str([item for item in self.stack])
    
def main():
    pass

if __name__ == "__main__":
    main()