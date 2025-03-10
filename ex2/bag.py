"""
File: baginterface.py
Author: Ken Lambert
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class BagInterface(object):
    """Interface for all bag types."""
    
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.head = None
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
    
    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        if not self.head:
            # No linked list without head node
            return True
        
        return False
    
    def __len__(self):
        """Returns the number of items in self."""
        size = 0
        current_node = self.head
        while current_node:
            # Crawling nodes, incrementing size
            size += 1
            current_node = current_node.next
        return size
    
    def __str__(self):
        """Returns the string representation of self."""
        items = []
        
        current_node = self.head
        while current_node:
            items.append(current_node.data)
            current_node = current_node.next
        
        if items:
            return ", ".join(items)

        return ""
    
    def __iter__(self):
        """Supports iteration over a view of self."""
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next
                
    
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        if not isinstance(other, BagInterface):
            raise TypeError("Operands must be BagInterface")
        
        new_bag = BagInterface()
        
        for item in self:
            new_bag.add(item)
        
        for item in other:
            new_bag.add(item)
        
        return new_bag
    
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if not isinstance(other, BagInterface):
            raise TypeError("Operand must be BagInterface")
        
        if len(self) != len(other):
            return False
        
        for item in self:
            if item not in other:
                return False
        
        return True
    
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        # Following nodes will be garbage collected as they are no longer referenced.
        self.head = None
            
    def add(self, item):
        """Adds item to self."""
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            print("Added item:", item)
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node
        print("Added item:", item)
        return
    
    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        if self.isEmpty():
            raise KeyError(str(item) + " not in bag")
        
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.data == item:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                print("Removed item:", item)
                return
            previous_node = current_node
            current_node = current_node.next
            
        raise KeyError(str(item) + " not in bag")

# Example Usage
bag = BagInterface()

# Checking bag methods: add, remove, isEmpty, __str__, __len__
print(f"Bag length: {len(bag)}")
print(f"Bag is empty: {bag.isEmpty()}")
print(f"Bag contents: {bag}")
bag.add("hello")
print(f"Bag contents: {bag}")
print(f"Bag is empty: {bag.isEmpty()}")
bag.remove("hello")
print(f"Bag is empty: {bag.isEmpty()}")
print(f"Bag contents: {bag}")
bag.add("goodbye")
bag.add("this")
bag.add("that")
print(f"Bag contents: {bag}")

# Checking bag methods: __iter__
print("\nIterating over bag contents:")
for item in bag:
    print(item)
    
# Checking bag methods: clear
print("\nClearing bag")
bag.clear()
print(f"Bag is empty: {bag.isEmpty()}")
print(f"Bag contents: {bag}")

# Checking sourceCollection
print("\nAdding sourceCollection")
bag = BagInterface(["hello", "goodbye", "this", "that"])
print(f"Bag contents: {bag}")

# Checking bag methods: __add__
print("\nAdding two bags")
bag1 = BagInterface(["hello", "goodbye"])
bag2 = BagInterface(["this", "that"])
bag3 = bag1 + bag2
print(bag3)
# bag4 = bag1 + "hello"


# Checking bag methods: __eq__
print("\nChecking if two bags are equal")
bag1 = BagInterface(["hello", "goodbye"])
bag2 = BagInterface(["goodbye", "hello"])
print(bag1 == bag2)
bag3 = BagInterface(["hello", "goodbye", "this"])
print(bag1 == bag3)
print(bag3 == bag1)
# print(bag1 == "hello")
