class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self, sourceCollection=None):
		self.top = None

		if sourceCollection:
			for item in sourceCollection:
				self.push(item)
	

	def isEmpty(self):
		"""
		Checks if the stack is empty
		"""
		# if not empty, will always have a top
		if not self.top:
			return True

		return False
	
	def __len__(self):
		"""
		Returns the size of the stack
		"""
		size = 0
		current_node = self.top
  
		# loop through the stack to get the size
		while current_node:
			size += 1
			current_node = current_node.next
		return size
		
	def __str__(self):
		"""
		Returns the string representation of the stack
		"""
		items = []

		current_node = self.top
  
		while current_node:
			items.append(current_node.data)
			current_node = current_node.next
   
		# return the items as a string
		if items:
			return ", ".join(items)
		
		return ""
		
	def __iter__(self):
		"""
		Iterates over the stack
		"""
		current_node = self.top
		# loop through the stack
		while current_node is not None:
			# yield the current node data and move to the next node
			yield current_node.data
			current_node = current_node.next
		
	def __contains__(self, item):
		"""
		Checks if the item is in the stack
		"""
		current_node = self.top
  
		# loop through the stack to check if item is in the stack
		while current_node:
			if current_node.data == item:
				return True
			current_node = current_node.next
		return False
		
	def __add__(self, other):
		"""
		Concatenates two stacks
		"""
		if not isinstance(other, Stack):
			raise TypeError("Operands must be Stack")
			
		new_stack = Stack()
  
		# add first stack to new stack
		for item in self:
			new_stack.push(item)

		# add second stack to the top
		for item in other:
			new_stack.push(item)
   
		return new_stack
		
	def __eq__(self, other):
		"""
		Checks if two stacks are equal
		"""
  
		if not isinstance(other, Stack):
			raise TypeError("Operand must be Stack")

		# cannot be equal if they are not the same length
		if len(self) != len(other):
			return False
			
		# check if the items are the same
		for item in self:
			if item not in other:
				return False

		return True
		
	
	
	def clear(self):
		"""
		Clears the stack
		"""
		# if can use garbage collector
		self.top = False

		# if not can use garbage collector
		# while not self.isEmpty():
		# 	self.pop()
		
	def peek(self):
		"""
		Returns the top item in the stack
		"""
		# if not empty, will always have a top
		if len(self) > 0:
			print(self.top.data)
			return self.top.data
			
		else:
			raise KeyError("Stack is Empty")
		
	def push(self, item):
		"""
		Adds an item to the top of the stack
		"""
		new_top = Node(item)

		# if not empty, set the top to be the next of the new top
		if self.top:
			new_top.next = self.top
		
		self.top = new_top
		
		
	def pop(self):
		"""
		Removes the top item from the stack
		"""
		if self.isEmpty():
			raise KeyError("Stack is Empty")

		popped_data = self.top.data
		self.top = self.top.next
    
		# return what is popped, like in a list
		return popped_data  # Return the stored data
	


	def isPalindrome(self):
		"""
		Checks if the stack is a palindrome
		"""
		list1 = []
		list2 = []

		current_node = self.top
		length = len(self)
  
		# get the midpoint
		mid = length // 2

		# loop with a counter, separate into halves
		count = 0
		while current_node:
			if count < mid:
				list1.append(current_node.data)
    
			# if odd, skip the middle element
			elif count >= mid + (length % 2):
				list2.append(current_node.data)

			current_node = current_node.next
			count += 1

		# reverse the second half to mirror first half, if palindrome
		list2 = list2[::-1]
		print(list1)
		print(list2)
		return list1 == list2



# Checking stack methods: isPalindrome
print("\nChecking if stack is palindrome")
stack = Stack(["A", "B", "C", "B", "A"])
print("Input: ABCBA")
print(stack.isPalindrome())

stack = Stack(["h", "a", "n", "n", "a", "h"])
print("Input: hannah")
print(stack.isPalindrome())

stack = Stack(["o", "c", "e", "l", "o", "t"])
print("Input: ocelot")
print(stack.isPalindrome())


"""
Below are the test cases for the stack class,
uncomment everything below to test
"""

# # Example Usage
# stack = Stack()

# # Checking stack methods: add, remove, isEmpty, __str__, __len__
# print(f"stack length: {len(stack)}")
# print(f"stack is empty: {stack.isEmpty()}")
# print(f"stack contents: {stack}")
# stack.push("hello")
# print(f"stack contents: {stack}")
# print(f"stack is empty: {stack.isEmpty()}")
# stack.pop()
# print(f"stack is empty: {stack.isEmpty()}")
# print(f"stack contents: {stack}")
# stack.push("goodbye")
# stack.push("this")
# stack.push("that")
# print(f"stack length: {len(stack)}")
# print(f"stack contents: {stack}")

# # Checking stack methods: __iter__
# print("\nIterating over stack contents:")
# for item in stack:
#     print(item)
    
# # Checking stack methods: clear
# print("\nClearing stack")
# stack.clear()
# print(f"stack is empty: {stack.isEmpty()}")
# print(f"stack contents: {stack}")

# # Checking sourceCollection
# print("\nAdding sourceCollection")
# stack = Stack(["hello", "goodbye", "this", "that"])
# print(f"stack contents: {stack}")

# # Checking stack methods: __add__
# print("\nAdding two stacks")
# stack1 = Stack(["hello", "goodbye"])
# stack2 = Stack(["this", "that"])
# stack3 = stack1 + stack2
# print(stack3)
# # stack4 = stack1 + "hello"


# # Checking stack methods: __eq__
# print("\nChecking if two stacks are equal")
# stack1 = Stack(["hello", "goodbye"])
# stack2 = Stack(["goodbye", "hello"])
# print(stack1 == stack2)
# stack3 = Stack(["hello", "goodbye", "this"])
# print(stack1 == stack3)
# print(stack3 == stack1)
# # print(stack1 == "hello")

# # Checking stack methods: __contains__
# print("\nChecking if item is in stack")
# stack = Stack(["hello", "goodbye", "this", "that"])
# print("hello" in stack)

# # Checking stack methods: pop
# stack = Stack("H")
# print(stack.pop())
# print(stack)