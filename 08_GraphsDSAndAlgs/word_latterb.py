#!/usr/bin/env python3
import sys

class QItem(): 
	def __init__(self, word, len): 
		self.word = word 
		self.len = len

def is_adjacent(a, b): 
	count = 0
	n = len(a) 
	for i in range(n): 
		if a[i] != b[i]: 
			count += 1
		if count > 1: 
			break
	return True if count == 1 else False

def set_chars_max(n, words):
	for i in range(n):
		S = set()
		for word in words:
			D[i] = S.add(word[i])
	return D

def get_chars_at_index(i, D):
	return D[i]

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
			if temp not in S:  
				if is_adjacent(curr.word, temp): 
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
