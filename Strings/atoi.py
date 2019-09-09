#!/usr/bin/env python3
import sys

# Atoi
# https://www.interviewbit.com/problems/atoi/
#
# Please Note:
#
# There are certain questions where the interviewer would intentionally frame the question vague.
# The expectation is that you will ask the correct set of clarifications or state your assumptions before you jump into coding.
#
# Implement atoi to convert a string to an integer.
#
# Example :
#
# Input : "9 2704"
# Output : 9
#
# Note: There might be multiple corner cases here. Clarify all your doubts using “See Expected Output”.
#
#     Questions:
#
#     Q1. Does string contain whitespace characters before the number?
#     A. Yes
#
#     Q2. Can the string have garbage characters after the number?
#     A. Yes. Ignore it.
#
#     Q3. If no numeric character is found before encountering garbage characters, what should I do?
#     A. Return 0.
#
#     Q4. What if the integer overflows?
#     A. Return INT_MAX if the number is positive, INT_MIN otherwise.
#
# Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
# If you do, we will disqualify your submission retroactively and give you penalty points.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        if len(A) < 1:
            return 0
        
        num_str = ''
        number_flag = 0
        num_is_negative = 0
        i = 0

        if (A[0] == '-' and not(A[i+1] >= '0' and A[i+1] <= '9') ):
            return 0
        elif (A[0] == '+' and not(A[i+1] >= '0' and A[i+1] <= '9') ):
            return 0
        elif not(A[0] >= '0' and A[0] <= '9') and A[0] != '+' and A[0] != '-':
            return 0

        for c in A:

            if c >= '0' and c <= '9':
                number_flag = 1
                num_str = num_str + c
                
            if c == '-' and (A[i+1] >= '0' and A[i+1] <= '9') and number_flag == 0:
                num_is_negative = 1

        
            if number_flag == 1 and not(c >= '0' and c <= '9'):
                break

            i = i + 1

            pass

        result = 0
        if number_flag == 1:
            for c in num_str:
                result = result*10 + ord(c) - ord('0')

            if num_is_negative == 1:
                result = result * (-1)
                
            if result > 2147483647:
                return 2147483647

            if result < -2147483648:
                return -2147483648

        return result


class Solution:

    def _bound_result(self, res):
        if res > (1 << 31) - 1:
            return (1 << 31) - 1
        elif res < -(1 << 31):
            return -(1 << 31)
        else:
            return res

    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = A.strip()

        if not len(A):
            return 0

        sign = -1 if A[0] == '-' else 1
        num = A[1:] if A[0] in ['+', '-'] else A
        ans = 0

        for a in num:
            if not a.isdigit():
                return self._bound_result(sign * ans) if ans else 0
            ans = ans * 10 + ord(a) - ord('0')

        return self._bound_result(sign * ans)

    def atoi_ivan(self, A):
        if len(A) < 1:
            return 0
        
        num_str = ''
        number_flag = 0
        num_is_negative = 0
        i = 0

        if (A[0] == '-' and not(A[i+1] >= '0' and A[i+1] <= '9') ):
            return 0
        elif (A[0] == '+' and not(A[i+1] >= '0' and A[i+1] <= '9') ):
            return 0
        elif not(A[0] >= '0' and A[0] <= '9'):
            return 0

        for c in A:

            if c >= '0' and c <= '9':
                number_flag = 1
                num_str = num_str + c

            if c == '-' and (A[i+1] >= '0' and A[i+1] <= '9') and number_flag == 0:
                num_is_negative = 1
            elif c == '+' and (A[i+1] >= '0' and A[i+1] <= '9') and number_flag == 0:
                num_is_negative = 0


            if number_flag == 1 and not(c >= '0' and c <= '9'):
                break

            i = i + 1

            pass

        result = 0
        if number_flag == 1:
            for c in num_str:
                result = result*10 + ord(c) - ord('0')

            if num_is_negative == 1:
                result = result * (-1)

            if result > 2147483647:
                return 2147483647

            if result < -2147483648:
                return -2147483648

        return result


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.atoi("-2147483649"))
    print(s.atoi_ivan("-2147483649"))
    print(s.atoi_ivan("7 U 0 T7165 0128862 089 39 5"))
    print(s.atoi_ivan("7 U 0 T7165 0128862 089 39 5"))
    print(s.atoi_ivan("- 5 88C340185Q 71 8079 834617385 2898422X5297Z6900"))
    print(s.atoi_ivan( "-07041 6784513221729 1128 43144"))
