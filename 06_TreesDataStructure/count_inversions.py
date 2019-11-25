#!/usr/bin/env python3
import sys

# An AVL Tree based Python program to 
# count inversion in an array 

# A utility function to get height of 
# the tree rooted with N 
def height(N): 
	if N == None: 
		return 0
	return N.height 

# A utility function to size of the 
# tree of rooted with N 
def size(N): 
	if N == None: 
		return 0
	return N.size 

# Helper function that allocates a new 
# Node with the given key and NULL left 
# and right pointers. 
class newNode: 
	def __init__(self, key): 
		self.key = key 
		self.left = self.right = None
		self.height = self.size = 1

# A utility function to right rotate 
# subtree rooted with y 
def rightRotate(y): 
	x = y.left 
	T2 = x.right 

	# Perform rotation 
	x.right = y 
	y.left = T2 

	# Update heights 
	y.height = max(height(y.left), 
				height(y.right)) + 1
	x.height = max(height(x.left), 
				height(x.right)) + 1

	# Update sizes 
	y.size = size(y.left) + size(y.right) + 1
	x.size = size(x.left) + size(x.right) + 1

	# Return new root 
	return x 

# A utility function to left rotate 
# subtree rooted with x 
def leftRotate(x): 
	y = x.right 
	T2 = y.left 

	# Perform rotation 
	y.left = x 
	x.right = T2 

	# Update heights 
	x.height = max(height(x.left), 
				height(x.right)) + 1
	y.height = max(height(y.left), 
				height(y.right)) + 1

	# Update sizes 
	x.size = size(x.left) + size(x.right) + 1
	y.size = size(y.left) + size(y.right) + 1

	# Return new root 
	return y 

# Get Balance factor of Node N 
def getBalance(N): 
	if N == None: 
		return 0
	return height(N.left) - height(N.right) 

# Inserts a new key to the tree rotted 
# with Node. Also, updates *result (inversion count) 
def insert(node, key, result): 
	
	# 1. Perform the normal BST rotation 
	if node == None: 
		return newNode(key) 

	if key < node.key: 
		node.left = insert(node.left, key, result) 

		# UPDATE COUNT OF GREATE ELEMENTS FOR KEY 
		result[0] = result[0] + size(node.right) + 1
	else: 
		node.right = insert(node.right, key, result) 

	# 2. Update height and size of this ancestor node 
	node.height = max(height(node.left),	 
					height(node.right)) + 1
	node.size = size(node.left) + size(node.right) + 1

	# 3. Get the balance factor of this ancestor 
	#	 node to check whether this node became 
	# unbalanced 
	balance = getBalance(node) 

	# If this node becomes unbalanced, 
	# then there are 4 cases 

	# Left Left Case 
	if (balance > 1 and key < node.left.key): 
		return rightRotate(node) 

	# Right Right Case 
	if (balance < -1 and key > node.right.key): 
		return leftRotate(node) 

	# Left Right Case 
	if balance > 1 and key > node.left.key: 
		node.left = leftRotate(node.left) 
		return rightRotate(node) 

	# Right Left Case 
	if balance < -1 and key < node.right.key: 
		node.right = rightRotate(node.right) 
		return leftRotate(node) 

	# return the (unchanged) node pointer 
	return node 

# The following function returns 
# inversion count in arr[] 
def getInvCount(arr, n): 
	root = None # Create empty AVL Tree 

	result = [0] # Initialize result 

	# Starting from first element, insert all 
	# elements one by one in an AVL tree. 
	for i in range(n): 

		# Note that address of result is passed 
		# as insert operation updates result by 
		# adding count of elements greater than 
		# arr[i] on left of arr[i] 
		root = insert(root, arr[i], result) 

	return result[0] 

# Driver Code 
if __name__ == '__main__': 
	arr = [8, 4, 2, 1] 
	n = len(arr) 
	print("Number of inversions count are :", 
						getInvCount(arr, n)) 

# This code is contributed by PranchalK 
