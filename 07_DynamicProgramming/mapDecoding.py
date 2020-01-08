#!/usr/bin/env python3
import sys

# A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers 
# using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# You are an FBI agent and you need to determine the total number of ways that the message can be decoded.
#
# Since the answer could be very large, take it modulo 109 + 7.
#
# Example
#
# For message = "123", the output should be
# mapDecoding(message) = 3.
#
# "123" can be decoded as "ABC" (1 2 3), "LC" (12 3) or "AW" (1 23), so the total number of ways is 3.
#
# Input/Output; [execution time limit] 4 seconds (py3)
#
# [input] string message:  A string containing only digits.
# Guaranteed constraints: 0 ≤ message.length ≤ 105.
#
# [output] integer: The total number of ways to decode the given message.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mapDecoding(message):

	if len(message) == 0: return 0
	if len(message) == 1: return int(message[0] != '0')
	if len(message) == 2: return ((1 if 10 <= int(message[:2]) <= 26 else 0) + (message[1] != '0'))*(message[0] != '0')

	dp = {}
	dp[0] = 1
	dp[1] = (1 if 10 <= int(message[:2]) <= 26 else 0) + (message[1] != '0')

	for i in range(2, len(message)):
		if message[i] == '0' and message[i-1] not in ('1', '2'):
			return 0

		if 10 <= int(message[i-1:i+1]) <= 26 and int(message[i-2:i]) != 10:
		 	dp[i] = dp[i-1] * (int(message[i]) != 0) + dp[i-2] * (1 if 10 <= int(message[i-1:i+1]) <= 26 else 0)
		else:
			dp[i] = dp[i-1] - (int(message[i-1:i+1]) == 10)

	return dp[i]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    print(mapDecoding("0"))
    print(mapDecoding("12"))
    print(mapDecoding("10"))
    print(mapDecoding("01"))
    print(mapDecoding("100"))
    print(mapDecoding("101"))
    print(mapDecoding("110"))
    print(mapDecoding("111"))
    print(mapDecoding("301"))
    print(mapDecoding("10122110"))
    print(mapDecoding("2871221111122261"))
    print(mapDecoding("1221112111122221211221221212212212111221222212122221222112122212121212221212122221211112212212211211"))