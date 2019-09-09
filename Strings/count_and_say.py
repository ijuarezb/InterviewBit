#!/usr/bin/env python3
import sys

# Count And Say
# https://www.interviewbit.com/problems/count-and-say/
#
# The count-and-say sequence is the sequence of integers beginning as follows:
#
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as one 1 or 11.
# 11 is read off as two 1s or 21.
#
# 21 is read off as one 2, then one 1 or 1211.
#
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
#
# Example:
#
# if n = 2,
# the sequence is 11.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Solution:

    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        ans = "1"

        while A > 1:
            prev, res, cnt = ans[0], '', 0
            for a in ans:

                if a == prev:
                    cnt += 1
                else:
                    res += "{}{}".format(cnt, prev)
                    cnt = 1

                prev = a
            ans = res + "{}{}".format(cnt, prev)
            A -= 1

        return ans


    def count_and_say(self, A):
    	result = ''

    	#  1 11
    	# 11 21
    	#  2 12
    	# 1, 11, 21, 1211, 111221, ...

    	if A < 1:
    		return ''

    	result = '1'

    	for i in range(1, A):

    		ans = ''
    		print(result)
    		j = 0

    		while j < len(result):
    			if result[j] == '1':
    				if j+1 < len(result) and result[j+1] == '1':
	    				ans = ans + '21'
	    				j = j + 1
	    			else:
	    				ans = ans + '11'
	    		elif result[j] == '2':
	    			ans = ans + '12'
	    		j = j + 1

    		result = ans

    	return result


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(4))
    print(s.countAndSay(5))
    print(s.countAndSay(6))
    print(s.countAndSay(7))
    #print(s.count_and_say(2))