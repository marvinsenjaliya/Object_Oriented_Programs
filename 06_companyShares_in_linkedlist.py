

class Node:
	def __init__(self,share):
		self.share=share
		self.next=None
	
class LinkedList:
	def __init__(self):
		self.head=None
		
	def insert_share(self,newnode):
		if self.head == None:
			self.head=newnode
		else:
			lastnode=self.head
			while True:
				if lastnode.next==None:
					break
				lastnode=lastnode.next
			lastnode.next=newnode

	def printlist(self):
		if self.head==None:
			print("list is empty")
		else:
			lastnode=self.head
			while True:
				if lastnode==None:
					break
				print(lastnode.data)
				lastnode=lastnode.next

first=Node('john')
linkedlist=LinkedList()
