from node import Node


class LinkedBag(object):
    """A link-based bag implementation."""
    
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        self.items = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                
    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        return self.size
    
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"
    
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next
    
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result
    
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        
        if self is other: return True
        
        if type(self) != type(other) or \
        len(self) != len(other):
            return False
        
        for item in self:
            if item not in other:
                return False
            
        return True


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = None

    def add(self, item):
        """Adds item to self."""
        self.items = Node(item, self.items)
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self."""
        
        # Check precondition and raise an exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        
        # Search for the node containing the target item
        # probe will point to the target node, and trailer
        # will point to the node before it, if it exists
        probe = self.items
        trailer = None
        while probe is not None and probe.data != item:
            trailer = probe
            probe = probe.next
        
        # Unhook the node to be deleted, either the first one or
        # one thereafter
        if probe is self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next
        
        # Decrement logical size
        self.size -= 1


bag = LinkedBag()

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
bag = LinkedBag(["hello", "goodbye", "this", "that"])
print(f"Bag contents: {bag}")

# Checking bag methods: __add__
print("\nAdding two bags")
bag1 = LinkedBag(["hello", "goodbye"])
bag2 = LinkedBag(["this", "that"])
bag3 = bag1 + bag2
print(bag3)
# bag4 = bag1 + "hello"


# Checking bag methods: __eq__
print("\nChecking if two bags are equal")
bag1 = LinkedBag(["hello", "goodbye"])
bag2 = LinkedBag(["goodbye", "hello"])
print(bag1 == bag2)
bag3 = LinkedBag(["hello", "goodbye", "this"])
print(bag1 == bag3)
print(bag3 == bag1)
# print(bag1 == "hello")
