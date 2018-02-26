# Have the function ThreeSum(arr) take the array of integers stored in arr, and determine if any three distinct numbers (excluding the first element) in the array can sum up to the first element in the array. For example: if arr is [8, 2, 1, 4, 10, 5, -1, -1] then there are actually three sets of triplets that sum to the number 8: [2, 1, 5], [4, 5, -1] and [10, -1, -1]. Your program should return the string true if 3 distinct elements sum to the first element, otherwise your program should return the string false. The input array will always contain at least 4 elements. 

# Use the Parameter Testing feature in the box below to test your code with different arguments.


def ThreeSum(arr): 
  #arr = arr.split(',')
  for i in range(1,len(arr)-1):
    for j in range(i+1,len(arr)-1):
      for k in range(j+1, len(arr)-1):
        #print i,j,k
        #print arr[0]
        print  int(arr[i]) + int(arr[j]) + int(arr[k])
        if int(arr[i]) + int(arr[j]) + int(arr[k]) == int(arr[0]):
          return 'true'
  return 'false'

# keep this function call here  
print ThreeSum(raw_input())