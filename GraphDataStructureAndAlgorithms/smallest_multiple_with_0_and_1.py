#!/usr/bin/env python3
import sys

# Smallest Multiple With 0 and 1
# https://www.interviewbit.com/problems/smallest-multiple-with-0-and-1/
#
# You are given an integer N. You have to find smallest multiple of N which consists of
# digits 0 and 1 only. Since this multiple could be large, return it in form of a string.
#
# Note:
#
#     Returned string should not contain leading zeroes.
#
# For example,
#
# For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
# For N = 2, 10 is the answer.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A): # Time Limit Exceeded. Almost...
        from collections import deque, defaultdict

        queue, states = deque(), defaultdict(lambda: False)
        queue.append(1)

        while True:
            curr = queue.popleft()

            if not curr % A:
                return curr

            curr = curr * 10
            for num in (curr, curr + 1):
                mod = num % A
                if not states[mod]:
                    states[mod] = True
                    queue.append(num)

    def multiple2(self, A): # Time Limit Exceeded. Naive approach!
        mult = 1
        digits = set('01') 

        while True: 
            result = A * mult 
            if set(str(result)).issubset(digits): 
                return str(result)
            mult += 1
                
        return str(result)


    def multiple3(self, A): # Successful submission.
        from collections import deque, defaultdict

        q = deque()
        vis = [-1] * (A + 1)
        par = [(-1, '1')] * (A + 1)
        tp, p, a1, a2, s = 0, 0, 0, 0, ''
        q.append(1%A)
        vis[1%A] = 1

        while len(q) > 0:
            tp = q.popleft()
            
            if tp == 0:
                s += par[0][1]
                p = par[0][0]

                while( p != -1):
                    s += par[p][1]
                    p = par[p][0]
                s = ''.join(reversed(s))
                return s
            
            a1 = (tp * 10) % A
            a2 = ((tp * 10) % A + 1) % A

            if vis[a1] == -1:   
              q.append(a1)
              vis[a1] = 1
              par[a1] = (tp, '0')

            if vis[a2] == -1:   
              q.append(a2)
              vis[a2] = 1
              par[a2] = (tp, '1')

        return s


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    # print(s.multiple(2))
    # print(s.multiple(17))
    # print(s.multiple(55))
    # print(s.multiple(1))
    # print(s.multiple(9))

    # print(s.multiple2(2))
    # print(s.multiple2(17))
    # print(s.multiple2(55))
    # print(s.multiple2(1))
    # # print(s.multiple2(9))

    # print(s.multiple3(2))
    # print(s.multiple3(17))
    print(s.multiple3(55))
    # print(s.multiple3(1))
    # print(s.multiple3(9))