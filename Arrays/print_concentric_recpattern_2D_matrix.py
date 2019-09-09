#!/usr/bin/env python3
import sys

# Python3 program for printing 
# the rectangular pattern 

# Function to print the pattern 
def printPattern(n) : 

	# number of rows and columns to be printed 
	s = 2 * n - 1
	M = [[0 for i in range(s)] for j in range(s)]
	rows = 0

	# Upper Half 
	for i in range(0, int(s / 2) + 1): 
		
		m = n
		indexi = 0
		indexj = 0
		

		# Decreasing part 
		for j in range(0, i): 
			M[i][j] = m 
			m-=1
			indexi += 1
			indexj += 1
		
		# Constant Part 
		for k in range(0, s - 2 * i): 
			M[i][k+indexi] = n-i
			indexj += 1

		
		# Increasing part. 
		m = n - i + 1
		for l in range(0, i): 
			M[i][l+indexj] = m 
			m+=1
		
		rows += 1 
	
	# Lower Half 
	rows -= 1
	for i in range(int(s / 2),-1,-1): 

		m = n 
		indexi = 0
		indexj = 0

		
		# Decreasing Part
		#print("rows: {}".format(rows))
		for j in range(0, i): 
			M[rows][j] = m 
			m-=1
			indexi += 1
			indexj += 1
		

		# Constant Part. 
		#print("rows: {}".format(rows))
		for k in range(0, s - 2 * i): 
			M[rows][k+indexi] = n-i
			indexj += 1
		

		# Decreasing Part 
		#print("rows: {}".format(rows))
		m = n - i + 1
		for l in range(0, i): 
			M[rows][l+indexj] = m 
			m+=1
		
		rows += 1

	return M
	
# Driven Program 
if __name__=='__main__': 
	n = 4
	print(printPattern(n))

# this code is contributed by Smitha Dinesh 
# Semwal 
