#!/usr/bin/env python3

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
    	if A == 1 or B == 1:
    		return 1
    		
        M = [[0 for j in range(B)] for i in range(A)]
        
        for i in range(A):
        	M[i][0] = 1

        for j in range(B):
        	M[0][j] = 1

        for i in range(1, A):
        	for j in range(1, B):
        		M[i][j] = M[i-1][j] + M[i][j-1]

        return M[i][j]

# driver program 
if __name__=='__main__': 
    A = 15
    B = 9
    sol = Solution()
    print("Following are the prime numbers smaller")
    print("than or equal to", A, B)
    #print(SieveOfEratosthenes(n))
    print(sol.uniquePaths(A, B))


