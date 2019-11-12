#!/usr/bin/env python3
import sys

class QItem(): 
	def __init__(self, word, len): 
		self.word = word 
		self.len = len

def isadjacent(a, b): 
	count = 0
	n = len(a) 
	for i in range(n): 
		if a[i] != b[i]: 
			count += 1
		if count > 1: 
			break
	return True if count == 1 else False

def shortestChainLen(start, target, D): 
	from collections import deque 
	Q, S, item = deque(), set(), QItem(start, 1)

	if start in D:
		D.remove(start)

	if target not in D:
		return 0

	Q.append(item)
	while Q: 
		curr = Q.popleft() 
		if curr.word == target: 
			return curr.len

		for temp in D:  
			if isadjacent(curr.word, temp):
				if temp not in S: 
					item = QItem(temp, curr.len + 1)
					Q.append(item) 
					S.add(temp)
					#D.remove(temp)

	return 0

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    start = "hit"
    end = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(shortestChainLen(start, end, words))

    A = "baxug"
    B = "clgko"
    C = [ "cljkh", "baxbg", "bajbm", "bljkm", "baxug", "cljko", "bajbg", "clnko", "clgko", "bljkh", "bljbm" ]
    print(shortestChainLen(A, B, C))

		
# This code is contributed by Divyanshu Mehta		 
