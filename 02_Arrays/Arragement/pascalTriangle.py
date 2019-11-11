#!/usr/bin/env python3
import sys

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def printPascal(self, n):
        P = []
      
        for line in range(1, n + 1):  
            C = 1; # used to represent C(line, i)
            L = []
            for i in range(1, line + 1):  
                  
                # The first value in a  
                # line is always 1  
                # print(C, end = " ");
                L.append(C)
                C = int(C * (line - i) / i);  
            #print("");
            P.append(L)
        return P

			

#driver code
if __name__ == "__main__":
    n = 7
    sol = Solution()
    print(sol.printPascal(n))