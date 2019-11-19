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
	print(floorSqrt(100))