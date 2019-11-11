#!/usr/bin/env python3
import sys

# Linked list example in Python
# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign value
        self.next = None  # Initialize next as null
  
# Linked List class
class LinkedList:
    # Function to initialize the Linked List
    def __init__(self): 
        self.head = None

	# Add new node at the Head
    def push(self, data):
    	new_node = Node(data)
    	new_node.next = self.head
    	self.head = new_node

    # Add new node after a specific Node
    def insert_after(self, prev_node, data):
    	if prev_node is None:
    		return -1

    	new_node = Node(data)
    	new_node.next = prev_node.next
    	prev_node.next = new_node
    	return 1

	# Add a new node at the end of the List (append)
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
        	self.head = new_node
        	return 1

        last = self.head
        while last.next != None:
        	last = last.next

        last.next = new_node
        return 1

    # Pop a Node from the Linked List
    def pop(self):
    	if self.head == None:
    		return None
    	data = self.head.data
    	self.delete_node_index(0)
    	return data

	# Delete the first occurrence of a KEY in a Linked List
    def delete_node(self, key):

    	temp = self.head

    	if temp != None:
    		if temp.data == key:
    			self.head = temp.next
    			temp = None
    			return 1

    	while temp != None:
    		if temp.data == key:
    			break
    		prev = temp
    		temp = temp.next

    	if temp == None:
    		return

    	prev.next = temp.next
    	temp = None

    def delete_node_index(self, index):
    	i = 0
    	temp = self.head

    	if self.head == None:
    		return

    	if index == 0:
    		self.head = temp.next
    		temp = None
    		return 1

    	while  temp != None:
    		if i == index:
    			break
    		i += 1
    		prev = temp
    		temp = temp.next

    	if i < index:
    		return

    	prev.next = temp.next
    	temp = None
    	return

    # Get the Lenght of a Linked List
    def get_count(self):
    	count = 0
    	temp = self.head

    	while temp != None:
    		count += 1
    		temp = temp.next
    	
    	return count

    def print_list(self):
    	temp = self.head
    	while  temp:
    		print(temp.data, end=' ')
    		temp = temp.next
    	print("")

# Driver codde
if __name__ == '__main__':

	LL = LinkedList()
	#LL.head = Node(1)
	#second = Node(2)
	#third = Node(3)
	#LL.head.next = second
	#second.next = third
	#LL.print_list();

	#LL.append(6)
	#LL.push(7)
	#LL.append(4)
	#LL.insert_after(LL.head.next, 8)
	#LL.print_list()

	LL.push(7)
	LL.push(1)
	LL.push(3)
	LL.push(2)
	LL.push(8)
	LL.print_list()
	print("the Lenght of LL is {}".format(LL.get_count()))
	#LL.delete_node(1)
	LL.delete_node_index(4)
	print("the Lenght of LL is {}".format(LL.get_count()))
	LL.print_list()

	