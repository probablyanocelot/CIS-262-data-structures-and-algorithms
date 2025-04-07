"""
File: linkedqueue.py
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def isEmpty(self):
        """
        Returns True if q is empty or False otherwise.
        """
        return self.front == None
    
    def __len__(self, data=None):
        """
        Same as len(q). Returns the number of items in q
        """
        size = 0
        current = self.front
        while current != None:
            size += 1
            current = current.next
        return size
    
    def __str__(self):
        """
        Same as str(q). Returns the string representation of q .
        """
        if self.isEmpty():
            return "Queue is empty"
        else:
            current = self.front
            s = ""
            while current != None:
                s += str(current.data) + " "
                current = current.next
            return s
        
    def __iter__(self):
        """
        Same as iter(q), or for item in q. Visits each
            item in q , from front to rear.
        """
        current = self.front
        while current is not None:
            yield current.data
            current = current.next
            
    def __contains__(self, item):
        """
        Same as item in q. Returns True if item is in q or
            False otherwise.
        """
        current = self.front
        while current:
            if current.data == item:
                return True
            current = current.next
        return False
    
    def __add__(self, q2):
        """
        Same as q1 + q2. Returns a new queue containing the
            items in q1 followed by the items in q2 .
        """
        new_queue = LinkedQueue()
        
        for item in self:
            new_queue.add(item)
        
        for item in q2:
            new_queue.add(item)
            
        return new_queue
    
    def __eq__(self, anyObject):
        """
        Same as q == anyObject. Returns True if q equals
            anyObject or False otherwise. Two queues are equal if the
            items at corresponding positions are equal
        """
        if len(self) != len(anyObject):
            return False
        
        for item in self:
            if item not in anyObject:
                return False
        
        return True

    def clear(self):
        """
        Makes q become empty.
        """
        print("Clearing queue")
        self.front = self.rear = None
        
    def peek(self):
        """
        Returns the item at the front of q . Precondition: q must not be
            empty; raises a KeyError if the queue is empty
        """
        if self.isEmpty():
            return None
        else:
            return self.front.data
    
    def add(self, item):
        """
        Adds item to the rear of q 
        """
        new_node = Node(item)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = self.rear.next
            self.rear.data = item
            
    def pop(self):
        """
        Removes and returns the item at the front of q . Precondition: q
            must not be empty; raises a KeyError if the queue is empty
        """
        if self.isEmpty():
            return None
        else:
            # print("Popping")
            data = self.front.data
            self.front = self.front.next
            return data
        
    def remove(self, item):
        """
        Removes the given item in the queue or raise an exception if the item is 
            not found.
        """
        if self.isEmpty():
            return None
        elif self.front.data == item:
            self.front = self.front.next
            return item
        else:
            current = self.front
            while current.next != None:
                if current.next.data == item:
                    current.next = current.next.next
                    return item
                current = current.next
            raise ValueError("Item not found in queue")
        
        
        
# q = LinkedQueue()
# print(f"Queue is empty: {q.isEmpty()}")
# print(f"Length of queue {len(q)}")
# q.add(1)
# q.add(2)
# q.add(3)
# print(f"Length of queue {len(q)}")

# print(f"Queue contents: {q}")
# popped = q.pop()
# print(f"Popped item: {popped}")
# print(f"Queue contents: {q}")

# print(f"Front item of queue: {q.peek()}")
# print(f"Queue is empty: {q.isEmpty()}")

# q.clear()
# print(f"Queue is empty: {q.isEmpty()}")

# q.add(1)
# q.add(2)
# q.add(3)

# print("Iterating through queue")
# for item in q:
#     print(item)

# print(f"Checking if 2 is in queue: {2 in q}")
# print(f"Checking if 4 is in queue: {4 in q}")

# q2 = LinkedQueue()
# q2.add(4)
# q2.add(5)
# print(f"Queue contents: {q}")
# print(f"Queue 2 contents: {q2}")
# print("Concatenating two queues")
# q3 = q + q2
# print(f"Queue 3 contents: {q3}")

# q4 = q3
# print(f"Queue 4 contents: {q4}")
# print(f"Queue 3 and 4 are equal: {q3 == q4}")
# print(f"Queue 3 and 2 are equal: {q3 == q2}")

# print(f"Queue 3 contents: {q3}")
# print(f"Removing 2 from queue 3")
# q3.remove(2)
# print(f"Queue 3 contents: {q3}")