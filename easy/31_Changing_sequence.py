# Have the function ChangingSequence(arr) take the array of numbers stored in arr and return the index at which the numbers stop increasing and begin decreasing or stop decreasing and begin increasing. For example: if arr is [1, 2, 4, 6, 4, 3, 1] then your program should return 3 because 6 is the last point in the array where the numbers were increasing and the next number begins a decreasing sequence. The array will contain at least 3 numbers and it may contains only a single sequence, increasing or decreasing. If there is only a single sequence in the array, then your program should return -1. Indexing should begin with 0. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def ChangingSequence(arr): 
	counti = 0 
	countd = 0
	for i in range(0,len(arr)-1):
		
		if arr[i+1] > arr[i]:
			counti += 1
			if countd > 0:
				return i
			
		elif arr[i+1] < arr[i]: 
			#print arr[i+1],arr[i]
			countd += 1  
			if counti > 0:
				return i
	return -1
    
# keep this function call here  
print ChangingSequence(raw_input())


# Another Solution :

# def ChangingSequence(arr):
#    sign = lambda x : 1 if x > 0 else -1
#    s = sign(arr[1] - arr[0])
#    for i in xrange(2, len(arr)):
#        if s != sign(arr[i] - arr[i-1]):
#            return i-1
#    return -1  
    
# # keep this function call here  
# # to see how to enter arguments in Python scroll down
# print ChangingSequence(raw_input())