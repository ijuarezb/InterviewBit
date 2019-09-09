import sys



def generateMatrix(A): 

	if A <= 0:
		return 0

	Matrix = [[0 for x in range(A)] for y in range(A)]
	spiral = []

	for i in range(A*A):
		spiral.append(i+1)

	T = 0
	R = A-1
	L = 0
	B = A-1
	direction = 0
	items = (B+1)*(R+1)
	spiral_pivot = 0

	#print(T, B, L, R)

	while T<=B and L<=R:
		if direction == 0:
			for i in range(L, R+1, 1):
				#spiral.append(A[T][i])
				Matrix[T][i] = spiral[spiral_pivot]
				spiral_pivot = spiral_pivot + 1
				#print((Matrix[T][i]))
			T = T + 1
			direction = 1

		elif direction == 1:
			for i in range(T, B+1, 1):
				#spiral.append(A[i][R])
				Matrix[i][R] = spiral[spiral_pivot]
				spiral_pivot = spiral_pivot + 1
				#print((Matrix[i][R]))
			R = R - 1
			direction = 2

		elif direction == 2:
			for i in range(R, L-1, -1):
				#spiral.append(A[B][i])
				Matrix[B][i] = spiral[spiral_pivot]
				spiral_pivot = spiral_pivot + 1
				#print((Matrix[B][i]))
			B = B - 1
			direction = 3

		elif direction == 3:
			for i in range(B, T-1, -1):
				#spiral.append(A[i][L])
				Matrix[i][L] = spiral[spiral_pivot]
				spiral_pivot = spiral_pivot + 1
				#print(Matrix[i][L])
			L = L + 1
			direction = 0



	return Matrix
   
# Driver function to check the above function  
a = 3
print("Matrix", generateMatrix(a))