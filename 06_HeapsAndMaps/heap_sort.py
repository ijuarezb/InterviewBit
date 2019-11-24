#!/usr/bin/env python3
import sys

# Implementation of heap sort in python:
def heapsort(A):
   build_max_heap(A)
   for i in range(len(A) - 1, 0, -1):
       A[0], A[i] = A[i], A[0]
       max_heapify(A, index=0, size=i)

def parent(i):
   return (i - 1)//2

def left(i):
   return 2*i + 1

def right(i):
   return 2*i + 2

def build_max_heap(A):
   length = len(A)
   start = parent(length - 1)
   while start >= 0:
       max_heapify(A, index=start, size=length)
       start = start - 1

def max_heapify(A, index, size):
   left_child = left(index)
   right_child = right(index)
   if (left_child < size and A[left_child] > A[index]):
       largest = left_child
   else:
       largest = index
   if (right_child < size and A[right_child] > A[largest]):
       largest = right_child;
   if (largest != index):
       A[largest], A[index] = A[index], A[largest]
       max_heapify(A, largest, size)

# Driver
if __name__ == '__main__':
	A = input('Enter the list of numbers: ').split()
	A = [int(x) for x in A]
	AA = [11, 2, 9, 13, 57, 25, 17, 1, 90, 3]
	heapsort(A)
	print('Sorted list: ', end='')
	print(A)


# Heap declaration :

#     A = []; # declares an empty list / heap. O(1)
#             # Note that heaps are internally implemented using lists for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k. 
# Insert a new key, value pair K, V:

#     heapq.heappush(A, (K, V));     // O(log n)
# Delete the smallest key K ( Note that deleting random key K will be inefficient ) :

#     heapq.heappop(A)[0]
# Find minimum key K in the map ( if the map is not empty ) :

#     A[0][0]
# Size ( number of entries in the map ) :

#     len(A)