#!/usr/bin/env python3
import sys

def binary_search(A, x):
	start = 0
	end = len(A)-1
 
	while start <= end:

		mid = (start + end) // 2

		if A[mid] == x:
			return mid
		elif A[mid] < x:
			start = mid + 1
		else:
			end = mid - 1

	return -1

def binary_search_ocurrences(A, x, search_first):
	start = 0
	end = len(A)-1
	result = -1
 
	while start <= end:

		mid = (start + end) // 2

		if A[mid] == x:
			result = mid
			if search_first:
				end = mid - 1 # searching towards the left (lower indices)
			else:
				start = mid + 1 # searching towards the right (higher indices)

		elif A[mid] < x:
			start = mid + 1
		else:
			end = mid - 1

	return result

def find_rotation_count(A):
	start = 0
	end = len(A) - 1
	n = len(A)

	while start <= end:
		if A[start] <= A[end]:  # Case 1
			return start
		mid = (start + end) // 2
		next_pointer = (mid + 1) % n
		prev_pointer = (mid + n - 1) % n

		if A[mid] <= A[next_pointer] and A[mid] <= A[prev_pointer]: # Case 2
			return mid
		elif A[mid] <= A[end]: # Case 3
			end = mid - 1
		elif A[mid] >= A[start]: # Case 4
			start = mid + 1
		pass

	return -1

# Algorithm:
# 1) Start with ‘start’ = 0, end = ‘x’,
# 2) Do following while ‘start’ is smaller than or equal to ‘end’.
#      a) Compute ‘mid’ as (start + end)/2
#      b) compare mid*mid with x.
#      c) If x is equal to mid*mid, return mid.
#      d) If x is greater, do binary search between mid+1 and end. In this case, we also update ans (Note that we need floor).
#      e) If x is smaller, do binary search between start and mid
#
# Python 3 program to find floor(sqrt(x)  
# Returns floor of square root of x          
def floorSqrt(x) : 
  
    # Base cases 
    if (x == 0 or x == 1) : 
        return x 
   
    # Do Binary Search for floor(sqrt(x)) 
    start = 1
    end = x    
    while (start <= end) : 
        mid = (start + end) // 2
          
        # If x is a perfect square 
        if (mid*mid == x) : 
            return mid 
              
        # Since we need floor, we update  
        # answer when mid*mid is smaller 
        # than x, and move closer to sqrt(x) 
        if (mid * mid < x) : 
            start = mid + 1
            ans = mid 
              
        else : 
              
            # If mid*mid is greater than x 
            end = mid-1
              
    return ans 

if __name__ == "__main__":
	A = [0, 1, 3, 15, 40, 1000, 1005]
	B = [1,1,3,3,5,5,5,5,5,9,9,11]
	C = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]
	C = [ 40342, 40766, 41307, 42639, 42777, 46079, 47038, 47923, 48064, 48083, 49760, 49871, 51000, 51035, 53186, 53499, 53895, 59118, 60467, 60498, 60764, 65158, 65838, 65885, 65919, 66638, 66807, 66989, 67114, 68119, 68146, 68584, 69494, 70914, 72312, 72432, 74536, 77038, 77720, 78590, 78769, 78894, 80169, 81717, 81760, 82124, 82583, 82620, 82877, 83131, 84932, 85050, 85358, 89896, 90991, 91348, 91376, 92786, 93626, 93688, 94972, 95064, 96240, 96308, 96755, 97197, 97243, 98049, 98407, 98998, 99785, 350, 2563, 3075, 3161, 3519, 4176, 4371, 5885, 6054, 6495, 7218, 7734, 9235, 11899, 13070, 14002, 16258, 16309, 16461, 17338, 19141, 19526, 21256, 21507, 21945, 22753, 25029, 25524, 27311, 27609, 28217, 30854, 32721, 33184, 34190, 35040, 35753, 36144, 37342 ]
	#print(s.titleToNumber('AA'))
	#print(s.titleToNumber('A'))
	print(binary_search(A, 1005))
	first_index = binary_search_ocurrences(B,5,True)
	if first_index > -1:
		last_index = binary_search_ocurrences(B,5,False)
		print("The number of occurrences of {} in array is {}".format(5, last_index-first_index+1))
	else:
		print("The number of occurrences of {} in array is {}".format(5, 0))

	print(len(C))
	print("The array is rotated {} times, lowest value is {}".format(find_rotation_count(C), C[find_rotation_count(C)]))

	print(floorSqrt(100))