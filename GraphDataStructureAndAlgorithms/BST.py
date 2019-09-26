#!/usr/bin/env python3
import sys

# Implementation of BST in Python:
# Python program to demonstrate insert operation in binary search tree 

#Defining each node containing some value and its children
class TreeNode: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
        #self.visited = False

# Function to insert node in tree recursively
def insertNode(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insertNode(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insertNode(root.left, node) 

# Function to print inorder traversal recursively
def inOrderTraversal(root): 
    if root: 
        inOrderTraversal(root.left) 
        print(root.val, end=" ") 
        inOrderTraversal(root.right)

# Function to print preorder traversal recursively
def preOrderTraversal(root): 
    if root != None: 
        print(root.val, end=" ")
        preOrderTraversal(root.left)  
        preOrderTraversal(root.right)

# Function to print postorder traversal recursively
def postOrderTraversal(root): 
    if root != None: 
        postOrderTraversal(root.left)  
        postOrderTraversal(root.right)
        print(root.val, end=" ") 

def search(root, data):
    if root == None: return False
    elif root.val == data: return True
    elif root.val >= data: return search(root.left, data)
    else: return search(root.right, data)


if __name__ == '__main__':
    # Creating a new BST with root as 50
    # r = TreeNode(55) 
    # insertNode(r,TreeNode(35)) 
    # insertNode(r,TreeNode(25)) 
    # insertNode(r,TreeNode(45)) 
    # insertNode(r,TreeNode(75)) 
    # insertNode(r,TreeNode(65)) 
    # insertNode(r,TreeNode(85)) 

    r = TreeNode(11)
    insertNode(r, TreeNode(2))
    insertNode(r, TreeNode(9))
    insertNode(r, TreeNode(13))
    insertNode(r, TreeNode(57))
    insertNode(r, TreeNode(25))
    insertNode(r, TreeNode(17))
    insertNode(r, TreeNode(1))
    insertNode(r, TreeNode(90))
    insertNode(r, TreeNode(3))

    # Print inoder traversal of the BST 
    inOrderTraversal(r)
    print()
    preOrderTraversal(r)
    print()
    postOrderTraversal(r)
    print()	