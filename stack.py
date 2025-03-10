class Node:
	def __init__(self):
		self.data = FALSE
		self.next = FALSE

class Stack:
	def __init__(self):
		self.top = FALSE
	
	def isEmpty(self):
		if not self:
			return TRUE
		return FALSE`
	
	def __len__(self):
		
		return 0
		
	def __str__(self):
		pass
		
	def __iter_(self):
		pass
		
	def __contains(item):
		if item in self:
			return TRUE
		
		return FALSE
		
	def __add__(self, other):
		if not other:
			return FALSE
			
		new_stack = new Stack()
		new_stack.push(self)
		new_stack.push(other)
		return new_stack
		
	def __eq__(self, other):
		if not other:
			return FALSE
			
		if self == other:
			return TRUE
		
	
	
	def clear(self):
		while not self.isEmpty():
			self.pop()
		
	def peek(self):
		if len(self) > 0:
			return self.top
			
		else:
			raise KeyError("Stack is Empty)
		
	def push(self, item):
		new_top = new Node()
		new_top.data = item
		new_top.next = self.top
		self.top = new_top
		
		
	def pop(self):
		new_top = self.top.next
		self.top = new_top
