#!/usr/bin/env python3
import sys

# Kth Permutation Sequence
# https://www.interviewbit.com/problems/kth-permutation-sequence/
#
# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3 ) :
#
# 1. "123"
# 2. "132"
# 3. "213"
# 4. "231"
# 5. "312"
# 6. "321"
# Given n and k, return the kth permutation sequence.
#
# For example, given n = 3, k = 4, ans = "231"
#
#  Good questions to ask the interviewer :
# What if n is greater than 10. How should multiple digit numbers be represented in string?
#  In this case, just concatenate the number to the answer.
# so if n = 11, k = 1, ans = "1234567891011" 
# Whats the maximum value of n and k?
#  In this case, k will be a positive integer thats less than INT_MAX.
# n is reasonable enough to make sure the answer does not bloat up a lot. 
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# A method to get all permutations of an array with 1 to n integers. Result a list with n! arrays
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # @param A : list of integers
    # @return a list of list of integers
    def _permute(self, xs, low=0):
        xs = xs[:]
        if low + 1 >= len(xs):
            yield xs
        else:
            for p in self._permute(xs, low + 1):
                yield p
            for i in range(low + 1, len(xs)):
                xs[low], xs[i] = xs[i], xs[low]
                for p in self._permute(xs, low + 1):
                    yield p
                xs[low], xs[i] = xs[i], xs[low]

    def permute(self, A):
        return list(self._permute(A))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Kth item in permutations of an array of 1 to n integers. Correct result, time exceeded.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def permute_ijb(self, A):
        if len(A) == 1: return [A]

        result = []
        for i in range(len(A)):
            for item in self.permute_ijb(A[:i] + A[i+1:]):
                result.append([A[i]] + item)

        return result

    def k_permutation(self, A, B):
        arr = [i+1 for i in range(A)]
        return ''.join(map(str, self.permute_ijb(arr)[B-1]))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Kth item in permutations of an array of 1 to n integers.  Successful submission!
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def getPermutation(self, n, k):
        d = {0: 1}
        
        for i in range(1, n+1):
            d[i] = d[i-1] * i
        l = [i+1 for i in range(n)]
        s = ""
        while k:
            i = k // d[len(l)-1]
            if i == len(l):
                s += str(l[-1])
                k -= (i) * d[len(l)-1]
                l.pop(-1)
            else:
                
                k -= (i) * d[len(l)-1]
                if not k:
                    s += str(l[i-1])
                    l.pop(i-1)
                else:
                    s += str(l[i])
                    l.pop(i)
        
        if l:
            s += ''.join(map(str,l[::-1]))
        return s

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Kth item in permutations of an array of 1 to n integers.  Successful submission! Nice approach!!!
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def getPermutation(self, A, B):
        return self.helper([x+1 for x in range(A)], A, B )
        
    def helper(self, nums, A, B):
        if A == 1:
            return str(nums[0])
        i = (B-1)//math.factorial(A-1)
        return str(nums[i]) + self.helper(nums[:i]+nums[i+1:], A - 1, (B-1)%math.factorial(A-1)+1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
    print(s.k_permutation(3, 4))
    print(s.getPermutation(8, 82))
    print(s.k_permutation(8, 82))


# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @return a strings
#     def getPermutation(self, n, k):
#         d = {0: 1}
        
#         for i in range(1,n+1):
#             d[i] = d[i-1]*i
#         #print d
#         l = range(1,n+1)
#         s = ""
#         while k:
#             i = k/d[len(l)-1]
#             #print k/d[len(l)-1], i
#             if i == len(l):
#                 s += str(l[-1])
#                 k -= (i)*d[len(l)-1]
#                 l.pop(-1)
#             else:
                
#                 k -= (i)*d[len(l)-1]
#                 if not k:
#                     s += str(l[i-1])
#                     l.pop(i-1)
#                 else:
#                     s += str(l[i])
#                     l.pop(i)
                
#             #print s
        
#         if l:
#             s += ''.join(map(str,l[::-1]))
#         return s

# >>> Editorial <<<
# from math import factorial as fact
# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @return a strings
#     def getPermutation(self, A, B):
#         digits = [str(i) for i in range(1,A+1)]
#         return self.recurse(digits, B-1)
#        
#     def recurse(self, digits, k):
#         n = len(digits)
#         if n == 1:
#             return digits[0]
#        
#         di = k/fact(n-1)
#         k2 = k%fact(n-1)
#         d = digits[di]
#         digits = digits[:di] + digits[di+1:]
#         return d + self.recurse(digits, k2)