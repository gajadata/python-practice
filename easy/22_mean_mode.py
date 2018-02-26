# Have the function MeanMode(arr) take the array of numbers stored in arr and 
# return 1 if the mode equals the mean, 0 if they don't equal each other 
# (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)).
# The array will not be empty, will only contain positive integers, and will not 
# contain more than one mode. 

# Use the Parameter Testing feature in the box below to test your code with 
# different arguments.

def MeanMode(arr): 

	avg = 0 
	# code goes here 
	for i in arr:
		avg += int(i) 
	avg = avg/len((arr))

	#print len((arr).split())
	frequency = {}

	for i in  arr:
		if i in frequency:
			frequency[i] += 1
		else:
			frequency[i] = 1
	k = 0 
	l = 0
	for i,j in frequency.iteritems():
		if j > k:
			k = j
			l = i 
		else :
			pass
	print avg 
	print l
	if int(avg) == int(l) :
		return 1
	else:
		return 0

	#return arr
    
    
    
# keep this function call here  
print MeanMode(raw_input())


# Another Solution :

# def MeanMode(arr): 
#   mean = sum(arr)/len(arr)
#   nmode = max([arr.count(i) for i in arr])
#   for i in arr:
#     if arr.count(i) == nmode:
#       mode = i
#   return 1 if mean == mode else 0
    
    
# # keep this function call here  
# # to see how to enter arguments in Python scroll down
# print MeanMode(raw_input())