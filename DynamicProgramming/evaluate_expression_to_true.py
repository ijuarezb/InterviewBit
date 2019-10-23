#!/usr/bin/env python3
import sys

# Evaluate Expression To True
# https://www.interviewbit.com/problems/evaluate-expression-to-true/
#
# Given expression, A, with operands and operators (OR , AND , XOR), in how many ways can you evaluate
# the expression to true, by grouping in different ways? Operands are only true and false.
#
# The string A, may contain these characters:
# here '|' will represent or operator
#      '&' will represent and operator
#      '^' will represent xor operator
#      'T' will represent true operand
#      'F' will false
#
# Output:
# Return an integer, representing the number of ways to evaluate the string.
#
# Constraints:
# 1 <= length(A) <= 150
#
# different ways % MOD
# where MOD = 1003
# Example:
#
# string : T|F
# only 1 way (T|F) => T
# so output will be 1 % MOD = 1
#
# Input 2: A = "T^T^F"
# Output 2: 0
# Explanation 2: There is no way to evaluate A to a true statement.
#
# Input: T|F&T^T
# Output:
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):
        elem = [A[i] for i in range(0, len(A), 2)]
        oper = [A[i] for i in range(1, len(A), 2)]
        n = len(elem)

        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            tmp = elem[i] == 'T'
            dp[i][i][0], dp[i][i][1] = int(tmp), int(not tmp)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                for k in range(i, j):

                    op = oper[k]
                    pre, suf = sum(dp[i][k]), sum(dp[k + 1][j])

                    if op == '&':
                        dp[i][j][0] += dp[i][k][0] * dp[k + 1][j][0]
                        dp[i][j][1] += pre * suf - dp[i][k][0] * dp[k + 1][j][0]
                    elif op == '|':
                        dp[i][j][0] += pre * suf - dp[i][k][1] * dp[k + 1][j][1]
                        dp[i][j][1] += dp[i][k][1] * dp[k + 1][j][1]
                    else:
                        dp[i][j][0] += dp[i][k][0] * dp[k + 1][j][1] + dp[i][k][1] * dp[k + 1][j][0]
                        dp[i][j][1] += dp[i][k][0] * dp[k + 1][j][0] + dp[i][k][1] * dp[k + 1][j][1]

        return dp[0][-1][0] % 1003

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == '__main__':
    s = Solution()
    print(s.cnttrue("T|F"))
    print(s.cnttrue("T^T^F"))
    print(s.cnttrue("T|F&T^T"))
    print(s.cnttrue("T|F^F&T^F"))
    print(s.cnttrue("T^T^T^F|F&F^F|T^F^T"))