class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.top = False
	
	def isEmpty(self):
		if not self:
			return True
		return False
	
	def __len__(self):
		
		return 0
		
	def __str__(self):
		pass
		
	def __iter_(self):
		pass
		
	def __contains(item):
		if item in self:
			return True
		
		return False ,
		
	def __add__(self, other):
		if not other:
			return False
			
		new_stack = Stack()
		new_stack.push(self)
		new_stack.push(other)
		return new_stack
		
	def __eq__(self, other):
		if not other:
			return False
			
		if self == other:
			return True
		
	
	
	def clear(self):
		# if can use garbage collector
		self.top = False

		# if not can use garbage collector
		while not self.isEmpty():
			self.pop()
		
	def peek(self):
		if len(self) > 0:
			return self.top
			
		else:
			raise KeyError("Stack is Empty")
		
	def push(self, item):
		new_top = Node()
		new_top.data = item
		new_top.next = self.top
		self.top = new_top
		
		
	def pop(self):
		new_top = self.top.next
		self.top = new_top
