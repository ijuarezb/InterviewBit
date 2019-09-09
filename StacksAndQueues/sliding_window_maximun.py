#!/usr/bin/env python3
import sys

# Sliding Window Maximum
# https://www.interviewbit.com/problems/sliding-window-maximum/
#
# A long array A[] is given to you. There is a sliding window of size w which is moving from the 
# very left of the array to the very right. You can only see the w numbers in the window. Each time 
# the sliding window moves rightwards by one position. You have to find the maximum for each window.
# The following example will give you more clarity.
#
# Example :
#
# The array is [1 3 -1 -3 5 3 6 7], and w is 3.
# Window position 	Max
#
# [1 3 -1] -3 5 3 6 7 	3
# 1 [3 -1 -3] 5 3 6 7 	3
# 1 3 [-1 -3 5] 3 6 7 	5
# 1 3 -1 [-3 5 3] 6 7 	5
# 1 3 -1 -3 [5 3 6] 7 	6
# 1 3 -1 -3 5 [3 6 7] 	7
#
# Input: A long array A[], and a window width w
# Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
# Requirement: Find a good optimal way to get B[i]
#
#     Note: If w > length of the array, return 1 element with the max of the array.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Solution(object):
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        from collections import deque

        if not A or not B:
            return list()

        max_queue = deque()

        for i in range(B):
            while len(max_queue) and A[max_queue[-1]] < A[i]:
                max_queue.pop()
            max_queue.append(i)

        ans = [A[max_queue[0]]]

        for i in range(B, len(A)):
            if max_queue[0] <= i - B:
                max_queue.popleft()

            while len(max_queue) and A[max_queue[-1]] < A[i]:
                max_queue.pop()

            max_queue.append(i)
            ans.append(A[max_queue[0]])

        return ans

    def printMax(self, arr, n, k):
        from collections import deque  

        """ Create a Double Ended Queue, Qi that 
        will store indexes of array elements. 
        The queue will store indexes of useful 
        elements in every window and it will 
        maintain decreasing order of values from 
        front to rear in Qi, i.e., arr[Qi.front[]] 
        to arr[Qi.rear()] are sorted in decreasing 
        order"""
        Qi = deque() 

        # Process first k (or first window) 
        # elements of array 
        for i in range(k): 
            # For every element, the previous
            # smaller elements are useless 
            # so remove them from Qi 
            while Qi and arr[i] >= arr[Qi[-1]] :
            	Qi.pop()

            # Add new element at rear of queue 
            Qi.append(i); 

        print(Qi)

        # Process rest of the elements, i.e. 
        # from arr[k] to arr[n-1] 
        for i in range(k, n): 
            #print(Qi)

            # The element at the front of the 
            # queue is the largest element of 
            # previous window, so print it 
            print(str(arr[Qi[0]]) + " ", end = "") 

            # Remove the elements which are 
            # out of this window 
            while Qi and Qi[0] <= i-k: 
                # remove from front of deque 
                Qi.popleft() 

            # Remove all elements smaller than 
            # the currently being added element 
            # (Remove useless elements) 
            while Qi and arr[i] >= arr[Qi[-1]] :
            	Qi.pop()

            # Add current element at the rear of Qi 
            Qi.append(i)

        # Print the maximum element of last window 
        print(str(arr[Qi[0]])) 

    def printMaxIJB(self, arr, k):
        from collections import deque
        n = len(arr)
        Qi = deque() 

        for i in range(k): 
            while Qi and arr[i] >= arr[Qi[-1]] :
            	Qi.pop()
            Qi.append(i);

        ans = [arr[Qi[0]]]
        for i in range(k, n): 
            #print(str(arr[Qi[0]]) + " ", end = "")
            while Qi and Qi[0] <= i-k: 
                Qi.popleft() 

            while Qi and arr[i] >= arr[Qi[-1]] :
            	Qi.pop()

            Qi.append(i)
            ans.append(arr[Qi[0]])

        #print(str(arr[Qi[0]]))
        return(ans) 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.slidingMaximum([7, 2, 4], 2))
    print(s.slidingMaximum([1, 3, -1, -3, 5, 3, 6, 7], 3))

    # Driver programm to test above fumctions 
    arr = [12, 1, 78, 90, 57, 89, 56] 
    k = 3
    print(arr)
    s.printMax(arr, len(arr), k) 
    print(s.printMaxIJB(arr, k))
    # This code is contributed by Shiv Shankar 